#!/bin/bash
# yohan-log.sh — 요한 세션 원장 기록기 (9yohan ops)
# 사용: yohan-log.sh <handle> <task_id> <status:done|failed|partial> "<summary 한 문장>" [output_path] [workflow]
# 원장 정본: 볼트 agents/_sessions/ledger.jsonl (마더십 git+NAS 일일 백업 커버)
# DEV 레포의 sessions/ 는 이 폴더로의 심링크 (gitignore — 퍼블릭 원격에 미전송)
set -euo pipefail
S="${CMDS_VAULT:-$HOME/Local Obsidian_MBP/CMDSPACE_Local_MBP}/00. Inbox/03. AI Agent/agents/_sessions"
HANDLE="${1:?handle}"; TASK="${2:?task_id}"; STATUS="${3:?status}"; SUMMARY="${4:?summary}"
OUTPUT="${5:-}"; WORKFLOW="${6:-adhoc}"
TS="$(date '+%Y-%m-%dT%H:%M:%S%z')"
mkdir -p "$S/cards"
python3 - "$S/ledger.jsonl" "$TS" "$HANDLE" "$TASK" "$STATUS" "$SUMMARY" "$OUTPUT" "$WORKFLOW" << 'PY'
import json, sys
path, ts, handle, task, status, summary, output, workflow = sys.argv[1:9]
with open(path, "a", encoding="utf-8") as f:
    f.write(json.dumps({"ts": ts, "handle": handle, "task_id": task, "status": status,
                        "summary": summary, "output": output or None, "workflow": workflow},
                       ensure_ascii=False) + "\n")
PY
# 세션 카드 (사람이 읽는 후속 작업용 — 요한별 최근 맥락)
C="$S/cards/${TASK}.md"
{
  echo "# ${TASK}"
  echo ""
  echo "- handle: ${HANDLE} · status: ${STATUS} · ${TS} · workflow: ${WORKFLOW}"
  echo "- summary: ${SUMMARY}"
  [ -n "$OUTPUT" ] && echo "- output: ${OUTPUT}"
  echo "- 후속 참고: 요한 스크래치 MEMORY.md 와 이 카드의 output 경로가 재개 지점"
} > "$C"
echo "logged: ${HANDLE} ${TASK} ${STATUS} → ledger.jsonl + cards/${TASK}.md"
