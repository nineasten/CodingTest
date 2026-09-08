# ─────────────────────────────────────────────────────────
# 프로그래머스 · 2019 카카오 개발자 겨울 인턴십
# [64061] 크레인 인형뽑기 게임  (Lv.1)
# https://school.programmers.co.kr/learn/courses/30/lessons/64061
# 보드 칸: 2D 격자 L1   |   목표: 15분 / O(n²)
#
# 시작: 2026-09-08 00:00
# 힌트: ●○○○  (1/4)
# ─────────────────────────────────────────────────────────

from collections import deque
def solution(board, moves):
    queues_len = len(board)
    queus = [deque() for _ in range(queues_len)]
    for row in board:
        for i, col in enumerate(row):
            if col:
                queus[i].append(col)

    moved = []
    score = 0
    print(queus)
    for n in moves:
        n -= 1
        if queus[n]:
            top = queus[n].popleft()
            if moved:
                if moved[-1] == top:
                    moved.pop()
                    score += 2
                else:
                    moved.append(top)
            else:
                moved.append(top)
        
    return score
                
                        
                        
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))