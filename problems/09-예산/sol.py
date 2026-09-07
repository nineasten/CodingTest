# ─────────────────────────────────────────────────────────
# 프로그래머스 · Summer/Winter Coding(~2018)
# [12982] 예산  (Lv.1)
# https://school.programmers.co.kr/learn/courses/30/lessons/12982
# 보드 칸: 이분탐색 L1   |   목표: 15분 / O(N log N)
#
# 시작: 2026-09-07
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────


def solution(d, budget):
    
    cur, result = 0, 0
    for x in sorted(d):
        cur += x
        result += 1
        if cur > budget:
            return result - 1
        
        print(f'cur: {cur}, result: {result}')
        
    return result

print(solution([2,2,3,3], 8))