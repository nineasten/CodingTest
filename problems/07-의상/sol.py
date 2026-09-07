# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 고득점 Kit · 해시
# [42578] 의상  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 보드 칸: 해시 L2-하   |   목표: 15분 / O(N)
#
# 시작: 2026-09-06
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

# 종류별로 뭔 의상이 있는지 확인
from collections import defaultdict

def solution(clothes):
    menu = defaultdict(list)
    for name, sort in clothes:
        menu[sort].append(name)
    
    result = 1
    for num in [len(x) for x in menu.values()]:
        result *= num + 1
    
    return result - 1
    
