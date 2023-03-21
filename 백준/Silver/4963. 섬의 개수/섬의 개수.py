from collections import deque
def bfs(i, j):
    jido[i][j] = 0
    q = deque()
    q.append([i,j])
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<h and 0<=ny<w and jido[nx][ny]==1:
                jido[nx][ny] =0
                q.append([nx,ny])
while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
      break
  jido = [list(map(int, input().split())) for _ in range(h)]
  dx = [-1, -1, 0, 1, 1, 1, 0, -1]
  dy = [0, 1, 1, 1, 0, -1, -1, -1]

  cnt = 0
  for i in range(h):
      for j in range(w):
          if jido[i][j] == 1:
              bfs(i,j)
              cnt += 1
  print(cnt)