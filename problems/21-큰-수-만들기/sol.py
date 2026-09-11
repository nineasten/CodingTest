# ─────────────────────────────────────────────────────────
# 프로그래머스 · 탐욕법(그리디)
# [42883] 큰 수 만들기  (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 보드 칸: 그리디 L2-하   |   목표: 20분 / O(n)
#
# 시작: 2026-09-11 00:00
# 힌트: ●●●○  (3/4)
# [1단계 2026-09-11] i==len-2 분기 후 modified 줄인 다음 modified[i+1] 인덱스가 유효한지?
# [2단계 2026-09-11] 매번 처음부터 재스캔하면 O(n·k) — 한 번의 순회로 끝나는 스택 기반 그리디로
# [3단계 2026-09-11] push 직전 while로 "top<현재값 and k남음"이면 pop, 끝나고 k남으면 뒤에서 자르기
# ─────────────────────────────────────────────────────────

# "4177252841"	4	"775841"
from collections import deque

def solution(number, k):

    q = deque(number)
    store = []
    n_del = 0
    
    while n_del < k:
        if store and store[-1] < q[0]:
            store.pop()
            n_del += 1
            continue
        
        store.append(q.popleft())
        
        if not q:
            store.pop()
            n_del += 1
            continue
        
        if store[-1] < q[0]:
            store.pop()
            n_del += 1
    
    return ''.join(store + list(q))
