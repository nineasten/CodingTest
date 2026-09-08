# ─────────────────────────────────────────────────────────
# 프로그래머스 · 구현
# [42888] 오픈채팅방  (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 보드 칸: 구현·시뮬 L2-하   |   목표: 18분 / O(N)
#
# 시작: 2026-09-08 00:00
# 힌트: ○○○○  (0/4)
# ─────────────────────────────────────────────────────────

# ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

from collections import defaultdict

def solution(records):
    users = defaultdict(str)
    ops, message = [], []
    for record in records:
        words = record.split()
        if len(words) == 2:
            op, uid = words
        else:
            op, uid, name = words
            
        if op != 'Change':
            ops.append((op, uid))
        
        if op != 'Leave':
            users[uid] = name
    
    
    for op, uid in ops:
        
        if op == 'Leave':
            message.append(f"{users[uid]}님이 나갔습니다.")
        else:
            message.append(f"{users[uid]}님이 들어왔습니다.")
            
    return message


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))