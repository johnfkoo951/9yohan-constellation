---
type: note
aliases:
  - 9yohan Architecture
  - 9요한 아키텍처
description: Technical architecture spec for the 9Yohan orchestration system. Covers orchestration topology (star with selective mesh), 4-layer harness (routing/memory/communication/persona), LLM-based dynamic routing prompt, mixed sequential/parallel invocation patterns, and a 5-phase implementation roadmap. Reference when implementing the platform in OpenClaw or Hermes.
author:
  - "[[구요한]]"
date created: 2026-04-19
date modified: 2026-04-19
tags:
  - agent-orchestration
  - harness-design
  - routing
  - multi-agent
  - architecture
CMDS: "[[📚 620 Generative AI]]"
status: inProgress
---

# 9요한 오케스트레이션 아키텍처

## 1. 전체 토폴로지

```
              ┌──────────────────────────┐
              │    9요한 (Meta-Agent)    │
              │                          │
              │  · Intent Understanding  │
              │  · Dynamic Routing (LLM) │
              │  · Context Curation      │
              │  · Result Synthesis      │
              └────────────┬─────────────┘
                           │
     ┌──────────┬──────────┼──────────┬──────────┐
     │          │          │          │          │
  ┌──▼───┐  ┌──▼───┐   ┌──▼───┐   ┌──▼───┐   ...(총 9명)
  │ 901  │  │ 902  │   │ 907  │   │ 909  │
  │사도요한│ │구텐베르크│ │폰노이만│ │요바2세│
  └──┬───┘  └──┬───┘   └──┬───┘   └──┬───┘
     │         │          │          │
     └─────────┴────┬─────┴──────────┘
                    ▼
            ┌──────────────────┐
            │  Shared Memory   │
            │  (CMDS Vault)    │
            └──────────────────┘
```

**패턴**: Star topology (기본) + Selective mesh (9요한이 허가한 직결 협업 예외).

**왜 star인가**: 모든 라우팅 로직이 9요한 한 곳에 모여 디버깅·관찰이 쉽다. 2-hop 패턴(A→B→C)이 반복적으로 관찰될 때만 mesh로 승격.

---

## 2. 하네스 4계층

### 2.1 라우팅 계층 (Routing Layer)

9요한의 핵심 책임. 결정 방식: **LLM 기반 동적 라우팅** (결정 ①).

흐름:

1. 사용자 입력 수신
2. 입력을 구조화: `intent` · `artifact_type` · `urgency` · `complexity`
3. 9개 에이전트 프로파일과 대조 (description + trigger_keywords + past_performance)
4. 라우팅 결정 산출: `single` / `sequential` / `parallel` (결정 ②)
5. Dispatch

**라우팅 프롬프트 템플릿** — 9요한 system prompt에 포함:

```
당신은 9요한, 구요한의 메타 에이전트입니다.
아래 9명의 스페셜리스트 중 누구에게 이 요청을 맡길지 결정합니다.

사용 가능한 에이전트:
- 사도요한 (901): 연구·PKM·문헌 통합    · keywords: [연구, 논문, 볼트, 문헌, 리뷰]
- 구텐베르크 (902): 편집·출판·배포      · keywords: [편집, 뉴스레터, 발행, 포스트]
- 페스탈로치 (903): 교육·커리큘럼·강의   · keywords: [강의, 커리큘럼, 수업, 워크숍]
- 바흐 (904): 창작·음악·영상·디자인     · keywords: [영상, 음악, 디자인, 썸네일]
- 케플러 (905): 데이터·통계·ML          · keywords: [데이터, 분석, 통계, 예측]
- 세례요한 (906): 외부 소통·제안·네트워킹 · keywords: [이메일, 제안, 고객, 파트너]
- 폰노이만 (907): 개발·자동화·인프라      · keywords: [코드, 플러그인, API, 배포]
- 하위징아 (908): 이벤트·커뮤니티         · keywords: [이벤트, 스터디, 운영, 모임]
- 요한바오로2세 (909): 컨설팅·조언         · keywords: [컨설팅, 전략, 진단, 로드맵]

요청: {user_input}

판단 기준:
- 단순/명확한 단일 주제 → single
- 한 결과가 다음 입력이 됨 → sequential
- 독립적 서브태스크 여러 개 → parallel

출력 (JSON):
{
  "intent": "<의도 1줄 요약>",
  "routing": "single" | "sequential" | "parallel",
  "agents": ["<에이전트명>", ...],
  "reasoning": "<왜 이 선택인지 1~2줄>"
}
```

**향후 최적화 경로**: 키워드 일치가 확실한 경우를 1차 필터로 두고 LLM 호출을 건너뛰는 "2-stage gate"로 승격 가능 (비용·지연 절감).

---

### 2.2 메모리 계층 (Memory Layer)

3층 구조:

| 계층 | 위치 | 접근권 | 용도 |
|------|------|--------|------|
| **Shared Long-term** | CMDS Vault 전체 | 모든 에이전트 Read · 9요한이 조율한 Write | 진실의 원천. 최종 산출물 보관. |
| **Agent Scratch** | `00. Inbox/03. AI Agent/agents/{name}/` | 해당 에이전트만 R/W | 작업 중간물 · 페르소나별 사유 · 재사용 가능한 부분 산출 |
| **Session Context** | 9요한 세션 윈도우 | 9요한만 유지 | 대화 흐름 · 라우팅 이력 · 결과 합성용 작업 메모리 |

**설계 이유**: Shared Long-term을 모든 에이전트가 마음대로 write하면 볼트 일관성이 깨짐. 9요한이 "이 산출은 vault에 영구 저장한다" 판단할 때만 commit.

---

### 2.3 통신 계층 (Communication Layer)

**기본**: Star (모든 통신이 9요한을 경유)
**예외**: 9요한이 `allow_direct_link=true` 플래그로 명시 시 specialist ↔ specialist 직결 허용

**메시지 포맷** (JSON):

```json
{
	"from": "9yohan",
	"to": "von-neumann",
	"task_id": "uuid",
	"intent": "플러그인 리팩토링",
	"context": {
		"files": ["plugin/main.ts"],
		"constraints": ["no breaking API changes"],
		"history": ["이전 논의 요약"]
	},
	"depends_on": [],
	"return_to": "9yohan"
}
```

`depends_on` 필드로 순차 체인 표현, 비어 있으면 병렬 가능.

---

### 2.4 페르소나 계층 (Persona Layer)

각 에이전트는 독립된 3요소 보유:

- **system prompt** (인물 원형 반영)
- **tool set** (권한 목록)
- **memory namespace** (자기 scratch 경로)

상세 정의는 `constellation.md` 참조.

---

## 3. 호출 패턴 (결정 ② 구체화)

### 3.1 Single — 단일 호출

단순 명확한 요청.

> 예: "오늘 미팅 노트 정리해줘" → **사도요한** 단독

### 3.2 Sequential — 순차 체인

한 에이전트 산출물이 다음 에이전트 입력.

> 예: "LG AX 강의안 만들어줘"
> → **사도요한** (관련 문헌·이전 강의 자료 발굴)
> → **페스탈로치** (커리큘럼 설계 · 모듈화)
> → **구텐베르크** (슬라이드 스크립트 편집)

### 3.3 Parallel — 병렬 분산

독립적 서브태스크를 동시 처리, 마지막에 합류.

> 예: "월간 뉴스레터 발행"
> ├─ **사도요한** (이번 달 인사이트 추출)
> └─ **바흐** (헤더 이미지 생성)
> → **구텐베르크** (레이아웃 · 발송)

9요한이 매 요청마다 위 3패턴 중 선택.

---

## 4. OpenClaw vs 헤르메스 (결정 ③)

**현재 방침**: 둘 다 유연하게 사용 · 실사용 패턴 누적 후 Phase 4에서 역할 분담 확정.

**잠정 가설** (검증 전, 이름에서 유추):

| 플랫폼 | 잠정 역할 |
|--------|---------|
| **OpenClaw** | 에이전트 실행 런타임 — 페르소나 적용, 툴 호출, 컨텍스트 관리 |
| **헤르메스** | 메시지 전달 레이어 — 스케줄링, 알림, 외부 시스템(Slack/Gmail/Calendar) 연동. 이름 그대로 "전령". |

**검증 방법**: 3~4주간 같은 에이전트를 양쪽에서 부르며 로그 수집 → "헤르메스에 더 잘 맞았던 것 / OpenClaw가 더 잘한 것" 데이터 기반으로 확정.

---

## 5. 구현 로드맵

| Phase | 목표 | 기간 |
|-------|------|------|
| **Phase 0** | 이 설계 확정 + 907 폰 노이만 프로토타입 구현 | 1주 |
| **Phase 1** | 9요한 라우터 구현 · 907 단독 라우팅 테스트 | 2주 |
| **Phase 2** | 고빈도 3개 추가 (903 페스탈로치 · 904 바흐 · 905 케플러) | 3주 |
| **Phase 3** | 나머지 4개 추가 + 직결 협업(mesh) 허용 | 4주 |
| **Phase 4** | OpenClaw/헤르메스 역할 분담 확정 · 마이그레이션 | 2주 |

**Phase 0에 907을 고른 이유**: 개발 작업 자체가 에이전트 구현 도구이기도 해서 "자기 손으로 자기 몸을 만드는" 피드백 루프가 가장 빠르게 돈다.

---

## 6. 관찰 포인트 (Phase 1 이후 지속 모니터링)

- **라우팅 오판 빈도** → 프롬프트 튜닝 or 키워드 보강 신호
- **순차 vs 병렬 선택 적절성** → 9요한의 complexity 판단 기준 개선
- **에이전트 간 responsibility overlap** → 페르소나 경계 재정의
- **쓰지 않는 에이전트 발생** → 다른 에이전트에 흡수 or 제거 고려
- **OpenClaw / 헤르메스 사용 편중** → Phase 4 역할 분담 데이터

---

## 🔗 관련

- `README.md` · 설계 개요 및 네비게이션
- `constellation.md` · 각 에이전트 페르소나 정의
- [[CLAUDE.md]] · 볼트 기술 규칙
- [[CMDS.md]] · 900 Divisions 상세
