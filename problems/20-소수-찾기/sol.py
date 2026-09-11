# ─────────────────────────────────────────────────────────
# 프로그래머스 · 완전탐색
# [42839] 소수 찾기  (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 보드 칸: 완전탐색·백트래킹 L2-하   |   목표: 20분 / O(n! · √(10^n)), n≤7
#
# 시작: 2026-09-10 00:00
# 힌트: ●○○○  (1/4)
# [1단계 2026-09-10] 길이 1~7 순열 전부 만들면 몇 개? "011"처럼 앞자리 0은 어떻게 처리?
# ─────────────────────────────────────────────────────────

# "011"	2

from itertools import permutations

def is_prime(n: int) -> bool:
    if n < 2:
        return 0
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    
    return 1

def solution(numbers):
    
    n_prime = 0
    for num in {int(''.join(x)) for i in range(1, len(numbers) + 1) for x in permutations(numbers, i)}:
        if is_prime(num):
            n_prime += 1
    
    return n_prime