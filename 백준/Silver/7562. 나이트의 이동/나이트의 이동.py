from collections import deque 

T = int(input())
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(cx, cy, mx, my):
  q = deque()
  q.append([cx, cy])
  pan[cx][cy] = 1
  while q:
    x, y = q.popleft()
    if x == mx and y == my:
      return pan[x][y] -1
    for d in range(8):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0<=nx<l and 0<=ny<l and pan[nx][ny] == 0:
        q.append([nx,ny])
        pan[nx][ny] = pan[x][y] + 1

for _ in range(T):
  l = int(input())
  pan = [[0]*l for _ in range(l)]

  cx, cy = map(int, input().split())
  mx, my = map(int, input().split())
  print(bfs(cx, cy, mx, my))
  


