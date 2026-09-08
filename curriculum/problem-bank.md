# 문제 은행 (프로그래머스, URL 검증됨)

`/next`가 문제를 고를 때 이 표에서만 뽑는다. **모든 URL은 2026-09-03에 실제로 열어
페이지 제목이 아래 제목과 일치하는지 확인했다.** (확인 중 기억이 틀렸던 항목 2건을
실제로 잡아냈다 — 예: `42587`은 "프린터"가 아니라 "프로세스", `42578`은 "위장"이
아니라 "의상". 검증 없이는 엉뚱한 문제를 안내했을 것.)

이 표는 **초기 시드(36문제)**이며 고정 목록이 아니다. `/next`가 은행에 없는 문제를
추천해야 할 상황이면, 1.1.5절 규칙대로 **URL을 먼저 열어 확인한 뒤** 이 표에 행을
추가하고 나서 제시한다. 즉 이 파일은 계속 자라난다.

`상태` 열: `미출제` → `/next`로 낸 적 없음. `사용중` → 낸 적 있으나 보드에 미반영.
`완료` → 커버리지 보드에 ✅/⚠ 반영됨. (`/retro`가 갱신)

## 구현 · 시뮬레이션

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L1 | 없는 숫자 더하기 | 86051 | https://school.programmers.co.kr/learn/courses/30/lessons/86051 | 월간 코드 챌린지 시즌3 | 완료 |
| L1 | 시저 암호 | 12926 | https://school.programmers.co.kr/learn/courses/30/lessons/12926 | 코딩테스트 연습 | 미출제 |
| L1 | [카카오 인턴] 키패드 누르기 | 67256 | https://school.programmers.co.kr/learn/courses/30/lessons/67256 | 2020 카카오 인턴십 | 미출제 |
| L1 | 신규 아이디 추천 | 72410 | https://school.programmers.co.kr/learn/courses/30/lessons/72410 | 2021 카카오 채용연계형 | 미출제 |
| L1 | 신고 결과 받기 | 92334 | https://school.programmers.co.kr/learn/courses/30/lessons/92334 | 2022 카카오 채용연계형 | 미출제 |
| L1 | 성격 유형 검사하기 | 118666 | https://school.programmers.co.kr/learn/courses/30/lessons/118666 | 2022 카카오 테크 인턴십 | 미출제 |
| L1-L2 | 카드 뭉치 | 159994 | https://school.programmers.co.kr/learn/courses/30/lessons/159994 | 코딩테스트 연습 | 미출제 |
| L2 | [1차] 캐시 | 17680 | https://school.programmers.co.kr/learn/courses/30/lessons/17680 | 2018 카카오 채용연계형 | 미출제 |
| L2 | 오픈채팅방 | 42888 | https://school.programmers.co.kr/learn/courses/30/lessons/42888 | 2019 카카오 채용연계형 | 완료 |

## 2D 격자

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L2 | 아이템 줍기 | 87694 | https://school.programmers.co.kr/learn/courses/30/lessons/87694 | DFS/BFS (좌표평면) | 완료 |

> 이 칸이 얇다 — 순수 격자 시뮬레이션(방향벡터·회전) 문제를 `/next` 첫 사용 시
> 추가 검증해 보강할 것.

## 문자열 파싱

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L2 | 튜플 | 64065 | https://school.programmers.co.kr/learn/courses/30/lessons/64065 | 2019 카카오 겨울 인턴십 | 완료 |

## 해시

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L1 | 완주하지 못한 선수 | 42576 | https://school.programmers.co.kr/learn/courses/30/lessons/42576 | 코딩테스트 고득점 Kit · 해시 | 완료 |
| L1 | 폰켓몬 | 1845 | https://school.programmers.co.kr/learn/courses/30/lessons/1845 | 코딩테스트 연습 · 해시 | 미출제 |
| L2 | 의상 | 42578 | https://school.programmers.co.kr/learn/courses/30/lessons/42578 | 코딩테스트 고득점 Kit · 해시 | 완료 |

## 정렬

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L1 | 실패율 | 42889 | https://school.programmers.co.kr/learn/courses/30/lessons/42889 | 2019 카카오 채용연계형 | 완료 |
| L2 | 가장 큰 수 | 42746 | https://school.programmers.co.kr/learn/courses/30/lessons/42746 | 코딩테스트 고득점 Kit · 정렬 | 완료 |

## 스택 · 큐

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L2 | 프로세스 | 42587 | https://school.programmers.co.kr/learn/courses/30/lessons/42587 | 코딩테스트 고득점 Kit · 스택/큐 | 완료 |
| L2 | 기능개발 | 42586 | https://school.programmers.co.kr/learn/courses/30/lessons/42586 | 코딩테스트 고득점 Kit · 스택/큐 | 미출제 |
| L2 | 다리를 지나는 트럭 | 42583 | https://school.programmers.co.kr/learn/courses/30/lessons/42583 | 코딩테스트 고득점 Kit · 스택/큐 | 미출제 |
| L2 | 두 큐 합 같게 만들기 | 118667 | https://school.programmers.co.kr/learn/courses/30/lessons/118667 | 2022 카카오 테크 인턴십 | 미출제 |

## 힙

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L2 | 더 맵게 | 42626 | https://school.programmers.co.kr/learn/courses/30/lessons/42626 | 코딩테스트 고득점 Kit · 힙 | 미출제 |

## BFS · DFS

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L2 | 게임 맵 최단거리 | 1844 | https://school.programmers.co.kr/learn/courses/30/lessons/1844 | 코딩테스트 고득점 Kit · DFS/BFS | 미출제 |
| L2 | 타겟 넘버 | 43165 | https://school.programmers.co.kr/learn/courses/30/lessons/43165 | 코딩테스트 고득점 Kit · DFS/BFS | 미출제 |
| L2 | 아이템 줍기 | 87694 | https://school.programmers.co.kr/learn/courses/30/lessons/87694 | DFS/BFS (좌표평면) | 미출제 |
| L3 | 네트워크 | 43162 | https://school.programmers.co.kr/learn/courses/30/lessons/43162 | 코딩테스트 고득점 Kit · DFS/BFS | 미출제 |

## 완전탐색 · 백트래킹

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L1 | 모의고사 | 42840 | https://school.programmers.co.kr/learn/courses/30/lessons/42840 | 코딩테스트 고득점 Kit · 완전탐색 | 완료 |
| L2 | 소수 찾기 | 42839 | https://school.programmers.co.kr/learn/courses/30/lessons/42839 | 코딩테스트 고득점 Kit · 완전탐색 | 미출제 |
| L2 | 카펫 | 42842 | https://school.programmers.co.kr/learn/courses/30/lessons/42842 | 코딩테스트 고득점 Kit · 완전탐색 | 미출제 |
| L2 | 전력망을 둘로 나누기 | 86971 | https://school.programmers.co.kr/learn/courses/30/lessons/86971 | 완전탐색 | 미출제 |
| L2-L3 | 이모티콘 할인행사 | 150368 | https://school.programmers.co.kr/learn/courses/30/lessons/150368 | 2023 카카오 채용연계형 | 미출제 |
| L3 | N-Queen | 12952 | https://school.programmers.co.kr/learn/courses/30/lessons/12952 | 코딩테스트 연습 · 백트래킹 | 미출제 |

## 그리디

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L2 | 큰 수 만들기 | 42883 | https://school.programmers.co.kr/learn/courses/30/lessons/42883 | 코딩테스트 고득점 Kit · 탐욕법 | 미출제 |

> 이 칸도 얇다 — 조이스틱(42860)·구명보트(42885)·단속카메라(42884) 등을 다음
> 세션에서 검증해 추가할 것.

## 이분탐색

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L1 | 예산 | 12982 | https://school.programmers.co.kr/learn/courses/30/lessons/12982 | Summer/Winter Coding(~2018) | 완료 |
| L3 | 입국심사 | 43238 | https://school.programmers.co.kr/learn/courses/30/lessons/43238 | 코딩테스트 고득점 Kit · 이분탐색 | 미출제 |

## DP

| 난이도 | 제목 | ID | URL | 카테고리(출처) | 상태 |
|---|---|---|---|---|---|
| L2 | 피보나치 수 | 12945 | https://school.programmers.co.kr/learn/courses/30/lessons/12945 | 코딩테스트 연습 · DP | 미출제 |
| L3 | 정수 삼각형 | 43105 | https://school.programmers.co.kr/learn/courses/30/lessons/43105 | 코딩테스트 고득점 Kit · DP | 미출제 |
| L3 | 땅따먹기 | 12913 | https://school.programmers.co.kr/learn/courses/30/lessons/12913 | 코딩테스트 연습 · DP | 미출제 |

---

## 검증 중 잡아낸 오류 (참고용 — 왜 이 절차가 필수인지)

| 기억으로 추정한 것 | 실제 확인 결과 |
|---|---|
| `42587` = "프린터" | 실제로는 **"프로세스"** |
| `42578` = "위장" | 실제로는 **"의상"** |
| `159994` = "롤케이크 자르기" | 실제로는 **"카드 뭉치"** |
| `86051` = "배열 뒤집기" | 실제로는 **"없는 숫자 더하기"** |

→ 이래서 URL은 절대 기억만으로 등록하지 않는다.
