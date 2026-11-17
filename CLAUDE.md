# CLAUDE.md — 네이버 블로그 자동화 에이전트 팀

이 저장소는 **네이버 블로그 포스팅을 자동 생성**하기 위한 8개 역할 기반 에이전트 팀의
운영 지침(플레이북)입니다. Claude는 아래 파이프라인 순서대로 각 에이전트 역할을 수행하여
하나의 완성된 블로그 원고(초안 + 이미지 프롬프트 + 발행용 패키지)를 만들어냅니다.

## 🏪 운영 대상

**고메365** — 네이버 스마트스토어. **양고기** 중심, 소고기·돼지고기 유통.
1단계로 경쟁이 낮은 **양고기 주제를 선점**하고, 전문성이 쌓인 뒤 소·돼지로 확장합니다.

- 상품·경험 정보: `guides/brand_assets.md` ← **먼저 채워야 함**
- 양고기 도메인 지식·키워드: `guides/lamb_domain.md`
- 식품 광고 규제: `guides/food_ad_compliance.md` ← **필수 준수**
- 자동화 범위(무엇이 수동인가): `workflow/automation_scope.md`

---

## 🎯 목적

- 주제만 입력하면 → **리서치 → SEO → 작성 → 검수 → 이미지 → 조립**까지 자동으로 진행
- 네이버 검색 로직(C-Rank / D.I.A.)에 맞는 **체류시간·정보성·독창성** 최적화
- 사람 손을 최소화한, 그러나 검수(중간 테스트)를 통과한 신뢰 가능한 원고 생산

## ⛔ 하지 않는 것

- **자동 발행 금지.** 네이버 블로그는 공식 발행 API가 없고, 브라우저 자동화 발행은
  운영정책 위반·계정 제재 위험이 있습니다. **발행 버튼은 사람이 누릅니다.**
- **효능·질병 표현 금지.** 축산물은 일반식품이며 판매 목적 글은 광고로 간주될 수 있습니다.
- **경험 없는 일반론 발행 금지.** 네이버는 LLM으로 문서를 평가합니다.
  `[사장님 입력]` 마커가 남은 원고는 QA에서 반려됩니다.

---

## 👥 에이전트 팀 (8명)

| # | 에이전트 | 파일 | 역할 요약 |
|---|----------|------|-----------|
| 1 | 기획·리서치 | `agents/01_planner_researcher.md` | 주제·타깃·키워드·경쟁글 분석, 원고 개요 설계 |
| 2 | SEO 전략 | `agents/02_seo_strategist.md` | 키워드 배치·제목·태그·메타 설계 |
| 3 | 작성(Writer) | `agents/03_writer.md` | 스타일 가이드에 맞춰 본문 초안 작성 |
| 4 | 편집·검수(QA) | `agents/04_editor_qa.md` | 중간 테스트(체크리스트) 실행, 통과/반려 판정 |
| 5 | 이미지 메이커 | `agents/05_image_maker.md` | 섹션별 이미지 프롬프트/썸네일 기획 및 생성 |
| 6 | 조립·발행 | `agents/06_assembler.md` | 모든 산출물을 발행용 패키지로 조립 |
| 7 | 영상 콘텐츠 | `agents/07_video_maker.md` | 숏폼/클립 기획·생성 (영상포함 글) |
| 8 | 검색 노출·추적 | `agents/08_analytics_tracker.md` | 발행 후 네이버 검색 노출·성과 추적, 개선 루프 |

---

## 🔄 워크플로우 (파이프라인)

```
[입력: 주제/키워드/톤]
      │
      ▼
① 기획·리서치 ──► outline.md (개요/타깃/핵심키워드/근거자료)
      │
      ▼
② SEO 전략 ──────► seo_plan.md (제목안/키워드맵/태그/메타)
      │
      ▼
③ 작성(Writer) ──► draft.md (스타일 가이드 준수 본문)
      │
      ▼
④ 편집·검수(QA) ─► qa_report.md (중간 테스트 결과)
      │
      ├─ ❌ 반려 → ③ 작성으로 되돌림(수정 지시 포함)
      │
      ▼ ✅ 통과
⑤ 이미지 메이커 ─► images/ + image_prompts.md
⑦ 영상 콘텐츠 ───► videos/ + video_plan.md  (영상포함 글만)
      │
      ▼
⑥ 조립·발행 ────► output/final_post.md (발행용 완성본)
      │
      ▼ (발행 후 D+3 / D+7)
⑧ 검색 노출·추적 ► tracking_report.md ──피드백──► ① 기획 (개선 루프)
```

자세한 내용은 `workflow/pipeline.md` 참고.

## 📅 스케줄 관리 (주 3일 발행)

- **발행 리듬**: 월/수/금 주 3회 — `workflow/content_calendar.md`
- **콘텐츠 보드**: Google Sheets/Notion 갤러리로 상태 관리 — `templates/content_board.csv`
- **스케줄 운영·예약발행·리마인더**: `guides/scheduling_guide.md`
- 콘텐츠 재고 **버퍼 3편** 유지, 발행 3일 전 기획 시작

---

## 📚 가이드 문서

- **스타일 가이드**: `guides/style_guide.md` — 문체, 문단, 톤, 금지 표현
- **SEO 가이드**: `guides/seo_guide.md` — 네이버 검색 최적화 규칙
- **QA 체크리스트(중간 테스트)**: `guides/qa_checklist.md` — 통과 기준
- **템플릿**: `templates/blog_post_template.md` — 원고 골격

### 고메365 전용 (작성 전 반드시 확인)
- **브랜드·상품 정보**: `guides/brand_assets.md` — 사장님 입력란. 비면 일반론만 나옴
- **양고기 도메인**: `guides/lamb_domain.md` — 램/머튼 구분, 부위, 키워드 전략
- **식품 광고 규제**: `guides/food_ad_compliance.md` — 금지 표현 치환 사전
- **자동화 범위**: `workflow/automation_scope.md` — 자동 vs 수동 경계

---

## 🚀 사용법 (Claude에게 지시하는 방법)

한 번에 전체 실행:

```
주제: "제주도 3박4일 가족여행 코스"
톤: 친근한 정보성
타깃: 30~40대 부모
→ 위 주제로 네이버 블로그 자동화 파이프라인 전체를 실행해줘.
```

단계별 실행도 가능:

```
① 기획·리서치 에이전트만 실행해줘 (주제: ...)
```

Claude는 각 단계 산출물을 `output/<주제-slug>/` 폴더에 저장합니다.

---

## 📁 산출물 폴더 규칙

```
output/
  ├── <주제-slug>/
  │     ├── 1_outline.md
  │     ├── 2_seo_plan.md
  │     ├── 3_draft.md
  │     ├── 4_qa_report.md
  │     ├── 5_image_prompts.md
  │     ├── 7_video_plan.md      # 영상포함 글
  │     ├── 8_tracking_report.md # 발행 후 추적
  │     ├── images/
  │     ├── videos/
  │     └── final_post.md
  └── _weekly/
        └── <주차>_report.md      # 주간 종합 성과
```

---

## ⚙️ 핵심 원칙

1. **각 에이전트는 자기 역할의 산출물만 책임진다** (역할 분리)
2. **QA를 통과하지 못한 원고는 발행 단계로 넘기지 않는다** (품질 게이트)
3. **가이드 문서가 곧 규칙이다** — 판단이 애매하면 가이드를 우선한다
4. **네이버 정책 준수** — 저작권 침해 이미지/과장·허위 광고 표현 금지
5. **출처 표기** — 통계·인용은 반드시 근거 링크 명시

---

## ➕ 추가 구성 요소 (확장)

- `guides/prohibited_expressions.md` — 네이버 광고/저품질 회피용 금지 표현 목록
- `templates/keyword_map.md` — 키워드 맵 작성 양식
- `workflow/example_run.md` — 예시 실행 결과 (샘플)
- `workflow/content_calendar.md` — 주 3일 발행 캘린더
- `guides/scheduling_guide.md` — 스케줄·콘텐츠 보드·예약발행 운영
- `templates/content_board.csv` — Google Sheets 콘텐츠 보드 양식
