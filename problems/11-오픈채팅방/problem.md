# 프로그래머스 · 구현
## [42888] 오픈채팅방 (Lv.2)
https://school.programmers.co.kr/learn/courses/30/lessons/42888

**보드 칸**: 구현·시뮬 L2-하 | **목표**: 18분 / O(N)

---

## 문제 요약

오픈채팅방의 입장/퇴장 기록과 닉네임 변경 기록이 주어진다. 최종적으로 각 사용자의 최신 닉네임으로 "사용자_ID님이 입장했습니다" / "사용자_ID님이 퇴장했습니다" 형식의 메시지를 출력해야 한다.

## 제약 조건

- 기록(records)의 길이: 1 ≤ N ≤ 100,000
- 각 기록 형식: "Enter/Leave/Change user_id nickname" (Enter와 Change만 닉네임 포함)
- 같은 사용자_id가 여러 번 등장 가능

## 입출력 예시

### 입력
```
["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
```

### 출력
```
["Prodo님이 입장했습니다", "Ryan님이 퇴장했습니다", "Prodo님이 입장했습니다"]
```

설명: uid1234는 최종 "Prodo", uid4567은 최종 "Ryan"
- uid1234 입장(Muzi) → 퇴장 → 입장(Prodo) : 마지막 닉네임 Prodo 반영
- uid4567 입장(Prodo) → 닉네임 변경(Ryan) : 최종 Ryan 반영, 퇴장 메시지에 반영

---

## 풀이 목표

정답 O(N) 시간복잡도로 풀기. Change 기록은 메시지 생성이 아니라 닉네임만 업데이트.
