# 행렬 테두리 회전하기

- 출처: 프로그래머스 · 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
- 문제 ID: 77485
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/77485
- 난이도: Lv.2
- 보드 칸: 2D 격자 L2-하 (재도전 — 아이템 줍기(87694) ⚠ 이후)

## 요약
rows × columns 크기 행렬에 1부터 rows×columns까지 순서대로 채운다. queries의 각
[x1,y1,x2,y2]에 대해 그 사각형 테두리의 숫자들을 시계방향으로 한 칸씩 회전시키고,
그 회전으로 위치가 바뀐 숫자들 중 최솟값을 결과 배열에 순서대로 담아 반환.

## 제약
- 2 ≤ rows, columns ≤ 100
- 1 ≤ queries 길이 ≤ 10,000
- 각 query: 1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns

## 목표 복잡도
회전 1회당 테두리 둘레 길이는 최대 O(rows+columns) ≈ 400.
쿼리 최대 10,000개 → 전체 O(Q × (rows+columns)) ≈ 4×10⁶으로 충분히 여유.

## 입출력 예시
| rows | columns | queries | result |
|---|---|---|---|
| 6 | 6 | [[2,2,5,4],[3,3,6,6],[5,1,6,3]] | [8, 10, 25] |
