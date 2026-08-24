#!/usr/bin/env python3
"""볼트 정본 → 레포 docs/files/ 새니타이즈 미러 (9yohan).

이 레포는 퍼블릭이다. 설계 논리는 공개해도 안전하지만 **식별자는 아니다** —
Slack 채널 ID·tailnet 호스트명·텔레그램 chat_id·세션 딥링크·로컬 절대경로·팀원 실명.
손으로 `cp` 하면 언젠가 한 번은 빠뜨린다(실제로 2026-08-24 미러에서 architecture.md가
팀원 실명을 그대로 실어 나갔다). 그래서 **모든** 미러가 이 한 경로를 지난다.

사용:
    python3 scripts/mirror-docs.py            # 전체 미러
    python3 scripts/mirror-docs.py --check    # 최신성 + 유출 검사만 (exit 1 = 실패)

정본은 볼트. 단방향(볼트 → 레포)이며 역방향은 없다.
페르소나 카드의 내용 일치 검증은 `validate-persona-canon.py`가 따로 본다.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

VAULT = Path(
    os.environ.get("CMDS_VAULT", Path.home() / "Local Obsidian_MBP/CMDSPACE_Local_MBP")
) / "70. Outputs/74. Projects/9yohan Constellation"
REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "docs" / "files"

_PERSONAS = [
    "00-9yohan-prime", "901-kepler-map", "902-goethe-sense", "903-dewey-learn",
    "904-bach-score", "905-neumann-compute", "906-baptist-prepare",
    "907-mccarthy-reason", "908-huizinga-play", "909-calvin-advise",
]

# 볼트 정본 경로 → (공개 파일명, 미러 배너 삽입 여부)
# 배너는 운영 문서에만 — 식별자가 치환됐다는 사실을 독자가 알아야 하는 문서들.
MIRROR: dict[str, tuple[str, bool]] = {
    "README.md": ("README.md", False),
    "1. Identity/canonical.md": ("canonical.md", False),
    "1. Identity/personas/README.md": ("personas/README.md", False),
    "2. Implementation/architecture.md": ("architecture.md", False),
    "2. Implementation/constellation.md": ("constellation.md", False),
    "3. Operations/workflows.md": ("workflows.md", False),
    "3. Operations/playbooks.md": ("playbooks.md", False),
    "3. Operations/schemas.md": ("schemas.md", False),
    "3. Operations/9YOHAN-SECURITY.md": ("security.md", True),
    "3. Operations/9YOHAN-CONTROL-PLANE.md": ("control-plane.md", True),
    "4. Research/요한쓰.md": ("yohans.md", False),
    **{f"1. Identity/personas/{p}.md": (f"personas/{p}.md", False) for p in _PERSONAS},
}

# (정규식, 치환) — 순서가 중요하다. 긴 패턴부터.
SANITIZE: list[tuple[str, str]] = [
    (r'(?m)^session-link:.*\n', ''),                       # 세션 딥링크 (프론트매터 1행)
    (r'[A-Za-z0-9-]+\.tail[0-9a-z]+\.ts\.net', '<tailnet-host>'),
    (r'\bC0[A-Z0-9]{8,}\b', '<채널ID>'),                    # Slack 채널 ID
    (r'telegram:\d{6,}', 'telegram:<chat_id>'),
    (r'/Users/[A-Za-z0-9._-]+/', '~/'),                     # 로컬 홈 절대경로
    # 팀원 실명 → 역할 표기 (구요한은 프로젝트 오너로 공개 표기이므로 유지)
    (r'구요한·이태극·형혜지', '구요한 외 팀 2인'),
    (r'\s*\(Tagg\)', ''),
    (r'이태극', '팀원 A'),
    (r'형혜지', '팀원 B'),
]

# 미러 결과에 남아 있으면 안 되는 것 (사후 검증 — 규칙이 놓친 변형을 잡는다)
LEAK_PATTERNS: list[tuple[str, str]] = [
    (r'\.ts\.net', 'tailnet 호스트명'),
    (r'\bC0[A-Z0-9]{8,}\b', 'Slack 채널 ID'),
    (r'telegram:\d{6,}', '텔레그램 chat_id'),
    (r'/Users/', '로컬 절대경로'),
    (r'session-link:', '세션 딥링크'),
    (r'이태극|형혜지', '팀원 실명'),
]

BANNER = (
    "> [!info] 이 문서는 볼트 정본의 **공개 미러**입니다\n"
    "> 정본은 CMDS 볼트 `70. Outputs/74. Projects/9yohan Constellation/{src}`.\n"
    "> 공개본에서는 식별자(채널 ID · 호스트명 · chat_id · 로컬 경로 · 팀원 실명)가 치환되었습니다.\n"
    "> 편집은 볼트에서 하고 `scripts/mirror-docs.py`로 다시 미러하세요.\n\n"
)


def sanitize(text: str, src_rel: str, banner: bool) -> str:
    for pattern, repl in SANITIZE:
        text = re.sub(pattern, repl, text)
    if banner and text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            cut = end + len("\n---\n")
            text = text[:cut] + "\n" + BANNER.format(src=src_rel) + text[cut:].lstrip("\n")
    return text


def check_leaks(text: str, label: str) -> list[str]:
    out = []
    for pattern, desc in LEAK_PATTERNS:
        m = re.search(pattern, text)
        if m:
            out.append(f"{label}: {desc} 잔존 ({m.group(0)!r})")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="쓰지 않고 최신성·유출만 검사")
    args = ap.parse_args()

    problems: list[str] = []
    stale: list[str] = []
    written = 0

    for rel, (out_name, banner) in MIRROR.items():
        src = VAULT / rel
        dst = OUT / out_name
        if not src.exists():
            problems.append(f"정본 없음: {rel}")
            continue

        rendered = sanitize(src.read_text(encoding="utf-8"), rel, banner)
        problems += check_leaks(rendered, out_name)

        if args.check:
            if not dst.exists():
                stale.append(f"{out_name}: 미러 없음")
            elif dst.read_text(encoding="utf-8") != rendered:
                stale.append(f"{out_name}: 정본과 불일치 (재미러 필요)")
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists() or dst.read_text(encoding="utf-8") != rendered:
                dst.write_text(rendered, encoding="utf-8")
                print(f"  updated  docs/files/{out_name}")
                written += 1

    for line in problems + stale:
        print(f"FAIL: {line}", file=sys.stderr)
    if problems or stale:
        return 1

    if args.check:
        print(f"PASS: 미러 {len(MIRROR)}건 최신 · 식별자 유출 없음")
    else:
        print(f"PASS: 미러 {len(MIRROR)}건 (갱신 {written}건) · 식별자 유출 없음")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
