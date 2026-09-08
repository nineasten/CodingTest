# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 연습
# [12906] 같은 숫자는 싫어  (Lv.1)
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 보드 칸: 스택·큐 L1   |   목표: 10분 / O(N)
#
# 시작: 2026-09-08 00:00
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

# [1,1,3,3,0,1,1]	[1,3,0,1]
from collections import deque
def solution(arr):
    queue = arr
    result = deque()
    while queue:
        result.appendleft(queue.pop())
        while queue and queue[-1] == result[0]:
            queue.pop()
    return list(result)
    
print(solution([1,1,3,3,0,1,1]))
