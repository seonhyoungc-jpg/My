# 네이버 블로그 자동화 에이전트 팀 🤖✍️

주제만 입력하면 **리서치 → SEO → 작성 → 검수 → 이미지 → 조립**까지 자동으로 진행하여
네이버 블로그 발행용 원고를 만들어내는, 6개 역할 기반 에이전트 시스템입니다.

## 구성

```
.
├── CLAUDE.md                 # 🧭 운영 지침(메인) — 여기서 시작
├── README.md                 # 이 문서
├── agents/                   # 👥 6개 에이전트 역할 정의
│   ├── 01_planner_researcher.md   # 기획·리서치
│   ├── 02_seo_strategist.md       # SEO 전략
│   ├── 03_writer.md               # 작성
│   ├── 04_editor_qa.md            # 편집·검수(중간 테스트)
│   ├── 05_image_maker.md          # 이미지 메이커
│   └── 06_assembler.md            # 조립·발행
├── guides/                   # 📚 규칙 문서
│   ├── style_guide.md             # 문체 가이드
│   ├── seo_guide.md               # 네이버 SEO 가이드
│   ├── qa_checklist.md            # QA 체크리스트(품질 게이트)
│   └── prohibited_expressions.md  # 금지 표현
├── templates/                # 🧩 작성 양식
│   ├── blog_post_template.md
│   └── keyword_map.md
└── workflow/                 # 🔄 파이프라인
    ├── pipeline.md
    └── example_run.md
```

## 빠른 시작

Claude에게 이렇게 요청하세요:

```
주제: "제주도 3박4일 가족여행 코스"
톤: 친근한 정보성 / 타깃: 30~40대 부모
→ 네이버 블로그 자동화 파이프라인 전체를 실행해줘.
```

Claude는 `output/<주제-slug>/` 에 단계별 산출물과 `final_post.md`(발행용 완성본)를 저장합니다.

## 핵심 특징
- **역할 분리**: 6개 에이전트가 각자 산출물만 책임
- **품질 게이트**: QA(중간 테스트) 통과 전엔 발행 단계로 못 넘어감
- **네이버 최적화**: C-Rank/D.I.A. 대응 SEO 규칙 내장
- **정책 안전**: 금지 표현·저작권·과장광고 필터링

자세한 운영 방식은 [`CLAUDE.md`](./CLAUDE.md) 와 [`workflow/pipeline.md`](./workflow/pipeline.md) 참고.
