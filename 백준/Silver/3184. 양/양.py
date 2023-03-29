from collections import deque
R, C = map(int, input().split())
field = [list(map(str, input().rstrip())) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
def bfs(x, y):
  global o_cnt, v_cnt
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    if field[x][y] == 'o':
      o_cnt += 1
    elif field[x][y] == 'v':
      v_cnt += 1
    for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
      nx = x + dx
      ny = y + dy
      if 0<=nx<R and 0<=ny<C and field[nx][ny] != '#' and visited[nx][ny] == False:
        q.append((nx,ny))
        visited[nx][ny] = True

o_res, v_res = 0, 0
for i in range(R):
  for j in range(C):
    if field[i][j] != '#' and visited[i][j] == False:
      o_cnt, v_cnt = 0, 0
      bfs(i, j)
      if o_cnt > v_cnt:
        v_cnt = 0
      else:
        o_cnt = 0
      o_res += o_cnt
      v_res += v_cnt
print(o_res, v_res)