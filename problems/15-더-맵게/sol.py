# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 고득점 Kit · 힙
# [42626] 더 맵게  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 보드 칸: 힙 L2-하   |   목표: 15분 / O(N log N)
#
# 시작: 2026-09-08 00:00
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

# [1, 2, 3, 9, 10, 12]	7	2
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    
    result = 0
    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first + second * 2)
        result += 1
    
    if scoville[0] < K:
        return -1
    
    return result
        

print(solution([1, 2, 3, 9, 10, 12], 7))