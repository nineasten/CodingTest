# ─────────────────────────────────────────────────────────
# 프로그래머스 · 탐욕법(그리디)
# [135808] 과일 장수  (Lv1)
# https://school.programmers.co.kr/learn/courses/30/lessons/135808
# 보드 칸: 그리디 L1   |   목표: 15분 / O(n log n)
#
# 시작: 2026-09-10 00:00
# 힌트: ●○○○  (1/4)
# [1단계 2026-09-10] 상자 가격은 "최솟값 × m" — 어떤 사과를 같이 묶어야 낮은 점수가 덜 낭비될까?
# 결과: ✅ 통과 (2026-09-10)
# ─────────────────────────────────────────────────────────

# 4	3	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	33
def solution(k, m, score):
    to_cut = len(score) % m
    greedy_list = sorted(score)[to_cut:]
    
    return sum(greedy_list[i] * m for i in range(0, len(greedy_list), m))
    
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
