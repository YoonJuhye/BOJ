import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(n)]

def bfs(i, j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    maxV = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1,0], [0,-1], [-1,0]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='L' and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] +1
                maxV = max(maxV, visited[nx][ny])
    return maxV -1
res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[0]*m for _ in range(n)]
            res = max(res, bfs(i,j))
print(res)