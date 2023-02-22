from collections import deque
N = int(input())
art = [list(input()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
cnt = 0
def bfs(si, sj):
  global cnt
  q = deque()
  q.append((si,sj))
  visited[si][sj] = True
  while q:
    i, j = q.popleft()
    for di, dj in [(-1,0),(0,1),(1,0),(0,-1)]:
      ni = i + di
      nj = j + dj
      if 0<=ni<N and 0<=nj<N and visited[ni][nj]==False:
        if art[ni][nj] == art[i][j]:
          q.append((ni,nj))
          visited[ni][nj] = True

for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      bfs(i,j)
      cnt += 1

cnt_c = 0
visited = [[False]*N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if art[i][j] == 'R':
      art[i][j] = 'G'
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      bfs(i, j)
      cnt_c += 1
print(cnt, cnt_c)