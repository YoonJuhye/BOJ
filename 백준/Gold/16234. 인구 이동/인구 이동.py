from collections import deque
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]



def check(x, y, idx):
    position = [] # 연합 인구 바꿀 좌표
    position.append((x,y))
    q = deque()
    q.append((x,y))
    visited[x][y] = idx
    union_nat = [] # 국경열린 연합 인구
    union_nat.append(graph[x][y])
    while q:
        x, y = q.popleft()
        for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx = x + dx
            ny = y + dy
            if 0<= nx < N and 0<=ny<N and visited[nx][ny] == -1:
                if L<=abs(graph[x][y] - graph[nx][ny])<=R:
                    q.append((nx,ny))
                    visited[nx][ny] = idx
                    union_nat.append(graph[nx][ny])
                    position.append((nx,ny))
    for i, j in position:
        graph[i][j] = sum(union_nat)//len(union_nat)
    return len(union_nat)
    
        
result = 0
while True:
    visited = [[-1]*N for _ in range(N)]
    idx = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                check(i,j, idx)
                idx += 1
    if idx == N*N:
        break
    result += 1
print(result)