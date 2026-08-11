# 영상 플랜: 제주도 3박4일 가족여행 코스

## 컨셉: **요약형** (3박4일 동선을 30초로 압축)
글의 핵심인 "권역 고정 동선"을 지도 흐름처럼 보여주어, 본문을 읽기 전에 전체 그림을 잡아준다.

## 삽입 위치
**"3박4일 전체 동선 한눈에 보기"** 섹션의 표 바로 위.
→ 도입 직후 영상이 나와 체류시간을 초반에 확보한다.

## 규격
- 길이: **30초**
- 비율: 16:9 (본문 삽입용) / 9:16 세로 버전은 숏폼 재활용 시 별도 렌더
- 자막: 한글 필수 (무음 시청 대응)

## 스토리보드

| 컷 | 장면 | 자막 | 길이 |
|----|------|------|------|
| 1 | 제주 해안도로 항공 뷰, 서서히 전진 | 제주 3박4일, 동선이 전부입니다 | 4s |
| 2 | 지도 그래픽 위 동부 권역 하이라이트 | 1일차 · 공항 인근 동부 — 가볍게 | 5s |
| 3 | 배에서 바라본 바다, 섬이 다가옴 | 2일차 · 성산과 우도 | 5s |
| 4 | 남부 오름의 완만한 능선과 초원 | 3일차 · 서귀포 남부 | 5s |
| 5 | 서부 해안 도로를 달리는 차창 뷰 | 4일차 · 서부 지나 공항으로 | 5s |
| 6 | 창밖에 비, 실내에서 쉬는 분위기 | 비 오면? 대체 코스도 준비했어요 | 6s |

## 생성 프롬프트(EN)

**컷 1**
```
Slow aerial push-in over a coastal road on a green volcanic island,
turquoise sea on one side, bright clear day, cinematic travel intro, 4 seconds
```

**컷 3**
```
POV from a ferry deck approaching a small green island, white wake on blue water,
gentle boat motion, sunny morning, cinematic, 5 seconds
```

**컷 4**
```
Wide shot of a gently sloping grassy volcanic hill under soft sunlight,
wind moving through the grass, calm and open, cinematic, 5 seconds
```

**컷 6**
```
Interior of a warm room, rain streaking down a large window,
blurred green landscape outside, cozy reassuring mood, cinematic, 6 seconds
```

> 컷 2, 5는 지도 그래픽·차창 뷰로 편집 단계에서 구성 (생성형 영상보다 그래픽이 정확도 높음)

## 오디오
- 배경음: 밝고 잔잔한 무료 라이선스 트랙 (저작권 안전)
- 나레이션: **불필요** — 자막 중심 (무음 시청 비중 고려)

## 파일
| 파일 | 상태 |
|------|------|
| `videos/jeju-family-trip-clip.mp4` | ⏳ 미생성 (스토리보드·프롬프트 준비 완료) |
| 썸네일 프레임 | 컷 1의 마지막 프레임 권장 |

> 이 실행은 **파이프라인 검증용 드라이런**이라 실제 영상 생성은 하지 않았습니다.

## 체크
- [x] 스토리보드가 본문 구성(1~4일차 + 우천)과 일치
- [x] 삽입 위치 명확
- [x] 자막 문안 작성 (무음 대응)
- [x] 저작권 안전 (무료 라이선스 음원, 생성형 영상, 상표 없음)
