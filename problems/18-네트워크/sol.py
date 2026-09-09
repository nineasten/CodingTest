# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 고득점 Kit · DFS/BFS
# [43162] 네트워크  (Lv.3)
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 보드 칸: BFS·DFS L3-초   |   목표: 20분 / O(n^2)
#
# 시작: 2026-09-09 00:00
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
from collections import deque
def solution(n, computers):
    answer = 0
    visited = set()
    for i in range(n):
        
        if i in visited:
            continue
        
        answer += 1
        q = deque([i])
        visited.add(i)
        while q:
            cur = q.popleft()
            for idx, computer in enumerate(computers[cur]):
                if computer and idx not in visited:
                    q.append(idx)
                    visited.add(idx)
    
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))