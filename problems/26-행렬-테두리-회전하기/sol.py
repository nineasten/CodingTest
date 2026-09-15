# ─────────────────────────────────────────────────────────
# 프로그래머스 · 2021 Dev-Matching 백엔드(상반기)
# [77485] 행렬 테두리 회전하기  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/77485
# 보드 칸: 2D 격자 L2-하   |   목표: 25분 / O(Q×(rows+columns))
#
# 시작: 2026-09-15
# 힌트: ●●●○  (3/4) — 2026-09-15 통과. maps 축(row/col) 혼동 + rotate() in-place 실수 직접 수정
# ─────────────────────────────────────────────────────────

# 6	6	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	[8, 10, 25]
from collections import deque
def solution(rows, columns, queries):
    
    maps = [[i + j for i in range(1, columns + 1)] for j in range(0, columns * rows, columns)]
    q = deque(queries)
    results = []
    while q:    
        next = q.popleft()
        x1, y1, x2, y2 = [i - 1 for i in next]  # 인덱스로
        
        indices = []
        for y in range(y1, y2+1):
            indices.append([x1, y])
        
        for x in range(x1+1, x2):
            indices.append([x, y2])
            
        for y in range(y2, y1-1, -1):
            indices.append([x2, y])
        
        for x in range(x2-1, x1, -1):   
            indices.append([x, y1])

        
        values = deque([maps[x][y] for x, y in indices])
        values.rotate(1)
        results.append(min(values))
        
        for (x, y), v in zip(indices, values):
            maps[x][y] = v

        
    return results  
            
    
print(solution(100, 97, [[1,1,100,97]]))
# 