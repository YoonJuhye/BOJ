from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

def bfs(s):
  global cnt
  q = deque()
  q.append(s)
  visited = [0] * (n+1)
  visited[s] = 1
  while q:
    x = q.popleft()
    for i in graph[x]:
      if visited[i] == 0:
        q.append(i)
        visited[i] = 1
        cnt += 1

for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

maxCnt = 0
res = []
for i in range(1, n+1):
  cnt = 0
  bfs(i)
  if cnt > maxCnt:
    res = []
    maxCnt = cnt
    res.append(i)
  elif cnt == maxCnt:
    res.append(i)
print(*res)