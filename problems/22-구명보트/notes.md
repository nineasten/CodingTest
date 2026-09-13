# 구명보트(42885) 회고

- 결과: ✅ 통과, 힌트 3/4
- 접근: deque + 정렬을 이용한 투포인터
  - sorted(people)로 오름차순 정렬
  - deque의 뒤(pop)는 가장 무거운 사람, 앞(popleft)는 가장 가벼운 사람
  - 무거운 사람을 먼저 꺼내고, 가벼운 사람이 함께 탈 수 있으면 함께 탐
- 로직: 각 보트는 최대 2명까지 탈 수 있고, 무거운 사람은 반드시 탈 보트가 필요 →
  가장 가벼운 사람과 짝짓기
- 잡기술: deque는 정확하지만, 인덱스 투포인터가 더 간단하고 공간 효율적
  ```python
  people = sorted(people)
  left, right = 0, len(people) - 1
  boats = 0
  while left < right:
      if people[left] + people[right] <= limit:
          left += 1
      right -= 1
      boats += 1
  if left == right:
      boats += 1
  return boats
  ```
- 결과: 투포인터 완전 습득, 큰 수 만들기 이후 그리디 L2-하 칸 ✅로 완성
