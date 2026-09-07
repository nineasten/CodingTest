# ─────────────────────────────────────────────────────────
# 프로그래머스 · 2019 카카오 겨울 인턴십
# [64065] 튜플  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 보드 칸: 문자열 파싱 L2   |   목표: 20분 / O(L + n log n)
#
# 시작: 2026-09-07
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────


def solution(s):
    a, b, comp = [], [], ''
    for str in s[1:-1]:
        if str == '{':
            a.append(str)
        elif str == '}':
            a.pop()
            b.append({int(x) for x in comp.split(',')})
            comp = ''
        else:
            if not a:
                continue
            if a[-1] == '{':
                comp += str
        
    #     print(f'comp: {comp}')
    # print(f'b:{b}')
    
    b.sort(key=lambda x : len(x))
    result = [b[0]]
    for i in range(len(b)-1):
        result.append(b[i+1]-b[i])
    return [next(iter(x)) for x in result]


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))