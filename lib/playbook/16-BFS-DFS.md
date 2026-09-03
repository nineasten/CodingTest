# BFS · DFS

## 1. 언제 이 기술인가 — 문제 속 신호
"최단 경로/최단 시간", "연결된 영역/네트워크 개수", "도달 가능한지", "모든 경우의 수를
가지치기하며 탐색" — 최단거리는 **BFS**, 모든 경로/조합을 다 봐야 하면 **DFS**가 기본.

## 2. 상황별 한국어 설명 + 예시 코드

### 상황 A: 최단 거리/최소 횟수 (BFS)
그래프/격자에서 "몇 번 만에 도달하는가"는 항상 BFS. 큐에서 꺼낸 순서가 곧 최단 거리
순서이기 때문에, 처음 방문하는 순간의 깊이가 곧 최단 거리다.
```python
from collections import deque
def bfs(start):
    q = deque([start])
    dist = {start: 0}
    while q:
        cur = q.popleft()
        for nxt in neighbors(cur):
            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist
```

### 상황 B: 연결된 요소(컴포넌트) 개수 세기 (네트워크류)
전체를 순회하며 안 가본 노드를 시작점으로 BFS/DFS를 한 번씩 돌리고, 돌린 횟수가 곧
컴포넌트 개수.
```python
visited = set()
count = 0
for node in all_nodes:
    if node not in visited:
        count += 1
        dfs(node, visited)   # 이 컴포넌트 전체를 방문 처리
```

### 상황 C: 모든 조합/경로를 만들어야 할 때 (DFS + 백트래킹)
"타겟 넘버"류 — 각 갈림길에서 선택지를 하나씩 시도하고, 끝까지 가면 되돌아온다(재귀의
자연스러운 특성). 백트래킹 노트(17번)와 겹치는 영역.
```python
def dfs(idx, total):
    if idx == len(arr):
        if total == target:
            nonlocal count
            count += 1
        return
    dfs(idx+1, total + arr[idx])
    dfs(idx+1, total - arr[idx])
```

### 상황 D: 격자 위에서의 BFS/DFS
방향벡터·범위체크는 11번(2D격자) 노트를 그대로 쓴다. 이 노트에선 탐색 로직 자체에 집중.

### 상황 E: 인접 리스트로 그래프 표현하기
간선 리스트를 받으면 인접 리스트로 변환해두는 게 탐색을 빠르게 한다.
```python
from collections import defaultdict
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)   # 무방향 그래프면 양쪽 다
```

## 3. 자주 하는 실수
- 최단 거리 문제에 DFS를 써서 최단이 아닌 아무 경로나 찾아버림 — **최단 거리는 무조건 BFS**
- `visited` 체크를 큐에 **넣을 때**가 아니라 **꺼낼 때** 함 — 같은 노드가 큐에 중복으로
  쌓여 비효율(정답은 맞을 수 있어도 느려짐). 넣는 순간 바로 visited 처리할 것
- 재귀 DFS에서 종료 조건을 빼먹어 무한 재귀

## 4. Python 잡기술
- DFS는 재귀 대신 스택으로도 구현 가능 (재귀 깊이 제한 걱정될 때)
- `functools.lru_cache`를 DFS에 씌우면 같은 상태를 다시 안 계산 (메모이제이션, DP 20번과 연결)
