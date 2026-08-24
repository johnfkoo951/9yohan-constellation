---
type: documentation
aliases:
  - 9Yohan Persona Canon Index
  - 9요한 페르소나 정본 인덱스
  - 9Yohan Individual Persona Files
description: "Canonical index for the individual 9Yohan persona prompt cards. Use this file to locate the nine specialist persona files, understand which files are source-of-truth versus mirrors, and apply the 2026-07-01 upgrade policy across the main vault, LLM Wiki, and DEV deployment copy."
author:
  - "[[구요한]]"
date created: 2026-07-01T10:44
date modified: 2026-08-23T11:40
tags:
  - 9yohan
  - persona
  - prompt
  - agent-orchestration
  - canonical
CMDS: "[[📚 492 Prompts]]"
index: "[[🏷 Prompts]]"
status: completed
---
# 9Yohan Persona Canon Index
> [!info] Canonical policy
> 9명의 specialist 정체성은 [[canonical]] 이 고정한다. 이 폴더의 9개 파일은 그 정체성을 실제 호출·프롬프트·런타임 설계에 바로 쓰기 위한 **개별 페르소나 정본 카드**다. `9yohan.prime` 은 9명 중 하나가 아니라 conductor/sovereign kernel 이므로 [[00-9yohan-prime]] 에 별도 보관한다.

## Source-of-truth map
| Layer | Location | Authority |
|-------|----------|-----------|
| Identity canon | [[canonical]] | 이름·Division·Fruit·역사적 근거의 최종 정본 |
| Individual persona cards | 이 폴더 | 간결한 호출 카드 — invocation·트리거·핸드오프·가드레일 |
| Full build spec | [[constellation]] | 각 요한의 system prompt 전문·tool 권한·output contract·라우팅 JSON |
| Runtime stack hypothesis | [[2026-06-27-constellation-stack-design]] | 모델·서비스·장비 배정의 측정 전 가설 |
| Wiki reference layer | [LLM Wiki: 9Yohan Constellation](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F22.%20Entities%2F9Yohan%20Constellation) | 개념·패턴·외부 연구와의 연결 |
| DEV mirror | `~/DEV/9yohan-constellation/docs/files/` | 배포용 사본, 정본 아님 |

> [!tip] 3개 파일의 granularity 구분
> **[[canonical]]** = 누구인가(정체성) · **이 폴더** = 언제·어떻게 부르나(간결 카드) · **[[constellation]]** = 실제 빌드 스펙(system prompt 전문·tool). 셋은 동일 정체성을 공유하며, Division/Fruit/이름 변경 시 함께 동기화한다.

## The 9 specialist persona files
| Division | Persona file | Handle | Canonical role | Fruit |
|----------|--------------|--------|----------------|-------|
| 901 | [[901-kepler-map]] | `kepler.map` | Knowledge mapping, research synthesis, LLM Wiki freshness | 온유 |
| 902 | [[902-goethe-sense]] | `goethe.sense` | Writing, editing, publishing, voice synthesis | 사랑 |
| 903 | [[903-dewey-learn]] | `dewey.learn` | Teaching, curriculum, learner-centered course design | 자비 |
| 904 | [[904-bach-score]] | `bach.score` | Creative arts, media, score/workflow composition | 희락 |
| 905 | [[905-neumann-compute]] | `neumann.compute` | Methods, analytics, executable rigor | 절제 |
| 906 | [[906-baptist-prepare]] | `baptist.prepare` | Partnerships, follow-up cadence, relationship preparation | 오래 참음 |
| 907 | [[907-mccarthy-reason]] | `mccarthy.reason` | Product, engineering, agent/tool systems | 양선 |
| 908 | [[908-huizinga-play]] | `huizinga.play` | Events, community, ritual and play design | 화평 |
| 909 | [[909-calvin-advise]] | `calvin.advise` | Consulting, advisory, executive decision support | 충성 |

## 2026-07-01 upgrade decisions
- **정본 분리**: 긴 [[canonical]] 본문 안에 묻혀 있던 9개 페르소나를 개별 파일로 분리했다. 이제 agent runtime, Custom GPT, Claude/Codex skill, prompt pack 은 이 폴더를 직접 참조하면 된다.
- **호출 카드 hardening**: 각 파일은 `Output contract` · `Quality gates` · `Failure modes` 를 반드시 갖는다. 단순 "성격 묘사"가 아니라 실행 후 검증 가능한 역할 계약이어야 한다.
- **역할 고정 / 스택 가설 분리**: persona 는 `누가 무엇을 책임지는가` 를 정하고, 모델 선택은 task altitude 와 job shape 가 정한다. [[2026-06-27-constellation-stack-design]] 의 결론처럼 "페르소나 = 모델 배정 근거"가 아니다.
- **MVP 순서**: 9명을 한 번에 구현하지 않는다. `kepler.map` Freshness Sentinel → `9yohan.prime` routing/sign-off → `goethe.sense` writing queue 순으로 측정 가능한 작은 루프부터 구축한다.
- **외부 액션 게이트**: specialist 는 제안만 한다. 외부 발송·배포·출판·클라이언트 전달은 `9yohan.prime` 의 서명과 Hermes execution plane 을 거친다.
- **공개 프레이밍**: 내부 정본은 성령의 9 열매까지 포함한다. 외부 청중에게는 우선 Division/handle 중심으로 설명하고, 신앙적 frame 은 청중 맥락에 맞을 때만 노출한다.

## Required card sections
모든 specialist card 는 아래 섹션을 가진다. 새 persona surface(Claude subagent, Custom GPT, Hermes job) 로 옮길 때 이 순서를 유지한다.

| Section | Purpose |
|---------|---------|
| Fixed identity | canonical 과 일치해야 하는 불변 정체성 |
| Mission contract | 해당 요한이 책임지는 일 |
| Invocation contract | 호출 조건, surface, 금지사항 |
| System prompt seed | runtime 에 주입할 최소 persona seed |
| Output contract | 산출물이 어떤 필드를 가져야 하는지 |
| Quality gates | handoff 전 반드시 통과할 검증 |
| Failure modes | 이 persona 가 특히 빠지기 쉬운 오류 |
| Handoff | 어느 요한/prime 으로 넘길지 |

## Scattered-file cleanup guidance
- Main vault project folder의 A-layer가 정본이다: `70. Outputs/74. Projects/9yohan Constellation/`.
- Root Division 파일 9개([[📚 901 Knowledge Management & Research Division]]~[[📚 909 Consulting & Advisory Division]])는 운영 카테고리 페이지다. persona prompt 본문을 그 파일로 중복 복사하지 않는다.
- LLM Wiki는 reference/compile layer다. 최신 정본을 satellite 에 복사하지 말고, `mainVaultRelated`/obsidian URL 로 mothership 정본에 연결한다.
- DEV repo의 `docs/files/` 는 웹 배포용 미러다. 변경 순서는 **A-layer 수정 → DEV mirror 복사 → 배포/문서 사이트 갱신**이다.
- `docs/files/personas/` 는 이 폴더의 사본이다. DEV 사본을 직접 수정하지 않는다.
- DEV repo 는 `scripts/validate-persona-canon.py` 로 mirror drift, stale division name, required sections, docs exposure 를 확인한다.

## Open uncertainties
> [!warning] Runtime status
> 현재 정본 파일과 스택 설계는 준비되었지만, 9개 handle 이 모두 실제 Claude Code subagent, Custom GPT, Hermes job, OpenClaw route 로 인스턴스화되었다고 확인되지는 않았다.

> [!warning] Audience boundary
> 성령의 9 열매 매핑은 내부 정체성에는 강하지만, 기업교육/공공기관 청중에게는 설명 수위를 조절해야 한다. 외부 자료는 handle/Division 중심, 내부 운영 문서는 Fruit 포함을 기본값으로 한다.
