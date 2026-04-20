# 9yohan Constellation

구요한(9요한)의 다중 페르소나 에이전트 시스템 — 9명의 역사적 요한이 9개 CMDS Division과 성령의 9가지 열매에 1:1:1로 매핑된 Sovereign Kernel 아키텍처.

## Live

- **Landing**: https://9yohan.cmdspace.work
- **Full Docs**: https://9yohan.cmdspace.work/docs/
- **Vercel Project**: `9yohan-constellation` (scope: `johnfkoo951s-projects`)

## The Nine

| Division | John | Fruit | Handle |
|----------|------|-------|--------|
| 901 KM & Research | 케플러 (Kepler) | 온유 | `kepler.map` |
| 902 Writing & Publishing | 괴테 (Goethe) | 사랑 | `goethe.sense` |
| 903 Teaching & Curriculum | 듀이 (Dewey) | 자비 | `dewey.learn` |
| 904 Creative Arts & Media | 바흐 (Bach) | 희락 | `bach.score` |
| 905 Research Methods & Analytics | 폰 노이만 (von Neumann) | 절제 | `neumann.compute` |
| 906 Partnerships & Networks | 세례요한 (John the Baptist) | 오래 참음 | `baptist.prepare` |
| 907 Product & Engineering | 매카시 (McCarthy) | 양선 | `mccarthy.reason` |
| 908 Events & Community | 하위징아 (Huizinga) | 화평 | `huizinga.play` |
| 909 Consulting & Advisory | 칼뱅 (Calvin) | 충성 | `calvin.advise` |

**9 Divisions × 9 Johns × 9 Fruits — triple closure · 1:1:1 mapping · no gap, no overlap.**

## Project Structure

```
9yohan-constellation/
├── index.html              # Landing (v4.3 landing template)
├── vercel.json             # Vercel config
├── assets/
│   ├── logos/              # CMDS round/typo logos
│   └── og/                 # 1200×630 OG image
├── docs/
│   ├── index.html          # Full docs (editorial-docs template)
│   └── files/              # Vault-sourced markdown docs
│       ├── canonical.md    # Layer 01 — Identity SSOT
│       ├── constellation.md # Layer 02 — Agent definitions
│       ├── architecture.md # Layer 02 — Harness spec
│       ├── workflows.md    # Layer 03 — Patterns
│       ├── playbooks.md    # Layer 03 — 10 scenarios
│       ├── schemas.md      # Layer 03 — Message schemas
│       └── yohans.md       # Layer 04 — Research archive
└── scripts/
    └── build-og.sh         # Chrome headless OG renderer
```

## Design Stack

- **v4.3 CMDSPACE standard**: Apple SF Pro × CMDS Green (#134538) / Pink (#E985A2)
- **Landing**: Static HTML + IntersectionObserver reveal + light/dark + KO/EN toggle
- **Docs**: Static HTML + marked.js (inline markdown render) + ⌘K command palette + sidebar nav + TOC + scroll spy
- **Extended components** (new in 9yohan): Star Topology diagram (JS circular layout), Numbered Control Loop (5×2 grid), Division Grid, Callout Box, Layer Grid — documented in the `cmdspace-web-builder` skill at `references/LANDING-COMPONENTS.md`

## Deploy

```bash
# One-time: OG image render
./scripts/build-og.sh

# Deploy (prod)
vercel deploy --prod --yes --scope johnfkoo951s-projects
```

## Content Origin

The `docs/files/` markdown documents are sourced from the CMDSPACE Obsidian vault at `00. Inbox/03. AI Agent/03-1. Claude Code (MBP)/2026-04-19-9yohan-orchestration/`. They are the **actual working documents** used to design and operate the system — not a web-specific rewrite.

## Credits

- **9요한** (Yohan Koo / 구요한) · Sovereign Kernel · project owner
- **CMDSPACE** · https://litt.ly/cmds
- **System Files** · https://system.cmdspace.work (sibling project defining the CMDS vault itself)

