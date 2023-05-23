from collections import deque

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

N, K = map(int, input().split())
graph = []
virus = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j, 0))

S, X, Y = map(int, input().split())

virus.sort()
q = deque(virus)
while q:
    num, x, y, cnt = q.popleft()
    if cnt == S:
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0:
            graph[nx][ny] = num
            q.append((graph[nx][ny], nx, ny, cnt+1))
print(graph[X-1][Y-1])