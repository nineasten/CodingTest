# 카드 뭉치

- 출처: 프로그래머스 · 코딩테스트 연습
- 문제 ID: 159994
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/159994
- 난이도: Lv2

## 요약
두 개의 카드 뭉치(배열 `cards1`, `cards2`)와 목표 배열 `goal`이 주어진다.
cards1과 cards2의 맨 위 카드부터 순서대로만 뽑을 수 있다. 
goal의 순서대로 카드를 뽑을 수 있으면 "Yes", 아니면 "No"를 반환한다.

## 제약
- cards1, cards2, goal 길이 ≤ 100
- 각 배열의 원소는 1~100 범위의 정수

## 목표 복잡도
O(n) — 선형 추적으로 충분 (양쪽 포인터 또는 덱)
