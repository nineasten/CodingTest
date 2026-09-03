# 공통: 정렬과 key

## 1. 언제 이 기술인가 — 문제 속 신호
"순서대로 정렬해", "우선순위가 높은 것부터", "여러 기준으로 비교" 가 나오면 정렬 문제다.
정렬 자체는 쉽지만 **기준(key)을 어떻게 세우느냐**가 시험에서 갈린다.

## 2. 상황별 한국어 설명 + 예시 코드

### 상황 A: 기본 오름차순/내림차순
```python
arr.sort()                 # 제자리 정렬 (반환값 없음)
new_arr = sorted(arr)      # 새 리스트 반환
arr.sort(reverse=True)     # 내림차순
```

### 상황 B: 특정 값 기준으로 정렬 (key)
튜플/객체 리스트를 정렬할 때 가장 많이 쓴다. `key`에 넘긴 함수의 반환값을 기준으로 비교.
```python
people = [("Kim", 25), ("Lee", 30), ("Park", 20)]
people.sort(key=lambda x: x[1])          # 나이 기준 오름차순
```

### 상황 C: 여러 기준으로 정렬 (1순위 다음 2순위)
튜플은 앞 요소부터 순서대로 비교되므로, key가 튜플을 반환하면 자동으로 다중 기준이 된다.
```python
people.sort(key=lambda x: (-x[1], x[0]))  # 나이 내림차순, 같으면 이름 오름차순
```

### 상황 D: 문자열을 "숫자처럼" 비교하고 싶을 때 vs "이어붙인 결과"로 비교할 때
"가장 큰 수" 유형의 핵심. 단순 문자열 사전순 정렬은 틀린다 — 이어붙였을 때 더 큰 쪽이
앞으로 오게 비교해야 한다.
```python
from functools import cmp_to_key
def compare(a, b):
    if a + b > b + a: return -1   # a가 앞에 와야 더 큰 수
    elif a + b < b + a: return 1
    return 0
arr_str = list(map(str, arr))
arr_str.sort(key=cmp_to_key(compare))
```

### 상황 E: 정렬은 하되 원래 인덱스도 알아야 할 때
```python
indexed = sorted(enumerate(arr), key=lambda x: x[1])  # (원래인덱스, 값) 쌍으로 정렬
```

## 3. 자주 하는 실수
- 문자열 숫자를 그냥 `sort()` — "10"이 "9"보다 사전순으로 앞에 옴. 숫자 비교가 필요하면
  `int()` 변환하거나 상황 D처럼 비교 함수를 직접 정의
- `key=lambda x: -x`로 내림차순을 흉내내다 음수 처리를 깜빡함 — 그냥 `reverse=True` 사용
- `sort()`의 반환값(`None`)을 변수에 저장하려다 버그 — `sort()`는 제자리 정렬, `sorted()`가 반환

## 4. Python 잡기술
- `sort()`는 안정 정렬(stable) — 같은 키를 가진 원소들의 상대 순서가 유지됨. 다단계 정렬에서
  뒤 기준부터 여러 번 `sort()`를 걸어도 안전한 이유
- `min(arr, key=...)`, `max(arr, key=...)` — 전체를 정렬하지 않고 기준값만 필요할 때 더 빠름
