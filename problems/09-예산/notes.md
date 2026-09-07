# [12982] 예산 — 노트

- 난이도: Lv.1 | 유형: 이분탐색
- 결과: 통과 (한 번에 정답)
- 힌트: 0/4

## 핵심 아이디어
오름차순 정렬 후 누적합이 예산을 넘는 순간까지가 답. 실제로는 그리디/누적합
스캔으로 풀었는데, 이분탐색 감각 연습으로 `bisect.bisect_right`를 누적합
배열에 바로 적용하는 버전도 봤음.

```python
from itertools import accumulate
import bisect

def solution(d, budget):
    prefix = list(accumulate(sorted(d)))
    return bisect.bisect_right(prefix, budget)
```

## 스타일
- 디버그용 `print` / 테스트 호출은 제출 전 제거 습관 들이기.
