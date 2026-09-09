# 풀이 기록

## 막힌 지점

`queue = heapq.heapify(scoville)` — `heapify`는 제자리(in-place) 변환이라
반환값이 `None`. `queue`에 `None`이 담겨 이후 인덱싱/pop에서 에러.
`heapify(scoville)`만 호출하고 `scoville` 자체를 계속 쓰는 걸로 수정.

## 풀이 전략

`heapq.heapify`로 최소힙 구성 → 최솟값이 K 미만인 동안 가장 작은 두 개를 꺼내
`a + b*2` 공식으로 합쳐 다시 push. 원소가 1개 남았는데도 K 미만이면 -1.

## 핵심

정렬을 유지하며 매번 리스트에 삽입(`bisect.insort` 등)하면 삽입 자체가 O(N)이라
전체 O(N²) — N≤1,000,000에서 위험. 힙은 삽입도 O(log N)이라 이 문제에 적합.

## 복잡도

- 시간: O(N log N), 공간: O(1) 추가(in-place)

## 결과

통과 (0/4 힌트 — heapq 문법 질문 다수 + heapify 반환값 버그는 직접 디버깅)

## 교훈

`heapq.heapify()`, `list.sort()` 등 in-place 함수는 반환값이 `None` — 결과를
변수에 재할당하지 말고 원본 변수를 그대로 계속 사용할 것.
