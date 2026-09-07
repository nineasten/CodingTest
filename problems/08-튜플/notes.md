# [64065] 튜플 — 노트

- 난이도: Lv.2 | 유형: 문자열 파싱
- 결과: 통과 (한 번에 정답)
- 힌트: 0/4

## 핵심 아이디어
크기 오름차순 정렬 후, 인접한 두 집합의 차집합이 "새로 추가된 원소" —
그게 곧 다음 튜플 원소. 크기가 1..n으로 항상 유일하게 매겨진다는 문제 보장이
이 방식을 안전하게 만든다.

## 리뷰에서 나온 리팩토링
스택으로 중괄호 깊이를 직접 추적하는 대신 `re.findall(r'\{[^{}]*\}', s)`로
가장 안쪽 덩어리만 한 번에 뽑으면 깊이 관리 코드 자체가 사라짐.

```python
import re
tokens = re.findall(r'\{[^{}]*\}', s)
sets = sorted((set(map(int, t.strip('{}').split(','))) for t in tokens), key=len)
result = [next(iter(sets[0]))]
for i in range(1, len(sets)):
    result.append(next(iter(sets[i] - sets[i-1])))
```

## 스타일
- 반복문 변수로 `str` 쓰면 내장 함수 섀도잉 — `ch` 등으로.
