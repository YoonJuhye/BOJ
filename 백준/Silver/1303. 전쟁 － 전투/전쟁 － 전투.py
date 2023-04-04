from collections import deque
N, M = map(int, input().split())
color = [list(map(str, input().rstrip())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

def bfs(i, j, col, cnt):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for dx, dy in [[0,1], [0,-1],[1,0],[-1,0]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<M and 0<=ny<N and visited[nx][ny] == False:
                if color[nx][ny] == col:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt
       
w_res, b_res = 0, 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == False:
          w_cnt, b_cnt = 1, 1
          if color[i][j] == 'W':
              w_cnt = bfs(i, j, 'W', w_cnt)
              w_res += w_cnt**2
          elif color[i][j] == 'B':
              b_cnt = bfs(i, j, 'B', b_cnt)
              b_res += b_cnt**2
print(w_res,b_res)