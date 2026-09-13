# BFS · DFS

## 1. 언제 이 기술인가 — 문제 속 신호
"최단 경로/최단 시간", "연결된 영역/네트워크 개수", "도달 가능한지", "모든 경우의 수를
가지치기하며 탐색" — 최단거리는 **BFS**, 모든 경로/조합을 다 봐야 하면 **DFS**가 기본.

## 2. 상황별 한국어 설명 + 예시 코드

### 상황 A: 최단 거리/최소 횟수 (BFS)
5×5 게임 맵에서 시작점 `(0,0)`부터 목표점까지 벽을 피해 이동할 때 "최소 몇 칸을
지나야 하는가"를 구한다고 하자. BFS는 "가까운 칸부터 한 겹씩" 넓혀가며 방문하기
때문에, **어떤 칸을 처음 방문하는 순간의 깊이가 곧 그 칸까지의 최단 거리**가 된다.
DFS로는 어쩌다 먼 길로 먼저 도착할 수 있어 최단 거리가 보장되지 않는다.
```python
from collections import deque
def bfs(start):
    q = deque([start])
    dist = {start: 0}   # dist[state] = start부터 몇 번 만에 도달했는지
    while q:
        cur = q.popleft()
        for nxt in neighbors(cur):
            if nxt not in dist:            # 처음 방문하는 순간 = 최단 거리 확정
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist
```

### 상황 B: 연결된 요소(컴포넌트) 개수 세기 (네트워크류)
컴퓨터 5대가 `[[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,1],[0,0,1,1,1],[0,0,1,1,1]]`처럼
연결돼 있을 때("네트워크"류), 몇 개의 독립된 그룹으로 나뉘는지 구한다고 하자. 전체
컴퓨터를 순서대로 보면서 "아직 한 번도 방문 안 한 컴퓨터"를 만날 때마다, 그 컴퓨터와
연결된 것들을 BFS/DFS로 전부 방문 처리하고 그룹 수를 1 늘린다.
```python
visited = set()
count = 0
for node in range(5):           # 컴퓨터 0~4
    if node not in visited:
        count += 1               # 새로운 그룹 발견
        dfs(node, visited)       # 이 그룹 전체를 방문 처리
# count == 2 (컴퓨터 0,1이 한 그룹 / 2,3,4가 한 그룹)
```

### 상황 C: 모든 조합/경로를 만들어야 할 때 (DFS + 백트래킹)
숫자 `[1,1,1,1,1]`에 `+` 또는 `-`를 하나씩 붙여 만들 수 있는 모든 식 중, 결과가
target(예: 3)이 되는 경우의 수를 구한다고 하자("타겟 넘버"류). 각 숫자마다 "더하는
갈래"와 "빼는 갈래" 두 가지로 갈라지는 걸 재귀로 전부 따라가 본다.
```python
arr = [1, 1, 1, 1, 1]
target = 3
count = 0
def dfs(idx, total):
    global count
    if idx == len(arr):
        if total == target:
            count += 1
        return
    dfs(idx+1, total + arr[idx])   # +1을 선택하는 갈래
    dfs(idx+1, total - arr[idx])   # -1을 선택하는 갈래
dfs(0, 0)   # count == 3
```

### 상황 D: 격자 위에서의 BFS/DFS
방향벡터·범위체크는 11번(2D격자) 노트를 그대로 쓴다. 예를 들어 "게임 맵 최단거리"는
상황 A의 BFS를 격자 위에서 그대로 돌리되, `neighbors(cur)`가 "상하좌우 중 벽이 아닌
칸"으로 바뀔 뿐이다. 탐색 로직 자체는 그래프든 격자든 동일하다.

### 상황 E: 인접 리스트로 그래프 표현하기
간선이 `[(1,2), (1,3), (2,4)]`처럼 리스트로 주어지면, 매번 "1과 연결된 노드가 뭐지?"를
찾으려고 전체 간선 리스트를 훑으면 느리다. 미리 "각 노드에서 갈 수 있는 노드 목록"으로
변환해두면(인접 리스트), 탐색 중엔 바로 `graph[node]`로 이웃을 O(1)에 꺼낼 수 있다.
```python
from collections import defaultdict
edges = [(1,2), (1,3), (2,4)]
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)   # 무방향 그래프면 양쪽 다 등록
# graph[1] == [2, 3], graph[2] == [1, 4]
```

## 3. 자주 하는 실수
- 최단 거리 문제에 DFS를 써서 최단이 아닌 아무 경로나 찾아버림 — **최단 거리는 무조건 BFS**
- `visited` 체크를 큐에 **넣을 때**가 아니라 **꺼낼 때** 함 — 같은 노드가 큐에 중복으로
  쌓여 비효율(정답은 맞을 수 있어도 느려짐). 넣는 순간 바로 visited 처리할 것
- 재귀 DFS에서 종료 조건을 빼먹어 무한 재귀

## 4. Python 잡기술
- DFS는 재귀 대신 스택으로도 구현 가능 (재귀 깊이 제한 걱정될 때)
- `functools.lru_cache`를 DFS에 씌우면 같은 상태를 다시 안 계산 (메모이제이션, DP 20번과 연결)
