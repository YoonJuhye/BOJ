from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]

def bfs(i, j):
  q = deque()
  q.append((i,j))
  while q:
    i, j = q.popleft()
    for d in range(4):
      nx = i + dx[d]
      ny = j + dy[d]
      if 0<=nx<N and 0<=ny<M and miro[nx][ny]==1:
        q.append((nx, ny))
        miro[nx][ny] = miro[i][j] + 1
  return miro[N-1][M-1]

print(bfs(0,0))