# 구명보트

- 출처: 프로그래머스 · 탐욕법(그리디)
- 문제 ID: 42885
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/42885
- 난이도: Lv2

## 요약
사람들의 몸무게가 배열 `people`로 주어진다. 각 보트는 최대 2명까지 탈 수 있고,
각 보트의 무게 제한은 `limit`이다. 모든 사람을 구출하는 데 필요한 최소 보트 수를
구한다.

## 제약
- 1 ≤ people 길이 ≤ 50,000
- 1 ≤ limit ≤ 120,000
- 1 ≤ people[i] ≤ limit

## 목표 복잡도
O(n log n) — 정렬 후 두 포인터로 O(n)
