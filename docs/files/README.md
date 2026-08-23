---
type: note
aliases:
  - 9yohan Orchestration README
  - 9요한 오케스트레이션 README
  - 9Yohan Master Index
description: "Master index for the entire 9Yohan multi-agent project. Maps every artifact across the vault orchestration folder, root Division files, system files, LLM Wiki reference pages, and the /DEV/9yohan-constellation/ deployment mirror. Reference first to find any 9Yohan artifact and to understand which file owns which concern."
author:
  - "[[구요한]]"
date created: 2026-04-19T20:46
date modified: 2026-07-01
tags:
  - agent-orchestration
  - openclaw
  - hermes
  - 9yohan
  - multi-agent
  - design-doc
  - master-index
CMDS: "[[📚 620 Generative AI]]"
status: inProgress
---
# 9요한 프로젝트 마스터 인덱스

9요한(구요한)을 메타 오케스트레이터로 두고, CMDS 900 Divisions (901~909) 에 1:1 대응하는 9명의 "요한" 전문가 에이전트를 설계·구현·배포한 **전체 프로젝트의 단일 진입점**.

> "내가 여러 가지 일을 다 잘하고, 모든 부캐를 본캐처럼 탁월하게 사용한다" — 이 정체성을 시스템적으로 externalize 한 구조.
> 정본은 [[canonical]]. 라이브 사이트는 https://9yohan.cmdspace.work.

---

## 🤖 에이전트가 작업 시작 전 자동 로드 (@ import)

이 프로젝트 작업 시 LLM agent 가 반드시 컨텍스트로 가져가야 할 핵심 파일들. 본 README 자체는 entry point 일 뿐, 실 작업은 아래 4 파일 내용을 합쳐 진행한다.

@1. Identity/canonical.md
@1. Identity/personas/README.md
@2. Implementation/constellation.md
@2. Implementation/architecture.md
@ecosystem-plan.md

> 운영 디테일이 필요하면 [[workflows]] · [[playbooks]] · [[schemas]] 도 추가 로드. 리서치 배경은 [[요한쓰]].

---

## 🗺 5-Location Map

9요한 산출물은 **5개의 물리적 위치** 에 분산. 역할이 다르므로 분산 자체는 정상이고, 정본/미러 구분이 핵심이다.

| Location | 경로 | 역할 |
|----------|------|------|
| **A. Orchestration folder** (이 폴더) | `00. Inbox/03. AI Agent/03-1. Claude Code (MBP)/2026-04-19-9yohan-orchestration/` | 설계 문서 · 정본 · 운영 매뉴얼 · 에코시스템 플랜 |
| **B. Vault root — Division files** | [[📖 900 Divisions]] 하위 9 파일 | 각 Division 의 CMDS 카테고리 페이지. 에이전트 매핑 메타데이터 포함 |
| **C. Vault root — System files** | [[CLAUDE.md]] · [[AGENTS.md]] · [[CMDS.md]] · [[🏛 CMDS Head Quarter]] | LLM 컨텍스트로 자동 로드되는 system files. Division 개명·9요한 매핑 반영됨 |
| **D. LLM Wiki reference layer** | `CMDS_LLM_Wiki/20. Wiki/22. Entities/9Yohan Constellation.md` | agent orchestration · Persona-as-Skill · harness 패턴과 연결하는 satellite reference |
| **E. DEV repo** | `~/DEV/9yohan-constellation/` | 배포용 정적 사이트 (HTML/CSS/JS). GitHub + Vercel 연결. 라이브: https://9yohan.cmdspace.work |

---

## 📁 A. Orchestration Folder · 설계·운영 정본

### 🎯 Identity Layer · 정체성

| 파일 | 역할 | 상태 |
|------|------|------|
| [[README]] | (이 파일) **마스터 인덱스** · 5-location map · 의사결정 로그 · 네비게이션 | 🔄 v3 (2026-07-01) |
| **[[canonical]]** | **정본 — 9 Divisions × 9 Johns × 9 Fruits 완전 1:1:1 매핑의 단일 진실원천** | ✅ 확정 2026-04-19 |
| **[[personas/README]]** | **개별 페르소나 정본 인덱스** — 9 specialist prompt cards + `9yohan.prime` conductor card | ✅ 신규 2026-07-01 |

#### Individual persona cards (2026-07-01)
- [[00-9yohan-prime]] — conductor / sovereign kernel (9명과 별도)
- [[901-kepler-map]] · [[902-goethe-sense]] · [[903-dewey-learn]]
- [[904-bach-score]] · [[905-neumann-compute]] · [[906-baptist-prepare]]
- [[907-mccarthy-reason]] · [[908-huizinga-play]] · [[909-calvin-advise]]

### ⚙ Implementation Layer · 구현

| 파일 | 역할 | 상태 |
|------|------|------|
| [[constellation]] | 에이전트 운영 정의 · system prompt 전문 · 도구 · 핸드오프 | ✅ 정본 기반 재작성 완료 |
| [[architecture]] | 하네스 기술 스펙 · 라우팅 로직 · 4-Layer 다이어그램 | ✅ 정본 기반 |

### 🔄 Operations Layer · 실전 운영

| 파일 | 역할 | 상태 |
|------|------|------|
| **[[workflows]]** | 4 워크플로우 패턴 · Control Loop 10단계 · CMDS Stage 매핑 · 통신 구조 · mermaid 다이어그램 | ✅ 신규 2026-04-19 |
| **[[playbooks]]** | 실전 시나리오 10선 (뉴스레터 · 컨설팅 제안서 · 1on1 코칭 · 플러그인 개발 · 의료 AI 킥오프 등) · mermaid sequence 포함 | ✅ 신규 2026-04-19 |
| **[[schemas]]** | 메시지 규격 — Task Packet · Agent Result · Signed Action Packet · Session Record · Trace Event | ✅ 신규 2026-04-19 |

### 🌐 Ecosystem Layer · 생태계 플랜 (NEW · 2026-04-20)

| 파일 | 역할 | 상태 |
|------|------|------|
| **[[ecosystem-plan]]** | **Claude Code · OpenClaw · Hermes 3-tool 생태계 플랜** · Decision Matrix · 4 Phase 로드맵 · **Multi-Machine Topology (MBP=dev / Studio=runtime)** · LLM Wiki 참조 cross-link | 🆕 v0.2 (2026-04-20) |

### 📚 Research Layer · 리서치 아카이브

| 파일 | 역할 | 상태 |
|------|------|------|
| [[요한쓰]] | 선정 리서치 · 7개 외부 AI 어드바이저(ChatGPT · Gemini · grok 등) 제안 아카이브 · 대안 후보 | ✅ §11·§12 추가됨 |

---

## 📚 B. Vault Root · 9 Division 파일 (901~909)

각 Division 의 CMDS 카테고리 페이지. **2026-04-19 6개 부서명 개명** 반영 + alias 로 구 이름 보존 (기존 wikilink 안전).

| 파일 | 에이전트 | Handle | Fruit | 비고 |
|------|---------|--------|-------|------|
| [[📚 901 Knowledge Management & Research Division]] | 케플러 요한 | `kepler.map` | 온유 | — |
| [[📚 902 Writing & Publishing Division]] | 괴테 요한 | `goethe.sense` | 사랑 | 구: Editorial & Content Creation |
| [[📚 903 Teaching & Curriculum Division]] | 듀이 요한 | `dewey.learn` | 자비 | 구: Education & Training. **903↔909 경계 규칙** 적용 |
| [[📚 904 Creative Arts & Media Division]] | 바흐 요한 | `bach.score` | 희락 | — |
| [[📚 905 Research Methods & Analytics Division]] | 노이만 요한 | `neumann.compute` | 절제 | 구: Data Science & Analytics |
| [[📚 906 Partnerships & Networks Division]] | 세례요한 | `baptist.prepare` | 오래 참음 | 구: Partnerships & Outreach |
| [[📚 907 Product & Engineering Division]] | 매카시 요한 | `mccarthy.reason` | 양선 | 구: Technology & Development. 본 프로젝트의 CMDS 카테고리 |
| [[📚 908 Events & Community Engagement Division]] | 하위징아 요한 | `huizinga.play` | 화평 | — |
| [[📚 909 Consulting & Advisory Division]] | 칼뱅 요한 | `calvin.advise` | 충성 | 구: Consulting & Professional Services |

상위: [[📖 900 Divisions]]

---

## 🤖 C. Vault Root · System Files (LLM context)

LLM coding agent 가 자동 로드하는 system files. **Division 개명 · 9요한 매핑 모두 반영됨**.

| 파일 | 9요한 관련 변경 |
|------|----------------|
| [[CLAUDE.md]] | Division 6개 개명 반영 · 9Yohan Constellation 표 · 903↔909 경계 규칙 |
| [[AGENTS.md]] | 동일 (Codex/Cursor/Windsurf 용) |
| [[CMDS.md]] | "9Yohan Constellation (2026-04-19 확정)" 섹션 · 9-row 매핑 표 |
| [[🏛 CMDS Head Quarter]] | 900 Divisions 네비게이션 — 새 부서명 |

---

## 🛰 D. LLM Wiki Reference Layer · `CMDS_LLM_Wiki`

LLM Wiki 는 9Yohan 을 외부 agent/harness 패턴과 연결하는 satellite reference layer 다. 정본을 복사하지 않고 mothership 정본으로 링크한다.

| 파일 | 역할 |
|------|------|

---

## 🚀 E. DEV Repo · `~/DEV/9yohan-constellation/`

배포용 정적 사이트. GitHub + Vercel 자동 배포. **vault 외부**라 wikilink 대상 아님 — 코드 표기 유지.

- **GitHub**: https://github.com/johnfkoo951/9yohan-constellation
- **Live**: https://9yohan.cmdspace.work (Cloudflare DNS A → Vercel · Proxy OFF)
- **Vercel project**: `9yohan-constellation`

| 파일 / 폴더 | 역할 |
|------------|------|
| `index.html` | 메인 랜딩 (v4.3 cmdspace-web-builder · 5 신규 컴포넌트 적용) |
| `docs/index.html` | 상세 문서 페이지 (editorial-docs 템플릿 · 사이드바 TOC · ⌘K 검색) |
| `docs/files/canonical.md` | [[canonical]] 사본 (vault → DEV 복사) |
| `docs/files/personas/` | [[personas/README]] 및 9개 specialist persona card 사본 (vault → DEV 복사) |
| `docs/files/constellation.md` | [[constellation]] 사본 |
| `docs/files/architecture.md` | [[architecture]] 사본 |
| `docs/files/workflows.md` | [[workflows]] 사본 |
| `docs/files/playbooks.md` | [[playbooks]] 사본 |
| `docs/files/schemas.md` | [[schemas]] 사본 |
| `docs/files/yohans.md` | [[요한쓰]] 사본 (영문 파일명) |
| `docs/files/README.md` | [[README]] 사본 |
| `assets/og/templates/og-9yohan-constellation.html` | OG 이미지 생성 템플릿 |
| `scripts/build-og.sh` | OG 이미지 빌드 스크립트 |
| `README.md` | GitHub 레포 리드미 |
| `.vercel/` | Vercel 링크 (gitignored) |

> **E 폴더의 `docs/files/*.md` 는 A 폴더 [[canonical]] 등의 사본**. A 가 정본, E 는 배포용 미러. 변경 시 A → E 복사 필요.

미러 후 검증:

```bash
cd ~/DEV/9yohan-constellation
python3 scripts/validate-persona-canon.py
```

---

## 🛠 E. Skill Reflection (2026-04-20)

이 프로젝트에서 만든 5개 신규 컴포넌트가 **`cmdspace-web-builder` 스킬에 영구 반영**됨. (스킬은 `~/.claude/skills/` 에 있어 vault 외부 — 경로 표기 유지)

| 위치 | 내용 |
|------|------|
| `~/.claude/skills/cmdspace-web-builder/references/LANDING-COMPONENTS.md` | 5 컴포넌트 (Star Topology · Numbered Control Loop · Division Grid · Callout Box · Layer Grid) HTML/CSS/JS 전문 + 함정 주의 (601 lines) |
| `~/.claude/skills/cmdspace-web-builder/SKILL.md` | Landing 섹션에 "확장 컴포넌트 5종" 추가 |
| 관련 vault 노트 | [[2026-04-20-cmdspace-web-builder-new-components]] |

---

## 🎯 핵심 설계 결정 (2026-04-19 확정)

| 결정 사항 | 선택 | 근거 |
|---------|------|------|
| **① 라우팅 방식** | **(B) LLM 기반 동적 판단** | 자연어 의도 분석으로 유연하게 라우팅. 키워드 매칭보다 맥락 이해가 중요한 초기 단계 |
| **② 호출 패턴** | **(C) 순차 + 병렬 혼용** | 9요한이 요청별로 결정. 단순 작업은 단일, 복합 작업은 sequential/parallel 분해 |
| **③ 플랫폼 분담** | **OpenClaw + Hermes 유연 사용** | 둘 다 사용하며 실사용 패턴 누적 → Phase 4(3~4주 후)에 역할 확정 |
| **④ Runtime 호스트** (2026-04-20) | **Mac Studio 전용** | OpenClaw·Hermes 는 Studio 24/7 호스트. MBP 는 dev workshop. 자세한 내용은 [[ecosystem-plan]] §5 |

---

## 🏛 9+1 구조 요약

**메타 오케스트레이터** — 9요한 (Yohan Koo) · 지휘자(conductor)
**9명의 스페셜리스트** — 901~909 Division 에 대응하는 역사적 "요한" 들

| #   | Division                     | 에이전트     | Handle            | Fruit     |
| --- | ---------------------------- | --------- | ----------------- | --------- |
| 901 | KM & Research                | 케플러 요한    | `kepler.map`      | **온유**    |
| 902 | Writing & Publishing         | 괴테 요한     | `goethe.sense`    | **사랑**    |
| 903 | Teaching & Curriculum        | 듀이 요한     | `dewey.learn`     | **자비**    |
| 904 | Creative Arts & Media        | 바흐 요한     | `bach.score`      | **희락**    |
| 905 | Research Methods & Analytics | 노이만 요한    | `neumann.compute` | **절제**    |
| 906 | Partnerships & Networks      | 세례요한      | `baptist.prepare` | **오래 참음** |
| 907 | Product & Engineering        | 매카시 요한    | `mccarthy.reason` | **양선**    |
| 908 | Events & Community           | 하위징아 요한   | `huizinga.play`   | **화평**    |
| 909 | Consulting & Advisory        | 칼뱅 요한     | `calvin.advise`   | **충성**    |

3중 완결 · 상세 근거는 [[canonical]] 참조.

---

## 🧭 읽는 순서 (신규 열람자용)

1. [[README]] (여기) — 전체 5-location map
2. [[canonical]] — 누가 누구인가 (이름·Fruit·근거)
3. [[personas/README]] — 9개 개별 페르소나 파일 정본
4. [[constellation]] — 각자 어떻게 일하는가 (system prompt)
5. [[workflows]] — 어떻게 협업하는가 (패턴·mermaid)
6. [[playbooks]] — 실전 시나리오 10선
7. [[schemas]] — 메시지 규격
8. [[architecture]] — 기술 스펙
9. [[ecosystem-plan]] — Claude Code · OpenClaw · Hermes 3-tool 분업·로드맵
10. [[요한쓰]] — 선정 리서치 (선택)
11. [[2026-06-27-constellation-stack-design]] — **각자 어떤 모델·서비스를 쓰나** (가설 스택 설계 · 2026-06-27)
12. [[2026-06-27-kepler-map-wiki-freshness-sentinel]] — 901 kepler.map 첫 production 워크로드 (LLM Wiki 자동 메인터넌스)

---

## 📝 다음 작업 (2026-07-01 기준)

- [ ] LLM Wiki 에 [[OpenClaw]] · [[Hermes Agent]] 페이지 ingest (2h)
- [x] 9개 specialist 개별 페르소나 파일 정본 분리 — [[personas/README]]
- [x] persona card hardening — Output contract · Quality gates · Failure modes 추가
- [x] DEV mirror drift 검증 스크립트 추가 — `scripts/validate-persona-canon.py`
- [ ] `.claude/agents/kepler.md` 또는 `.agents/skills/kepler-map/SKILL.md` 첫 런타임 파일 작성 ([[901-kepler-map]] 기준) — 현재는 정본 문서 단계
- [ ] 실제 뉴스레터 작업을 Phase 1 테스트로 (1h) — kepler → goethe → bach 체인 작동 관찰
- [ ] [[constellation]] 의 각 에이전트 "자주 맡길 태스크 3가지" TODO 채우기
- [ ] OpenClaw 설치 timing 결정 (Mac Studio 전용 · [[ecosystem-plan]] §5 참조)
- [ ] 3~4주 후 OpenClaw vs Hermes 사용 패턴 리뷰 → Phase 4 실행
- [ ] **MVP 빌드 순서 (2026-06-27 권고)**: kepler.map(Freshness Sentinel) → 9yohan.prime(최소 router) → goethe.sense(더배러). all-Claude + ONE Hermes + one-queue로 시작, 새 provider·런타임은 *측정된 수요로만* 추가 (페르소나 맵으로 밀어넣지 말 것). → [[2026-06-27-constellation-stack-design]] §7

---

## 🔗 관련

- [[CLAUDE.md]] · 기술 규칙
- [[AGENTS.md]] · Codex/Cursor 등 타 agent 규칙
- [[CMDS.md]] · 9 Divisions 설명 + 9Yohan Constellation 매핑 표
- [[🏛 CMDS Head Quarter]] · 900 Divisions 네비게이션
- [[📚 620 Generative AI]] · 상위 카테고리
- [[📚 907 Product & Engineering Division]] · 본 프로젝트 owner Division (매카시 요한)
- [[📚 901 Knowledge Management & Research Division]] · 케플러 요한 (자료 조사)

---

## 📋 문서 이력

- **2026-04-19** — v1 초안. orchestration 폴더 내부 7 파일만 인덱싱.
- **2026-05-03** — **v2 마스터 인덱스로 재작성**. 4-location map 추가 · [[ecosystem-plan]] 섹션 신설 · Vault root 의 9 Division 파일 · System files · DEV repo · skill reflection 모두 명시. Multi-Machine Topology 결정 (Mac Studio runtime) 반영.
- **2026-05-03 (rev2)** — 옵시디언 규칙 적용. 인라인 코드 백틱 → [[wikilink]] 일괄 변환 (vault 내부 파일). 핵심 정본 4개 ([[canonical]] · [[constellation]] · [[architecture]] · [[ecosystem-plan]]) 은 상단에 `@` import 블록으로 명시 — 에이전트 작업 시 자동 로드. DEV/ · `~/.claude/` 등 vault 외부 경로만 코드 표기 유지.
- **2026-07-01** — **v3 페르소나 정본 업그레이드**. LLM Wiki reference layer 를 5-location map 에 추가. `1. Identity/personas/` 아래 9개 specialist card + [[00-9yohan-prime]] conductor card 를 신설하고 DEV mirror 정책 반영.
