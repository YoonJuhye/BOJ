from collections import deque

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]
def bfs(i, j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<m and 0<=ny<n and visited[nx][ny] == False and graph[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = True
               
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]

cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] != True:
            bfs(i,j)
            cnt += 1
print(cnt)