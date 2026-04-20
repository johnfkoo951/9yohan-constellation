---
type: note
aliases:
  - 9yohan Orchestration README
  - 9요한 오케스트레이션 README
description: Entry point for the 9Yohan agent orchestration design. Indexes architecture.md (structure/harness/routing spec) and constellation.md (9+1 agent personas). Reference first when understanding, implementing, or evolving the multi-agent system across OpenClaw and Hermes platforms.
author:
  - "[[구요한]]"
date created: 2026-04-19
date modified: 2026-04-19
tags:
  - agent-orchestration
  - openclaw
  - hermes
  - 9yohan
  - multi-agent
  - design-doc
CMDS: "[[📚 620 Generative AI]]"
status: inProgress
---

# 9요한 에이전트 오케스트레이션 설계

9요한(구요한)을 메타 오케스트레이터로 두고, CMDS 900 Divisions (901~909)에 1:1 대응하는 9명의 "요한" 전문가 에이전트를 설계한다.

> "내가 여러 가지 일을 다 잘하고, 모든 부캐를 본캐처럼 탁월하게 사용한다" — 이 정체성을 시스템적으로 externalize한 구조.

## 📁 폴더 구성

### 🎯 Identity Layer · 정체성
| 파일 | 역할 | 상태 |
|------|------|------|
| `README.md` | (이 파일) 개요 · 의사결정 로그 · 네비게이션 | — |
| **`canonical.md`** | **정본 · 이름 · Fruit · 근거의 단일 진실원천** | ✅ 확정 2026-04-19 |

### ⚙ Implementation Layer · 구현
| 파일 | 역할 | 상태 |
|------|------|------|
| `constellation.md` | 에이전트 운영 정의 · system prompt 전문 · 도구 · 핸드오프 | ✅ 정본 기반 재작성 완료 |
| `architecture.md` | 하네스 기술 스펙 · 라우팅 로직 · 로드맵 | — |

### 🔄 Operations Layer · 실전 운영
| 파일 | 역할 | 상태 |
|------|------|------|
| **`workflows.md`** | 워크플로우 패턴 · Control Loop 10단계 · CMDS Stage 매핑 · 통신 구조 · 핸드오프 · mermaid 다이어그램 | ✅ 신규 2026-04-19 |
| **`playbooks.md`** | 실전 시나리오 10선 (뉴스레터 · 컨설팅 제안서 · 1on1 코칭 · 플러그인 개발 · 의료 AI 킥오프 등) · 각 시나리오 mermaid sequence 포함 | ✅ 신규 2026-04-19 |
| **`schemas.md`** | 메시지 규격 · Task Packet · Agent Result · Signed Action Packet · Session Record · Trace Event | ✅ 신규 2026-04-19 |

### 📚 Research Layer · 리서치 아카이브
| 파일 | 역할 | 상태 |
|------|------|------|
| `요한쓰.md` | 선정 리서치 · 참고 자료(7개 외부 AI 제안) · 대안 아카이브 | ✅ §11·§12 추가됨 |

## 🎯 핵심 설계 결정 (2026-04-19)

| 결정 사항 | 선택 | 근거 |
|---------|------|------|
| **① 라우팅 방식** | **(B) LLM 기반 동적 판단** | 자연어 의도 분석으로 유연하게 라우팅. 키워드 매칭보다 맥락 이해가 중요한 초기 단계. |
| **② 호출 패턴** | **(C) 순차 + 병렬 혼용** | 9요한이 요청별로 결정. 단순 작업은 단일, 복합 작업은 sequential/parallel 분해. |
| **③ 플랫폼 분담** | **OpenClaw + 헤르메스 유연 사용** | 둘 다 사용하며 실사용 패턴 누적 → Phase 4(3~4주 후)에 역할 확정. |

## 🏛 9+1 구조 요약

**메타 오케스트레이터** — 9요한 (Yohan Koo) · 지휘자(conductor)
**9명의 스페셜리스트** — 901~909 Division에 대응하는 역사적 "요한"들

| # | Division | 에이전트 | Runtime Handle | Fruit |
|---|---------|---------|---------------|------|
| 901 | KM & Research | 케플러 요한 | `kepler.map` | **온유** |
| 902 | Writing & Publishing | 괴테 요한 | `goethe.sense` | **사랑** |
| 903 | Teaching & Curriculum | 듀이 요한 | `dewey.learn` | **자비** |
| 904 | Creative Arts & Media | 바흐 요한 | `bach.score` | **희락** |
| 905 | Research Methods & Analytics | 노이만 요한 | `neumann.compute` | **절제** |
| 906 | Partnerships & Networks | 세례요한 | `baptist.prepare` | **오래 참음** |
| 907 | Product & Engineering | 매카시 요한 | `mccarthy.reason` | **양선** |
| 908 | Events & Community | 하위징아 요한 | `huizinga.play` | **화평** |
| 909 | Consulting & Advisory | 칼뱅 요한 | `calvin.advise` | **충성** |

**확정 · 2026-04-19** · 3중 완결: 9 Divisions × 9 Johns × 9 Fruits 완전 1:1:1 매핑.
상세 근거는 `canonical.md` 참조.

## 📝 다음 작업

- [ ] `constellation.md`의 각 에이전트 "자주 맡길 태스크 3가지" TODO 채우기 (트리거 튜닝에 필수)
- [ ] 9요한 라우팅 프롬프트로 기존 요청 10개 재라우팅 시뮬레이션 (라우팅 품질 검증)
- [ ] Phase 0 프로토타입 대상: **907 매카시 요한** (`mccarthy.reason`) — 개발 작업 빈도 최고, 자기참조적 피드백 루프
- [ ] 3~4주 후 OpenClaw vs 헤르메스 사용 패턴 리뷰 → Phase 4 실행

## 🧭 읽는 순서 (신규 열람자용)

1. **README.md** (여기) — 전체 개요
2. **`1. Identity/canonical.md`** — 누가 누구인가 (이름·Fruit·근거)
3. **`2. Implementation/constellation.md`** — 각자 어떻게 일하는가 (system prompt)
4. **`3. Operations/workflows.md`** — 어떻게 협업하는가 (패턴·mermaid)
5. **`3. Operations/playbooks.md`** — 실전 시나리오 10선
6. **`3. Operations/schemas.md`** — 메시지 규격
7. **`2. Implementation/architecture.md`** — 기술 스펙
8. **`4. Research/요한쓰.md`** — 선정 리서치 (선택)

## 🔗 관련

- [[CLAUDE.md]] · 기술 규칙
- [[CMDS.md]] · 9 Divisions 설명
- [[🏛 CMDS Head Quarter]] · 900 Divisions 네비게이션
- [[📚 620 Generative AI]] · 상위 카테고리
