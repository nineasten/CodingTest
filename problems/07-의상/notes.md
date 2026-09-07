# [42578] 의상 — 노트

- 난이도: Lv.2 | 유형: 해시
- 결과: 통과 (리팩토링 학습)
- 핵심: Counter로 종류별 카운트 + 경우의 수 곱셈

## 학습한 관용구

### Counter로 종류별 개수 세기
```python
from collections import Counter
counter = Counter(sort for _, sort in clothes)
# clothes = [["name1", "type1"], ["name2", "type1"], ...]
# counter = Counter({'type1': 2, 'type2': 1, ...})
```
- `counter` = 딕셔너리처럼 보이지만 개수 센 객체
- `counter.values()` = 각 종류의 개수 [2, 1, ...]
- `counter['type1']` = 2 (type1의 개수)

### reduce로 연속 곱셈
```python
from functools import reduce
from operator import mul

reduce(mul, [3, 2, 1])  # 3 * 2 * 1 = 6
# 단계: mul(3,2)=6 → mul(6,1)=6

# 의상에서: 
reduce(mul, (c+1 for c in counter.values())) - 1
# (headgear 2+1) * (eyewear 1+1) - 1 = 3*2-1 = 5
```
- `reduce(함수, 시퀀스)` = 왼쪽부터 차례로 적용
- 코딩테스트에선 루프가 더 읽기 쉬움

### 언팩에서 불필요한 값은 `_` 사용
```python
for _, sort in clothes:  # 이름은 안 씀, 종류만 필요
```

## 개선 전후
**Before (내 풀이)**
```python
result = 1
for num in [len(x) for x in menu.values()]:
    result *= num + 1
return result - 1
```

**After (리팩토링)**
```python
from collections import Counter
from functools import reduce
from operator import mul

counter = Counter(sort for _, sort in clothes)
return reduce(mul, (c+1 for c in counter.values())) - 1
```

둘 다 O(N)이지만, 이름을 저장할 필요가 없으니 Counter가 더 직관적.
