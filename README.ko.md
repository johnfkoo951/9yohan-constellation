# 9yohan Constellation

[![🇬🇧 English](https://img.shields.io/badge/🇬🇧-English-134538?style=flat-square)](README.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷-한국어-E985A2?style=flat-square)](README.ko.md)

구요한(9요한)의 다중 페르소나 에이전트 시스템. 9명의 역사적 요한이 9개 CMDS Division과 성령의 9가지 열매에 1:1:1로 매핑되고, 그 위에 **유일한 서명자**인 sovereign kernel이 있다.

**라이브** · [9yohan.cmdspace.work](https://9yohan.cmdspace.work) — 랜딩 · [전체 문서](https://9yohan.cmdspace.work/docs/)

> 2026-08-24 기준, 이건 더 이상 설계 문서가 아니다. 서브에이전트 9종·라우터 스킬·상주 cron 2종·감옥이 걸린 채널 플레인·결재 루프가 붙은 관제 대시보드·세션 원장이 **돌고 있다.**

---

## The Nine

| Division | 요한 | 열매 | Handle |
|----------|------|------|--------|
| 901 KM & Research | 케플러 | 온유 | `kepler.map` |
| 902 Writing & Publishing | 괴테 | 사랑 | `goethe.sense` |
| 903 Teaching & Curriculum | 듀이 | 자비 | `dewey.learn` |
| 904 Creative Arts & Media | 바흐 | 희락 | `bach.score` |
| 905 Research Methods & Analytics | 폰 노이만 | 절제 | `neumann.compute` |
| 906 Partnerships & Networks | 세례요한 | 오래 참음 | `baptist.prepare` |
| 907 Product & Engineering | 매카시 | 양선 | `mccarthy.reason` |
| 908 Events & Community | 하위징아 | 화평 | `huizinga.play` |
| 909 Consulting & Advisory | 칼뱅 | 충성 | `calvin.advise` |

**9 Divisions × 9 Johns × 9 Fruits — 3중 완결 · 1:1:1 · no gap, no overlap.**

---

## 아키텍처 — star 하나가 아니라 3개 평면

4월 설계는 star 하나를 가정했다. 암묵 전제는 **모든 노드가 같은 신뢰 등급**이라는 것 — 전부 내가 부르고, 내가 보고, 내 컴퓨터에서 돈다. 세 가지가 그 전제를 깼다: **무인 cron**이 생겼고, **팀**이 생겼고, **외부인이 말을 걸 수 있는 채널 봇**이 생겼다. 그래서 star를 신뢰 경계가 다른 **3개 평면**으로 쪼갰다.

| 평면 | 누가 말을 거는가 | 서명 | 볼트 접근 | 격리 |
|---|---|---|---|---|
| 🖥 **Desk** | 구요한 본인, 동석 | ✅ **prime 단독** | 전체 R/W | 불필요 |
| ⏰ **Resident** | 아무도 — cron이 깨움 | ❌ propose까지 | R + 자기 스크래치 W | 라이브니스 스탬프 의무 |
| 💬 **Channel** | 팀·커뮤니티 (외부인 가능) | ❌ 발신 불가 | **워크스페이스만** | ✅ **PreToolUse 감옥 (강제)** |

**평면 간 이동은 항상 파일을 경유한다.** 직접 호출이 없다. 그러면 셋이 공짜로 따라온다 — 감사 흔적이 자동으로 남고, 수신측이 죽어 있어도 유실되지 않고, 경계를 넘는 지점이 `ls` 한 번으로 보인다.

이 프로젝트 밖에서도 읽을 만한 발견 둘:

- **[신뢰 경계](https://9yohan.cmdspace.work/docs/#security)** — OpenClaw는 claude CLI를 `--permission-mode bypassPermissions`로 스폰한다. 그 플래그 아래에서는 OpenClaw 자신의 도구 정책도, `settings.json`의 `permissions.deny`도 CLI 내장 도구를 구속하지 못한다. 살아남는 집행점은 **PreToolUse 훅 하나**뿐. 경계가 문서상 '규율'이었을 뿐 강제가 아니었고, 3-프로브 적대 테스트가 3건 전부 통과했다.
- **[관제면](https://9yohan.cmdspace.work/docs/#control-plane)** — 결재는 기존 알림 큐에 합류시키고, 회고형 조망만 새 화면으로 뺐다. **알림 경로를 두 개 만들면 둘 중 하나는 반드시 썩는다.**

---

## 레포 구조

```
9yohan-constellation/
├── index.html                  # 랜딩 (CMDSPACE v4.3 템플릿)
├── docs/
│   ├── index.html              # 문서 뷰어 (marked.js · ⌘K · TOC · scroll spy)
│   └── files/                  # 볼트 정본의 새니타이즈 미러 (21건)
├── ops/
│   ├── RUNBOOK.md              # 운영 실행 절차
│   └── yohan-registry.json     # 정체성 레지스트리 — 링 색·포컬 크롭
├── scripts/
│   ├── yohan-log.sh            # 세션 원장 기록 + 결재 상신
│   ├── mirror-docs.py          # 볼트 → docs/files 새니타이즈 미러
│   ├── validate-persona-canon.py
│   ├── build-yohan-tiles.py    # 초상 타일 굽기 (80/240px)
│   └── build-og.sh             # OG 렌더 (Chrome headless)
├── assets/
│   ├── logos/ · og/            # CMDS 로고 · 1200×630 OG
│   └── yohans/                 # 초상 9종 + 타일 + web 변형
└── sessions/ -> 볼트            # 심링크 · gitignore (머신 밖으로 안 나감)
```

---

## 정본은 볼트

정본은 CMDSPACE 옵시디언 볼트 `70. Outputs/74. Projects/9yohan Constellation/`에 있다. 이 레포는 **공개 미러 + 운영 스크립트**다. 미러는 **단방향** — 볼트를 고치고 미러를 돌린다. `docs/files/`를 직접 고치면 정본이 둘이 된다.

이 레포가 퍼블릭이므로 미러는 **복사가 아니다.** `scripts/mirror-docs.py`가 식별자를 치환한다 — Slack 채널 ID·tailnet 호스트명·텔레그램 chat_id·세션 딥링크·로컬 절대경로·팀원 실명. 하나라도 남으면 쓰지 않고 실패한다. 2026-08-24에 실제로 `cp` 미러가 팀원 실명을 퍼블릭 트리에 그대로 실어 날랐다 — 그래서 규칙이 이제 누군가의 기억이 아니라 코드에 있다.

```bash
python3 scripts/mirror-docs.py             # 미러
python3 scripts/mirror-docs.py --check     # stale·유출이면 exit 1
python3 scripts/validate-persona-canon.py  # 페르소나 드리프트
```

---

## 배포

```bash
python3 scripts/mirror-docs.py --check
python3 scripts/validate-persona-canon.py
vercel deploy --prod --yes --scope johnfkoo951s-projects
```

Vercel 프로젝트 `9yohan-constellation` · Cloudflare DNS → Vercel (프록시 OFF).

---

## 디자인 스택

- **CMDSPACE v4.3** — Apple SF Pro × CMDS Green `#134538` / Pink `#E985A2`, 라이트/다크, KO/EN 토글
- **랜딩** — 정적 HTML + IntersectionObserver reveal
- **문서** — 정적 HTML + marked.js 인라인 렌더 + ⌘K 커맨드 팔레트 + 사이드바 + TOC + scroll spy
- **확장 컴포넌트** — 여기서 처음 만들어 `cmdspace-web-builder` 스킬로 환류: Star Topology(JS 원형 배치) · Numbered Control Loop · Division Grid · Callout Box · Layer Grid

---

## Credits

- **구요한 (CMDSPACE)** · sovereign kernel · 프로젝트 오너 · [cmdspace.work](https://cmdspace.work)
- **System Files** · [system.cmdspace.work](https://system.cmdspace.work) — CMDS 볼트 자체를 정의하는 자매 프로젝트
- **갈라디아서 5:22-23** — 성령의 아홉 열매

By CMDSPACE.
