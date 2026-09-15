# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 연습
# [68645] 삼각 달팽이  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/68645
# 보드 칸: 2D 격자 L2-하   |   목표: 25분 / O(n^2)
#
# 시작: 2026-09-15
# 힌트: ●●○○  (2/4) — 2026-09-15 접근: BFS/DFS 아님, 방향전환 시뮬레이션(구현)
# ─────────────────────────────────────────────────────────

# 5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]

def solution(n):
    results = [[0] * i for i in range(1, n+1)]
    lens = [i for i in range(1, n+1)]
    x, y = 0, 0
    cur, div = 0, 0
    while lens:
        filled = 0
        to_fill = lens.pop()
        for i in range(cur + 1, cur + to_fill + 1): # i = 1, 2, 3, 4, 5
            results[x][y] = i
            filled += 1

            
            if div % 3 == 0:
                if filled < to_fill:
                    x += 1
                else:
                    y += 1
                    
            elif div % 3 == 1:
                if filled < to_fill:
                    y += 1
                else:
                    x -= 1
                    y -= 1
            else:
                if filled < to_fill:
                    x -= 1
                    y -= 1
                else:
                    x += 1
                
            
        div += 1
        cur += to_fill
        
    return [v for row in results for v in row]  
print(solution(5))
