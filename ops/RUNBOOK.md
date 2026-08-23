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
| huizinga | OpenClaw 2026.7.1 (온보딩 대기) | `openclaw gateway status` |
| 주간 계측 | `~/.claude/scripts/weekly-measure-all.sh` (일 21:23) → `9yohan-measure.py` | 9yohan-measure.jsonl |

## 세션 원장 규약 (후속 작업 재개용)

- **기록 의무**: prime(라우터)은 요한 런이 끝날 때마다 `scripts/yohan-log.sh <handle> <task_id> <status> "<summary>" [output] [workflow]` 1회 호출. Hermes cron 런은 주간 리뷰가 cron Last run에서 이관.
- **재개 절차**: 후속 작업 시 ① `sessions/ledger.jsonl`에서 해당 handle 최근 행 → ② `sessions/cards/<task_id>.md` → ③ 카드의 output 경로(요한 스크래치)와 그 요한의 `MEMORY.md`를 읽고 이어서 작업.
- task_id 규약: `<workflow>-<YYYYMMDD>-<yohan|slug>` (예: `pb01-20260823-kepler`).

## 불변식 (요약 — 전문은 볼트 9YOHAN-OPERATIONS)

prime 단독 서명 · propose-don't-commit · self_docked 의무 · 동시 4명 상한 · 라이브니스 스탬프 · 팀 3인(구요한·이태극·형혜지) 지시도 큐 경유.
