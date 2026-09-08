# ─────────────────────────────────────────────────────────
# 프로그래머스 · 코딩테스트 연습
# [12930] 이상한 문자 만들기  (Lv.1)
# https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 보드 칸: 문자열 파싱 L1   |   목표: 12분 / O(N)
#
# 시작: 2026-09-08 00:00
# 힌트: ●●○○  (2/4)
# 1단계(관찰 2026-09-08): split()/join()이 연속 공백을 보존하는지 확인
# 2단계(접근 2026-09-08): 원본 문자열 1회 순회 + 공백 만나면 인덱스 리셋
# ─────────────────────────────────────────────────────────

# "try hello world"	"TrY HeLlO WoRlD"
def solution(s):
    i = 0
    new_s = ''
    for ch in s:
        if ch == ' ':
            i = 0
            new_s += ' '
        else:
            if i % 2 == 0:
                new_s += ch.upper()
            else:
                new_s += ch.lower()
            i += 1
    return new_s
        
print(solution("try hello world"))
