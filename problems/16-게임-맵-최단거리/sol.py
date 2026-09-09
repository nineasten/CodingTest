# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 고득점 Kit · DFS/BFS
# [1844] 게임 맵 최단거리  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 보드 칸: BFS·DFS L2-하   |   목표: 15분 / O(N×M)
#
# 시작: 2026-09-09 00:00
# 힌트: ●○○○  (1/4) — 2026-09-09: 방향 4개 순회 안 됨 + 벽 체크 누락 (관찰)
# ─────────────────────────────────────────────────────────

# [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
from collections import deque
def solution(maps):
    
    queue = deque([[0, 0, 1]])
    visited = {(0, 0)}
    n, m = len(maps), len(maps[0])
    while queue:
        
        cur = queue.popleft()
        
        neighbors = [[cur[0] + x, cur[1] + y] for x, y in zip([0, 0, 1, -1], [-1, 1, 0, 0])]
        for neighbor in neighbors:
            x, y = neighbor
            if neighbor == [n-1, m-1]:
                return cur[2] + 1

            if 0 <= x < n and 0 <= y < m and maps[x][y] and (x, y) not in visited:
                queue.append([x, y, cur[2] + 1])
                visited.add((x, y))
    
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))