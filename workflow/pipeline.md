# 파이프라인 운영 가이드 (Pipeline)

6개 에이전트를 순서대로 실행하는 전체 흐름과 상태 관리.

## 실행 순서

```
① 기획·리서치  →  1_outline.md
② SEO 전략     →  2_seo_plan.md
③ 작성         →  3_draft.md
④ 편집·검수(QA) →  4_qa_report.md   ─┐ FAIL이면 ③으로 되돌림
⑤ 이미지 메이커 →  5_image_prompts.md + images/
⑦ 영상 콘텐츠   →  7_video_plan.md + videos/   (영상포함 글만)
⑥ 조립·발행    →  final_post.md
⑧ 검색 노출·추적 → 8_tracking_report.md   (발행 후 D+3/D+7) → ①로 피드백
```

> ⑦ 영상은 ⑤ 이미지와 병렬로 진행 가능하며, 둘 다 ⑥ 조립의 입력이 된다.
> ⑧ 추적은 발행 후 실행되어 성과를 ①(기획)의 다음 주제 선정에 피드백한다(개선 루프).

## 스케줄 연동
- 발행 리듬·리드타임은 `workflow/content_calendar.md` (주 3일)
- 진행 상태는 Google Sheets/Notion 콘텐츠 보드(`templates/content_board.csv`)의 `Status`로 관리
- 예약 발행·리마인더는 `guides/scheduling_guide.md`

## 상태 게이트
- **④ QA는 품질 게이트다.** PASS 전에는 ⑤/⑥로 넘어가지 않는다.
- FAIL → ③ 재작업 → 다시 ④. **최대 3회** 반복 후에도 FAIL이면 사람에게 보고.

## 산출물 폴더
```
output/<주제-slug>/
  ├── 1_outline.md
  ├── 2_seo_plan.md
  ├── 3_draft.md
  ├── 4_qa_report.md
  ├── 5_image_prompts.md
  ├── images/
  └── final_post.md
```
- `<주제-slug>`: 주제를 영문 소문자-하이픈으로 (예: `jeju-family-trip`)

## 실행 방식

### 전체 자동 실행
사용자가 주제를 주면 Claude가 ①→⑥을 순차 수행하고, 각 단계 산출물을 저장한다.
QA FAIL 시 자동으로 ③으로 되돌려 재작업한다.

### 단계별 실행
특정 에이전트만 실행 가능. 이전 단계 산출물이 있어야 한다.

## 에이전트 간 계약(Contract)
- 각 에이전트는 **이전 산출물을 입력으로 받고, 정해진 출력 파일만 생성**한다.
- 다른 에이전트의 산출물을 임의로 수정하지 않는다 (QA의 교정 반영 제외).
- 판단이 애매하면 `guides/`의 규칙을 우선한다.

## 이미지 생성 도구
- MCP `generate_image` 사용 가능 시 Agent 5가 실제 이미지를 생성.
- 불가 시 프롬프트만 산출 → 사람이 수동 생성.

## 최종 인수인계
- `final_post.md`를 그대로 네이버 블로그 에디터에 붙여넣고,
  이미지를 순서대로 업로드 → 발행 전 체크리스트 확인 → 발행.
