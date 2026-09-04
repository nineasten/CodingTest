# ─────────────────────────────────────────────────────────
# 프로그래머스 · 2019 카카오 채용연계형
# [42889] 실패율  (Lv.1)
# https://school.programmers.co.kr/learn/courses/30/lessons/42889
# 보드 칸: 정렬 L1   |   목표: 10분 / O(N log N)
#
# 시작: 2026-09-04
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

# 실패율 = 각 단계에 머물러 있는 유저 수 / 그 단계 포함 그 이후로 진출한 유저 수
from collections import Counter
def solution(N, stages):
    fail_rate = {i: -1 for i in range(1, N+1)}
    user_cnt = Counter(stages)
    n_user = len(stages)
    for i in range(1, N+1):
        x = user_cnt[i]
        if n_user == 0:
            fail_rate[i] = 0
        else:
            fail_rate[i] = x / n_user
        n_user -= x
    
    return [x for x, _ in sorted(fail_rate.items(), key=lambda x : (-x[1], x[0]))]
