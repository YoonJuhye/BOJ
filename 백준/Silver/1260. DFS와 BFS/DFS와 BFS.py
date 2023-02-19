from collections import deque

def dfs(v):
  visitedDfs[v] = True
  print(v, end=" ")
  for i in graph[v]:
    if visitedDfs[i] == False:
      visitedDfs[i] = True
      dfs(i)

def bfs(v):
  q = deque([v])
  visitedBfs[v] = True
  while q:
    v = q.popleft()
    print(v, end=" ")
    for i in graph[v]:
      if visitedBfs[i] == False:
        visitedBfs[i] = True
        q.append(i)

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
  x, y = map(int, input().split())

  graph[x].append(y)
  graph[y].append(x)
  for i in range(N + 1):
    graph[i] = sorted(graph[i])

visitedDfs = [False] * (N+1)
visitedBfs = [False] * (N+1)

dfs(V)
print()
bfs(V)

