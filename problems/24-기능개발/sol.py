# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 고득점 Kit · 스택/큐
# [42586] 기능개발  (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 보드 칸: 스택·큐 L2-상   |   목표: 20분 / O(n)
#
# 시작: 2026-09-14 00:00
# 힌트: ●●○○  (2/4) [접근] (100-x)//y+1은 나머지 0일 때 오프바이원.
#   올림 나눗셈 트릭: (분자 + 분모 - 1) // 분모
# ─────────────────────────────────────────────────────────

# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

# [5, 10, 1, 1, 20, 1]
# [5, 10, 10, 10, 20, 20]
# [1, 3, 2]

from itertools import accumulate, groupby
def solution(progresses, speeds):
    
    return [len(list(x)) for _, x in groupby(accumulate([(100 - x + y - 1) // y for x, y in zip(progresses, speeds) ], max))]

print(solution([93, 30, 55], [1, 30, 5]))