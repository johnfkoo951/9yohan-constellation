#!/bin/bash
# yohan-log.sh — 요한 세션 원장 기록기 (9yohan ops)
# 사용: yohan-log.sh <handle> <task_id> <status:done|failed|partial|propose> "<summary 한 문장>" [output_path] [workflow]
#
# status=propose 는 "구요한 결재 대기" — 원장·카드에 더해 OmniControl 데몬에
# yohan_propose 이벤트를 상신한다 (조용한 오버레이 카드 + 관제 대시보드 배지).
# 데몬이 없거나 꺼져 있어도 원장 기록은 항상 성공한다 (전송은 best-effort).
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
# 결재 상신 — 데몬에 조용한 알림 (실패해도 원장은 이미 남았으므로 무해)
if [ "$STATUS" = "propose" ]; then
  CONFIG="$HOME/.config/cmux-voice"
  if [ -f "$CONFIG/enabled" ]; then
    PORT=$(jq -r '.port // 8765' "$CONFIG/config.json" 2>/dev/null || echo 8765)
    TOKEN=$(jq -r '.auth_token // ""' "$CONFIG/config.json" 2>/dev/null || echo "")
    PAYLOAD=$(python3 -c 'import json,sys; print(json.dumps(dict(zip(
      ["handle","task_id","summary","output","workflow"], sys.argv[1:6]))))' \
      "$HANDLE" "$TASK" "$SUMMARY" "$OUTPUT" "$WORKFLOW")
    curl -sS -m 3 -X POST "http://127.0.0.1:${PORT}/hook/yohan" \
      -H "Content-Type: application/json" \
      ${TOKEN:+-H "X-CMUX-Token: $TOKEN"} \
      -d "$PAYLOAD" >/dev/null 2>&1 &
  fi
fi

echo "logged: ${HANDLE} ${TASK} ${STATUS} → ledger.jsonl + cards/${TASK}.md${EXTRA:-}"
