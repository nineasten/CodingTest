# ─────────────────────────────────────────────────────────
# 프로그래머스 · 완전탐색
# [42842] 카펫  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 보드 칸: 완전탐색 L2-하   |   목표: 30분 / O(√yellow)
#
# 시작: 2026-09-16 02:15
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

def solution(brown, yellow):
    total = brown + yellow
    a = [(i, int(total / i)) for i in range(2, int(total ** 0.5) + 1) if total % i == 0]

    for col, row in a:
        if (col - 2) * (row - 2) == yellow:
            return [row, col]
