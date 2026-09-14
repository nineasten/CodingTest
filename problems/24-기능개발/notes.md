# 기능개발(42586) 회고

- 결과: ✅ 통과, 힌트 2/4
- 접근: 각 기능의 완료까지 걸리는 날을 계산 → 누적 최댓값(앞선 기능에 밀리는 것 반영)
  → 같은 값끼리 그룹핑해서 개수 세기
  ```python
  from itertools import groupby, accumulate
  def solution(progresses, speeds):
      times = accumulate(((100-p+s-1)//s for p, s in zip(progresses, speeds)), max)
      return [len(list(g)) for _, g in groupby(times)]
  ```
- 시행착오:
  1. 1차 시도: `q = [x+y for x,y in zip(q, n_dones)]`로 매일 진도를 누적하려 했으나,
     `n_dones`(완료 개수 리스트)를 speed 대신 잘못 사용 — zip이 짧은 쪽 기준으로
     q를 조용히 잘라먹어 반례 발생(빈 리스트 IndexError)
  2. 2차 시도: `(100-x)//y + 1`로 완료일 계산 → 나머지가 0일 때(정확히 나누어떨어짐)
     오프바이원 버그(실제보다 1일 더 크게 계산). 반례: progresses=[95,77], speeds=[1,4]
     → 실제 정답 [1,1]인데 [2] 출력
  3. 최종: 올림 나눗셈 `(100-x+y-1)//y`로 수정 → 통과
- 원인 태그: `#인덱스오프바이원` — 올림 나눗셈에서 나머지 0 케이스를 놓침
- 배운 것: 올림 나눗셈은 `math.ceil` 없이 `(a+b-1)//b`로. `a//b+1`은 나머지 0일 때
  틀림. `itertools.groupby`로 연속 동일값 그룹핑 표준화.
