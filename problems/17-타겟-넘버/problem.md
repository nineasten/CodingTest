# 타겟 넘버

- 출처: 프로그래머스 · 코딩테스트 고득점 Kit · DFS/BFS
- 문제 ID: 43165
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/43165
- 난이도: Lv.2 | 보드 칸: BFS·DFS L2-상

## 요약
음이 아닌 정수 배열 `numbers`의 각 숫자 앞에 `+` 또는 `-`를 하나씩 붙여 만들 수 있는
모든 식 중, 계산 결과가 `target`이 되는 식의 개수를 구한다.

## 제약
- `numbers`의 길이: 2 ≤ n ≤ 20
- `numbers`의 원소: 1 ≤ 값 ≤ 50
- `target`: -1000 ≤ target ≤ 1000

## 목표 복잡도
각 숫자마다 `+`/`-` 두 갈래로 갈라지는 완전탐색 → O(2^n). n≤20이면 최대 약
1,048,576번 — DFS/백트래킹으로 충분히 시간 내 처리 가능.

## 목표 시간
15분
