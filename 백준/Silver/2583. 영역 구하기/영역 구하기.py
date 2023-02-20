import sys
sys.setrecursionlimit(100000)

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for _ in range(K):
  a, b, c, d = map(int, input().split())
  for i in range(b, d):
    for j in range(a, c):
      graph[i][j] = 1


def dfs(x, y):
  global cnt
  graph[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<M and 0<=ny<N and graph[nx][ny] != 1:
      cnt += 1
      dfs(nx, ny)

cnt = 1
res = []

for i in range(M):
  for j in range(N):
    if graph[i][j] != 1:
      dfs(i, j)
      res.append(cnt)
      cnt = 1

print(len(res))
print(*sorted(res))