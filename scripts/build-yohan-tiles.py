#!/usr/bin/env python3
"""build-yohan-tiles.py — 요한 초상 → 포컬 크롭 타일 굽기.

왜 미리 굽는가: OmniControl 데몬(bridge/)은 Python 표준 라이브러리 전용이라
런타임에 이미지를 크롭할 수 없다. 데몬은 바이트만 서빙하고, 크롭은 빌드 타임인
여기서 끝낸다. 크롭 사각형은 ops/yohan-registry.json 이 정본.

산출: assets/yohans/tiles/{handle}-{80,240}.png
  80  = 오버레이 카드 40pt 타일의 2x (레티나)
  240 = 대시보드 120pt 타일의 2x

사용: python3 scripts/build-yohan-tiles.py [--check]
  --check  파일을 쓰지 않고 누락/구식만 보고 (CI·런북 검증용)
"""
import json
import pathlib
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow 필요: pip3 install Pillow  (빌드 타임 전용 — 데몬은 이걸 안 쓴다)")

ROOT = pathlib.Path(__file__).resolve().parent.parent
REG = ROOT / "ops" / "yohan-registry.json"
OUT = ROOT / "assets" / "yohans" / "tiles"
SIZES = (80, 240)


def main() -> int:
    check = "--check" in sys.argv
    reg = json.loads(REG.read_text(encoding="utf-8"))["yohans"]
    OUT.mkdir(parents=True, exist_ok=True)
    missing, written = [], 0

    for handle, m in sorted(reg.items()):
        src = ROOT / m["source"]
        if not src.exists():
            missing.append(f"원본 없음: {m['source']}")
            continue
        im = Image.open(src).convert("RGB")
        w, h = im.size
        x, y, cw, ch = m["crop"]
        box = (int(x * w), int(y * h), int((x + cw) * w), int((y + ch) * h))
        for size in SIZES:
            dst = OUT / f"{handle}-{size}.png"
            if check:
                if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
                    missing.append(f"타일 구식/누락: {dst.relative_to(ROOT)}")
                continue
            im.resize((size, size), Image.LANCZOS, box=box).save(dst, optimize=True)
            written += 1

    if missing:
        print("\n".join(missing), file=sys.stderr)
        return 1
    print(f"{'검증 통과' if check else f'{written}장 생성'} → {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
