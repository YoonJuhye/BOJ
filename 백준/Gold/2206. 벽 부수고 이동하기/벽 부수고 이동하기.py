from collections import deque

def bfs(i, j, c):
  q = deque()
  q.append((i, j, c))
  while q:
    x, y, c = q.popleft()
    if x == n-1 and y == m-1:
      return visited[x][y][c]
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
        q.append((nx, ny, c))
        visited[nx][ny][c] = visited[x][y][c] + 1
      elif graph[nx][ny] == 1 and c == 0:
        q.append((nx, ny, 1))
        visited[nx][ny][1] = visited[x][y][0] + 1
  return -1

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)]for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
visited[0][0][0] = 1
res = bfs(0,0,0)
print(res)