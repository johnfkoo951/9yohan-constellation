# 9yohan Constellation

[![🇬🇧 English](https://img.shields.io/badge/🇬🇧-English-134538?style=flat-square)](README.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷-한국어-E985A2?style=flat-square)](README.ko.md)

A running multi-persona agent system. Nine historical Johns map 1:1:1 onto nine CMDS Divisions and the nine Fruits of the Spirit, under a sovereign kernel that is the only signer.

**Live** · [9yohan.cmdspace.work](https://9yohan.cmdspace.work) — landing · [full docs](https://9yohan.cmdspace.work/docs/)

> As of 2026-08-24 this is no longer a design document. Nine subagents, a router skill, two resident cron jobs, a channel plane under an enforced jail, a control dashboard with an approval loop, and a session ledger are all running.

---

## The Nine

| Division | John | Fruit | Handle |
|----------|------|-------|--------|
| 901 KM & Research | Kepler | Gentleness | `kepler.map` |
| 902 Writing & Publishing | Goethe | Love | `goethe.sense` |
| 903 Teaching & Curriculum | Dewey | Kindness | `dewey.learn` |
| 904 Creative Arts & Media | Bach | Joy | `bach.score` |
| 905 Research Methods & Analytics | von Neumann | Self-control | `neumann.compute` |
| 906 Partnerships & Networks | John the Baptist | Patience | `baptist.prepare` |
| 907 Product & Engineering | McCarthy | Goodness | `mccarthy.reason` |
| 908 Events & Community | Huizinga | Peace | `huizinga.play` |
| 909 Consulting & Advisory | Calvin | Faithfulness | `calvin.advise` |

**9 Divisions × 9 Johns × 9 Fruits — triple closure · 1:1:1 · no gap, no overlap.**

---

## Architecture · three planes, not one star

The original April design assumed a single star topology: every agent equally trusted, all summoned by one person, all on one machine. Three things broke that assumption — unattended cron jobs, a team, and a channel bot outsiders can talk to. So the star was split into three planes with different trust boundaries.

| Plane | Who speaks to it | Can sign? | Vault access | Isolation |
|---|---|---|---|---|
| 🖥 **Desk** | the owner, present | ✅ **prime alone signs** | full R/W | not needed |
| ⏰ **Resident** | nobody — cron wakes it | ❌ propose only | read + own scratch | liveness stamp required |
| 💬 **Channel** | team & community (outsiders possible) | ❌ cannot send | **workspace only** | ✅ **PreToolUse jail (enforced)** |

**Crossing a plane always goes through a file.** No direct calls. That buys three things for free: an audit trail, delivery that survives a dead receiver, and a boundary you can see with `ls`.

Two findings worth reading even outside this project:

- **[Trust boundary](https://9yohan.cmdspace.work/docs/#security)** — OpenClaw spawns the Claude CLI with `--permission-mode bypassPermissions`. Under that flag neither OpenClaw's own tool policy nor `settings.json`'s `permissions.deny` binds the CLI's built-in tools. A PreToolUse hook is the only surviving enforcement point. The boundary had been documented discipline, not enforcement — an adversarial three-probe test passed all three probes.
- **[Control plane](https://9yohan.cmdspace.work/docs/#control-plane)** — approvals join the existing notification queue; only the retrospective board became a new screen. Build two notification paths and one of them rots.

---

## Repository layout

```
9yohan-constellation/
├── index.html                  # Landing (CMDSPACE v4.3 template)
├── docs/
│   ├── index.html              # Docs viewer (marked.js · ⌘K palette · TOC · scroll spy)
│   └── files/                  # Sanitized mirror of the vault canon (21 files)
├── ops/
│   ├── RUNBOOK.md              # Operating procedures
│   └── yohan-registry.json     # Identity registry — ring colors + focal crops
├── scripts/
│   ├── yohan-log.sh            # Session ledger writer + approval dispatch
│   ├── mirror-docs.py          # Vault → docs/files sanitized mirror
│   ├── validate-persona-canon.py
│   ├── build-yohan-tiles.py    # Pre-bakes portrait tiles (80/240px)
│   └── build-og.sh             # Chrome headless OG renderer
├── assets/
│   ├── logos/ · og/            # CMDS logos · 1200×630 OG image
│   └── yohans/                 # Nine portraits + tiles + web variants
└── sessions/ -> vault          # Symlink · gitignored (never leaves the machine)
```

---

## Source of truth

The canon lives in the CMDSPACE Obsidian vault at `70. Outputs/74. Projects/9yohan Constellation/`. This repository is a **public mirror plus the operational scripts**. The mirror is one-directional — edit the vault, then run the mirror. Editing `docs/files/` directly creates a second canon.

Because this repo is public, mirroring is **not** a copy. `scripts/mirror-docs.py` substitutes identifiers — Slack channel IDs, tailnet hostnames, Telegram chat IDs, session deeplinks, local absolute paths, teammate names — and refuses to write if any survive. On 2026-08-24 a plain `cp` mirror carried teammate names straight into the public tree; that is why the rule now lives in code rather than in someone's memory.

```bash
python3 scripts/mirror-docs.py             # mirror
python3 scripts/mirror-docs.py --check     # exit 1 if stale or leaking
python3 scripts/validate-persona-canon.py  # persona drift
```

---

## Deploy

```bash
python3 scripts/mirror-docs.py --check
python3 scripts/validate-persona-canon.py
vercel deploy --prod --yes --scope johnfkoo951s-projects
```

Vercel project `9yohan-constellation` · Cloudflare DNS → Vercel (proxy off).

---

## Design stack

- **CMDSPACE v4.3** — Apple SF Pro × CMDS Green `#134538` / Pink `#E985A2`, light/dark, KO/EN toggle
- **Landing** — static HTML + IntersectionObserver reveal
- **Docs** — static HTML + marked.js inline render + ⌘K command palette + sidebar nav + TOC + scroll spy
- **Extended components** first built here and folded back into the `cmdspace-web-builder` skill: Star Topology (JS circular layout), Numbered Control Loop, Division Grid, Callout Box, Layer Grid

---

## Credits

- **Yohan Koo (CMDSPACE)** · sovereign kernel · project owner · [cmdspace.work](https://cmdspace.work)
- **System Files** · [system.cmdspace.work](https://system.cmdspace.work) — sibling project defining the CMDS vault itself
- **Galatians 5:22-23** — the nine fruits

By CMDSPACE.
