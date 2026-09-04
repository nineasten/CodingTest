# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 고득점 Kit · 해시
# [42576] 완주하지 못한 선수  (Lv.1)
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 보드 칸: 해시 L1   |   목표: 7분 / O(N)
#
# 시작: 2026-09-04
# 힌트: ●○○○  (1/4)
#   1단계 09-04 - 정렬 비교 방식이면 시간복잡도가 목표 O(N)과 맞는지 질문
# ─────────────────────────────────────────────────────────

from collections import Counter

def solution(participant, completion):
    n_participant = Counter(participant)
    n_completion = Counter(completion)
    
    for k, v in (n_participant - n_completion).items():
        if v == 1:
            return k
