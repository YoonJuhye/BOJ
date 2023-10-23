from collections import deque

def solution(maps):
    def bfs(i, j):
        q = deque()
        q.append((i, j))
        visited[i][j] = 1
        while q:
            x, y = q.popleft()
            if x == n-1 and y== m-1:
                return visited[x][y]
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
        return visited[n-1][m-1]
    
    answer = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*(m) for _ in range(n)]
    answer = bfs(0,0)
    print(visited)
    if answer == 0:
        return -1
    return answer