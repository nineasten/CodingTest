# [42576] 완주하지 못한 선수

- 출처: 프로그래머스 · 코딩테스트 고득점 Kit · 해시
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/42576
- 난이도: Lv.1 | 보드 칸: 해시 L1

## 요약
마라톤 참가자 `participant`와 완주자 `completion` 배열이 주어진다.
완주하지 못한 선수 1명의 이름을 반환한다. 동명이인이 있을 수 있다.

## 제약
- `participant`, `completion` 길이는 1 이상 100,000 이하
- `completion`의 길이는 `participant`의 길이보다 정확히 1 작다
- 참가자 이름은 중복될 수 있음

## 목표 복잡도
O(N) — Counter 뺄셈 (또는 O(N log N) 정렬 방식도 가능)

## 입출력 예시
- participant = ["leo","kiki","eden"], completion = ["eden","kiki"] → "leo"
- participant = ["marina","josipa","nikola","vinko","filipa"], completion = ["josipa","filipa","marina","nikola"] → "vinko"
