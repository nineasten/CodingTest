# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 고득점 Kit · 정렬
# [42746] 가장 큰 수  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 보드 칸: 정렬 L2-하   |   목표: 18분 / O(N log N)
#
# 시작: 2026-09-07
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────


from functools import cmp_to_key

def compare(a: str, b: str) -> int:
    
    if a + b > b + a: 
        return -1
    
    # a = '3', b = '30' 일 때 330 > 303 이므로 a가 왼쪽에 와야 함.
    # 비교 방식은 두 수를 조합해서 큰 수가 만들어지도록.
    if a + b == b + a:
        return 0
    
    else:
        return 1
    
    
def solution(numbers):
    numbers = sorted(map(str, numbers), key = cmp_to_key(compare))
    result = ''.join(numbers)

    
    return '0' if result[0] == '0' else result

print(solution([6, 10, 2]))