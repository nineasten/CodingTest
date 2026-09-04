# Python 잡기술 치트시트

`/review`에서 새로운 관용구가 나올 때마다 한 줄씩 추가한다. 코딩 중 빠른 참조용 —
자세한 설명과 상황별 예시는 `lib/playbook/`을 볼 것.

## 입출력
- `sys.stdin.readline` — 대량 입력에서 `input()`보다 빠름
- `sys.stdin.read().split()` — 입력을 통째로 읽어야 할 때

## 산술
- `합공식 - 부분합` — "고정 범위에서 1개(또는 소수개) 빠진 원소 찾기"는 set 차집합보다 `sum(range(n)) - sum(arr)`가 더 가볍다

## 자료형
- `x in set` 은 O(1), `x in list`는 O(N) — 존재 확인은 항상 set/dict
- `deque.popleft()` — `list.pop(0)`는 O(N)이라 큐엔 절대 금지
- `Counter(a) - Counter(b)` — 이쪽에만 있는 것 찾기 (음수 결과는 버려짐)

## 정렬
- `sorted(arr, key=lambda x: (-x[1], x[0]))` — 다중 기준 정렬
- `functools.cmp_to_key` — "이어붙인 결과"로 비교해야 할 때 (가장 큰 수 유형)

## 격자
- `list(zip(*grid[::-1]))` — 시계방향 90도 회전
- `[[0]*M for _ in range(N)]` — 2D 배열 초기화. `[[0]*M]*N`은 얕은 복사 함정

## 힙
- `heapq.heappush(heap, -val)` — 최댓값 힙은 부호 반전으로 흉내

## 이분탐색
- `bisect.bisect_left/right` — 직접 루프 안 짜도 되는 경우가 많음

## DP
- `functools.lru_cache` — 재귀 DP를 짧게. 인자는 불변 타입(튜플)이어야 캐시됨
