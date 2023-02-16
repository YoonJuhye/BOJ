import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline 

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)] 
visited = [False] * (N+1) 
for _ in range(M): 
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(start):
  visited[start] = True
  for i in graph[start]:
    if visited[i] == False:
      visited[i] = True
      dfs(i)

cnt = 0
for i in range(1, N+1):
  if visited[i] == False:
    cnt += 1
    dfs(i)

print(cnt)