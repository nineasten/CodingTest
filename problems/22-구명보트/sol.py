# ─────────────────────────────────────────────────────────
# 프로그래머스 · 탐욕법(그리디)
# [42885] 구명보트  (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 보드 칸: 그리디 L2-하   |   목표: 15분 / O(n log n)
#
# 시작: 2026-09-13 00:00
# 힌트: ●●●●  (4/4)
# 결과: ✅ 통과 (2026-09-14)
# ─────────────────────────────────────────────────────────

# [70, 50, 80, 50]	100	3
from collections import deque
def solution(people, limit):
    
    n_boats = 0
    
    q = deque(sorted(people))
    
    while q:
        n_boats += 1
        cur = q.pop()
        if q and cur + q[0] <= limit:
            q.popleft()
    
    return n_boats