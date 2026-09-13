# 카드 뭉치(159994) 회고

- 결과: ✅ 통과, 힌트 0/4 (힌트 미사용)
- 접근: goal의 각 원소를 순서대로 확인하며, cards1 또는 cards2의 맨 앞에서 찾기
  - deque(goal)로 각 원소를 순서대로 꺼냄
  - 각 원소가 cards1[0] 또는 cards2[0]이면 제거
  - 둘 다 아니면 "No" 반환
- 로직: 위에서 본 카드만 뽑을 수 있으므로, 순서 추적만으로 충분
- 복잡도: O(n·m) — **슬라이싱 `cards1[1:]`이 O(m) 연산**, 제약(≤100)에선 통과했지만 최적 아님
- 최적화: 두 포인터로 O(n)으로 개선 가능
  ```python
  i = j = 0
  for card in goal:
      if i < len(cards1) and cards1[i] == card:
          i += 1
      elif j < len(cards2) and cards2[j] == card:
          j += 1
      else:
          return "No"
  return "Yes"
  ```
- 원인 태그: `#복잡도역산누락` — 배열 슬라이싱이 O(n) 비용을 간과
