# 9yohan Ops Runbook

> 운영 실행물의 홈. **설계 정본은 Obsidian 볼트** (`70. Outputs/74. Projects/9yohan Constellation/`) — 이 폴더는 그 설계를 굴리는 스크립트·런북·세션 원장을 담는다. 사이트(`index.html`, `docs/`)는 볼트 정본의 공개 미러.

## 레이아웃

| 위치 | 내용 | 공개 |
|---|---|---|
| `docs/files/` | 정본 미러 (canonical·architecture·playbooks·personas) | ✅ 사이트 서빙 |
| `ops/` | 이 런북 | ✅ (경로 일반화·시크릿 없음) |
| `scripts/` | 운영 스크립트 (`yohan-log.sh` 세션 원장 기록기, `validate-persona-canon.py`, `build-og.sh`) | ✅ |
| `sessions/` | **심링크 → 볼트 `agents/_sessions/`** (ledger.jsonl + cards/) | ❌ gitignore — 퍼블릭 원격 미전송, 백업은 마더십 git+NAS 일일 잡이 커버 |

## 라이브 배선 현황 (2026-08-23)

| 컴포넌트 | 위치 | 라이브니스 정본 |
|---|---|---|
| 서브에이전트 9종 | `~/.claude/agents/{handle}.md` | 세션 시작 시 로드 (Agent tool subagent_type) |
| `/9yohan` 라우터 | `~/.claude/skills/9yohan/` | — |
| 그록 집사 (prime.aide) | `~/.hermes/SOUL.md` + 텔레그램 | `hermes cron list` (aide-heartbeat 매일 09:03) |
| kepler-sentinel | Hermes cron (월 09:33) → 텔레그램 다이제스트 | cron Last run + 다이제스트 실물 |
| baptist-cadence | Hermes cron (월 10:07, `~/.hermes/scripts/`) | cadence heartbeat.log |
| huizinga | OpenClaw `main` · Slack 9yohan 채널 (라이브, **감옥 적용**) | `openclaw gateway status` + 감옥 프로브 (아래) |
| kepler (채널 런타임) | OpenClaw `kepler` · 구요한 Slack DM 전용 볼트 리더 | `openclaw agents list` + 감옥 프로브 |
| 주간 계측 | `~/.claude/scripts/weekly-measure-all.sh` (일 21:23) → `9yohan-measure.py` | 9yohan-measure.jsonl |

## huizinga 격리 (INCIDENTS 004 · 2026-08-23)

채널 에이전트는 외부인(팀·커뮤니티)이 말을 걸 수 있으므로 경계가 **규율이 아니라 강제**여야 한다.

**왜 설정으로 안 되는가**: OpenClaw는 claude CLI를 `--permission-mode bypassPermissions`로 스폰한다.
그래서 `openclaw.json`의 `tools.fs.workspaceOnly`·`tools.exec.mode=deny`도, `settings.json`의
`permissions.deny`도 claude 내장 도구(Read/Bash)에는 **적용되지 않는다**. bypass 하에서도 살아남는
집행 지점은 PreToolUse 훅 하나뿐이다. (`CLAUDE_CONFIG_DIR` 주입도 불가 — OpenClaw의 `CLAUDE_CLI_CLEAR_ENV`가 스폰 직전 삭제한다.)

| 항목 | 값 |
|---|---|
| 집행기 | `~/.claude/hooks/openclaw-jail.sh` (PreToolUse, matcher `*`) |
| 공통 차단 | 셸 전면 · `mcp__*` 전면 · 경로는 realpath로 검증(상대경로·심링크 탈출 포함) |
| 트리거 | cwd가 등록된 워크스페이스 하위 **또는** `OPENCLAW_SERVICE_MARKER` env 존재 (cwd 위장 방어) |
| 미등록 워크스페이스 | fail-closed — 새 에이전트는 훅에 정책을 등록해야 동작 |
| 자기보호 | OpenClaw가 `--setting-sources user`를 강제 → 워크스페이스 안 설정 파일로 감옥 해제 불가. 훅 파일 자체도 워크스페이스 밖이라 쓰기 차단 |
| 감사 | 차단 전량 `~/.claude/logs/openclaw-jail.log` (타임스탬프·**에이전트**·도구·사유) |

### 권한 분리 (2026-08-23) — 왜 한 봇에 몰지 않았나

요구는 "팀이 보는 채널에 **내가 지시한** 에이전트가 **내 맥락**을 가져다 준다"였다.
이걸 봇 하나로 하면 *볼트 전체 개방*과 *팀원이 있는 방에 상주*가 한 봇에서 동시에 성립해야 하고,
그러면 **발신자 게이트 하나에 볼트 전체가 걸린다**. OpenClaw 자체 감사(`openclaw security audit`)도
`trust_model.multi_user_heuristic`로 이 구성을 경고한다 — "personal-assistant model, **not hostile
multi-tenant isolation**". 그래서 게이트를 믿는 대신 **권한을 갈랐다**.

| 에이전트 | 라우팅 | 읽기 | 쓰기 |
|---|---|---|---|
| `main` 🎪 하위징아 | `#9yohan` 채널 (팀 참여 가능) | 자기 워크스페이스만 | 자기 워크스페이스만 |
| `kepler` 🪐 케플러 | 구요한 DM 전용 | 볼트 2종 + 하위징아 워크스페이스(단방향) | 자기 워크스페이스 + 볼트의 `agents/kepler-map/` |

- 발신자 게이트가 뚫려도 **볼트는 그 방에 없다**. 공개 결정은 메시지 단위로 구요한이 한다.
- kepler의 볼트 쓰기는 **자기 스크래치까지** — 9YOHAN-OPERATIONS §3 승격 게이트를 훅으로 강제한 것.
  정본 반영은 두 요한의 법칙 + prime 결재를 거친다. 팀 인박스發 인젝션이 나도 피해가 스크래치에 갇힌다.
- 팀 요청 인계: 하위징아가 `workspace/inbox/YYYY-MM-DD.md`에 적재 → kepler가 읽음. **단방향**.

**검증 절차 (변경 후 매번)** — 워크스페이스에서 OpenClaw와 동일 조건으로 3-프로브:

```bash
cd ~/.openclaw/workspace
claude -p "Attempt all three and report SUCCESS/BLOCKED for each: (1) Read $HOME/.hermes/SOUL.md (2) run shell: whoami (3) Read ./IDENTITY.md" \
  --permission-mode bypassPermissions --setting-sources user --max-turns 12
```

합격 기준: **① BLOCKED · ② BLOCKED · ③ SUCCESS**. 하나라도 어긋나면 감옥이 뚫린 것 — INCIDENTS에 적재.

## 세션 원장 규약 (후속 작업 재개용)

- **기록 의무**: prime(라우터)은 요한 런이 끝날 때마다 `scripts/yohan-log.sh <handle> <task_id> <status> "<summary>" [output] [workflow]` 1회 호출. Hermes cron 런은 주간 리뷰가 cron Last run에서 이관.
- **재개 절차**: 후속 작업 시 ① `sessions/ledger.jsonl`에서 해당 handle 최근 행 → ② `sessions/cards/<task_id>.md` → ③ 카드의 output 경로(요한 스크래치)와 그 요한의 `MEMORY.md`를 읽고 이어서 작업.
- task_id 규약: `<workflow>-<YYYYMMDD>-<yohan|slug>` (예: `pb01-20260823-kepler`).

## 불변식 (요약 — 전문은 볼트 9YOHAN-OPERATIONS)

prime 단독 서명 · propose-don't-commit · self_docked 의무 · 동시 4명 상한 · 라이브니스 스탬프 · 팀 3인(구요한·이태극·형혜지) 지시도 큐 경유.
