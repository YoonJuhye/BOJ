from collections import deque

def dfs(v):
  visitedDfs[v] = True
  print(v, end=" ")
  for i in range(1, N+1):
    if visitedDfs[i] == False and graph[v][i] == 1:
      visitedDfs[i] = True
      dfs(i)


def bfs(v):
  q = deque([v])
  visitedBfs[v] = True
  while q:
    v = q.popleft()
    print(v, end=" ")
    for i in range(1, N+1):
      if visitedBfs[i] == False and graph[v][i] == 1:
        visitedBfs[i] = True
        q.append(i)

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1

visitedDfs = [False] * (N+1)
visitedBfs = [False] * (N+1)

dfs(V)
print()
bfs(V)

