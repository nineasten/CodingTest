# Python 잡기술 치트시트

`/review`에서 새로운 관용구가 나올 때마다 한 줄씩 추가한다. 코딩 중 빠른 참조용 —
자세한 설명과 상황별 예시는 `lib/playbook/`을 볼 것.

## 입출력
- `sys.stdin.readline` — 대량 입력에서 `input()`보다 빠름
- `sys.stdin.read().split()` — 입력을 통째로 읽어야 할 때

## 문자열
- `re.findall(r'\{[^{}]*\}', s)` — 중첩 괄호에서 "가장 안쪽" 덩어리만 통째로 추출 (스택으로 깊이 추적하는 것보다 짧고 안전)

## 산술
- `합공식 - 부분합` — "고정 범위에서 1개(또는 소수개) 빠진 원소 찾기"는 set 차집합보다 `sum(range(n)) - sum(arr)`가 더 가볍다

## 자료형
- `x in set` 은 O(1), `x in list`는 O(N) — 존재 확인은 항상 set/dict
- `deque.popleft()` — `list.pop(0)`는 O(N)이라 큐엔 절대 금지
- `Counter(a) - Counter(b)` — 이쪽에만 있는 것 찾기 (음수 결과는 버려짐)
- `next(iter(counter_or_dict))` — 딱 1개만 남는 게 보장될 때 루프 없이 바로 꺼내기
- `Counter(item for _, item in pairs)` — 제너레이터로 초기화 (의상처럼 "이름은 버리고 종류만" 경우)
- `reduce(mul, values, 초기값)` — 연속 곱셈. `from functools import reduce; from operator import mul`

## 루프 · 필터링
- `sum(1 for a, b in zip(...) if a == b)` — 조건부 카운트 (직접 루프 + 누적보다 한줄)
- `[x for x in arr if condition]` — 필터링. `any(x in col for x in arr)` 로 "어떤 것이라도" 확인

## 정렬
- `sorted(arr, key=lambda x: (-x[1], x[0]))` — 다중 기준 정렬
- `functools.cmp_to_key` — "이어붙인 결과"로 비교해야 할 때 (가장 큰 수 유형)

## 격자
- `list(zip(*grid[::-1]))` — 시계방향 90도 회전
- `[[0]*M for _ in range(N)]` — 2D 배열 초기화. `[[0]*M]*N`은 얕은 복사 함정
- 좌표 전부 `*2` → 답은 `// 2` — 선(도형)을 격자 칸으로 옮길 때 간격 1이 붙어버리는
  거짓 인접 방지 (아이템 줍기류)
- `{(r, c)}` — set 리터럴. `set((r, c))`는 튜플이 풀려 원소 2개짜리가 됨
- set은 `.add()` (`.append()` 없음)

## 힙
- `heapq.heappush(heap, -val)` — 최댓값 힙은 부호 반전으로 흉내

## 이분탐색
- `bisect.bisect_left/right` — 직접 루프 안 짜도 되는 경우가 많음
- `bisect.bisect_right(itertools.accumulate(sorted(arr)), 한도)` — "정렬 후 누적합이 한도를 넘지 않는 최대 개수"를 한 줄로 (예산류)

## DP
- `functools.lru_cache` — 재귀 DP를 짧게. 인자는 불변 타입(튜플)이어야 캐시됨
