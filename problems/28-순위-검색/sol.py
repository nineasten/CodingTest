# ─────────────────────────────────────────────────────────
# 프로그래머스 · 2019 카카오 개발자 겨울 인턴십
# [72412] 순위 검색  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/72412
# 보드 칸: 이분탐색 L2-하   |   목표: 30분 / O((N+M)*16*log N)
#
# 시작: 2026-09-15
# 힌트: ●●●○  (3/4) — 2026-09-15 핵심로직: 조건 4개 → 2^4=16 와일드카드 조합 키로 info를 미리 그룹핑, 쿼리는 키 그대로 조회 후 bisect_left로 "이상 개수"
# ─────────────────────────────────────────────────────────

# ["java backend junior pizza 150",
# "python frontend senior chicken 210",
# "python frontend senior chicken 150",
# "cpp backend senior pizza 260",
# "java backend junior chicken 80",
# "python backend senior chicken 50"]
# 
# ["java and backend and junior and pizza 100",
# "python and frontend and senior and chicken 200",
# "cpp and - and senior and pizza 250",
# "- and backend and senior and - 150",
# "- and - and - and chicken 100",
# "- and - and - and - 150"]
# 
# [1,1,1,1,2,4]

from itertools import product
from collections import defaultdict
import bisect
def solution(info, query):
    dd = defaultdict(list)
    result = []
    for inf in info:
        a, b, c, d, score = inf.split(' ')
        for key in product([a, '-'], [b, '-'], [c, '-'], [d, '-']):
            dd[key].append(int(score))
    
    for v in dd.values():
        v.sort()
    
    for q in query:
        a, b, c, d = q.split(' and ')
        d, score = d.split(' ')
        val_list = dd[(a, b, c, d)]
        result.append(len(val_list) - bisect.bisect_left(val_list, int(score)))
        
    return result

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))