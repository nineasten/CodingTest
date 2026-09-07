# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 고득점 Kit · 완전탐색
# [42840] 모의고사  (Lv.1)
# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 보드 칸: 완전탐색·백트래킹 L1   |   목표: 15분 / O(N)
#
# 시작: 2026-09-06
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

# 1 2 3 4 5
# 2 1 2 3 2 4 2 5
# 3 3 1 1 2 2 4 4 5 5

# 문제 길이랑 각 답변 길이를 동일하게 만든 다음에 하나씩 비교

def solution(answers):
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    doc = [one, two, three]
    
    for i in range(3):
        correct = sum(1 for a, b in zip(doc[i], answers) if a == b)
        doc[i] = correct


    return [i + 1 for i, score in enumerate(doc) if score == max(doc)]
    