# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 고득점 Kit · 스택/큐
# [42587] 프로세스  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 보드 칸: 스택·큐 L2-하   |   목표: 15분 / O(N²)
#
# 시작: 2026-09-04
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

from collections import deque

def solution(priorities, location): 
    queue = deque(enumerate(priorities))
    executed = 0
    while queue:
        idx, priority = queue.popleft()
        if any(priority < x for _ , x in queue):
            queue.append((idx, priority))
        else:
            executed += 1
            if idx == location:
                return executed
