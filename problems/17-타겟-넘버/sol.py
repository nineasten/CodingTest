# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 고득점 Kit · DFS/BFS
# [43165] 타겟 넘버  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 보드 칸: BFS·DFS L2-상   |   목표: 15분 / O(2^n)
#
# 시작: 2026-09-09 00:00
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

# [1, 1, 1, 1, 1]	3	5
from collections import deque



def solution(numbers, target):
    
    results = []
    def func(pre, i):

        if i == len(numbers) - 1:
            return

        i += 1
        results.extend([func((pre + numbers[i]), i),func((pre - numbers[i]), i)])

    
    pass


