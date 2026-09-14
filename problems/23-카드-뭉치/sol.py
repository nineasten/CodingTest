# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 연습
# [159994] 카드 뭉치  (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/159994
# 보드 칸: 구현·시뮬레이션 L2-상   |   목표: 15분 / O(n)
#
# 시작: 2026-09-14 00:00
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

# ["i", "drink", "water"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"Yes"


def solution(cards1, cards2, goal):
    
    i = j = 0
    for word in goal:
        if i < len(cards1) and cards1[i] == word:
            i += 1
        elif j < len(cards2) and cards2[i] == word:
            j += 1
        else:
            return "No"
        
    return "Yes"

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))