# ─────────────────────────────────────────────────────────
# 프로그래머스 · DFS/BFS
# [87694] 아이템 줍기  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 보드 칸: 2D 격자 L2   |   목표: 20분 / O(N×M)
#
# 시작: 2026-09-05
# 힌트: ●●●○  (3/4)
#   1단계 09-05 - 격자 표현 + 탐색 방법이 뭘까?
#   2단계 09-05 - BFS로 격자 최단거리 (직사각형→격자 변환 + 상하좌우 이동)
#   3단계 09-05 - 핵심 함정: 좌표 2배 확장 필요 (겹치는 사각형의 벽 두께 문제)
# ─────────────────────────────────────────────────────────


from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    map = [[0] * 51 for _ in range(51)]
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1,x2+1):
            for y in range(y1, y2+1):
                map[x][y] = 1

    for x1, y1, x2, y2 in rectangle:
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                map[x][y] = 0
    

    visited = set([(characterX, characterY)])
    queue = deque([(characterX, characterY, 0)])
    vertical = [0, 0, -1, 1]
    horizonal = [-1, 1, 0, 0]
    while queue:
        x, y, dist = queue.popleft()
        
        if (x, y) == (itemX, itemY):
            return dist
        
        for i in range(4):
            next_x, next_y = x + horizonal[i], y + vertical[i]
            
            if 0 < next_x < 51 and 0 < next_y < 51 and map[next_x][next_y] == 1 and (next_x, next_y) not in visited:
                queue.append((next_x, next_y, dist + 1))
                visited.add((next_x, next_y))