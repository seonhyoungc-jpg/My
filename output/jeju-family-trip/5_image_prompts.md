# 이미지 프롬프트: 제주도 3박4일 가족여행 코스

본문 `[이미지: ...]` 마커 3개 + 썸네일 = 총 4장.
**저작권 안전**: 실제 상표·인물·저작물 모사 없음, 전부 생성형 이미지.

---

## 썸네일 (대표 이미지)
- **파일명**: `jeju-family-trip-thumb.jpg`
- **alt**: 제주도 가족여행 코스 3박4일 대표 이미지
- **비율**: 16:9 (제목 텍스트 오버레이 여백을 상단 1/3에 확보)
- **프롬프트(EN)**:
```
A bright coastal road on Jeju Island, a family of four walking away from camera,
volcanic black rock shoreline and turquoise sea on the right, green grass verge,
warm late-afternoon sunlight, clean and airy travel-blog photography style,
soft natural colors, wide empty sky in upper third for text overlay,
photorealistic, 16:9
```

## 본문 이미지 1 — 1일차 (동부)
- **마커**: `[이미지: 제주 동부 해안도로를 걷는 가족]`
- **파일명**: `jeju-family-trip-01.jpg`
- **alt**: 제주 동부 해안도로를 걷는 가족
- **프롬프트(EN)**:
```
Relaxed evening scene on Jeju's eastern coast, parents and two children strolling
along a quiet seaside path, low stone wall, calm sea, gentle golden-hour light,
unhurried mood suggesting an easy first travel day, photorealistic travel photography,
natural muted palette, 4:3
```

## 본문 이미지 2 — 2일차 (우도)
- **마커**: `[이미지: 우도로 향하는 배에서 바라본 바다]`
- **파일명**: `jeju-family-trip-02.jpg`
- **alt**: 우도로 향하는 배에서 바라본 제주 바다 풍경
- **프롬프트(EN)**:
```
View from the deck of a passenger ferry crossing to a small island near Jeju,
white wake trailing on deep blue water, distant green island on the horizon,
bright clear morning, sea breeze feeling, no visible logos or text,
photorealistic, cheerful travel mood, 4:3
```

## 본문 이미지 3 — 우천 대체 코스
- **마커**: 우천 섹션에 신규 배치 권장 (현재 마커 없음 → 조립 단계에서 추가)
- **파일명**: `jeju-family-trip-03.jpg`
- **alt**: 비 오는 날 제주 실내 여행지 분위기
- **프롬프트(EN)**:
```
Cozy indoor space on a rainy day in Jeju, large window with raindrops,
blurred green island landscape outside, warm interior lighting,
a family sitting comfortably by the window, calm and reassuring atmosphere,
photorealistic, soft warm tones, 4:3
```

---

## 파일 생성 상태
| 파일 | 상태 |
|------|------|
| `jeju-family-trip-thumb.jpg` | ⏳ 미생성 (프롬프트 준비 완료) |
| `jeju-family-trip-01.jpg` | ⏳ 미생성 |
| `jeju-family-trip-02.jpg` | ⏳ 미생성 |
| `jeju-family-trip-03.jpg` | ⏳ 미생성 |

> 이 실행은 **파이프라인 검증용 드라이런**이라 실제 이미지 생성은 하지 않았습니다.
> 실제 발행 시 이미지 생성 도구로 위 프롬프트를 그대로 사용하면 `images/` 폴더에 생성됩니다.

## 체크
- [x] 모든 이미지에 프롬프트·파일명·alt 완비
- [x] 파일명이 SEO 규칙(영문 키워드-하이픈) 준수
- [x] alt에 키워드 자연 포함
- [x] 저작권 안전 (상표·실인물·기존 저작물 없음)
