from collections import deque
R, C = map(int, input().split())
field = [list(map(str, input().rstrip())) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

def bfs(x, y):
    global k_cnt, v_cnt
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        if field[x][y] == 'v':
            v_cnt += 1
        elif field[x][y] == 'k':
            k_cnt += 1
        for dx, dy in [[0, 1],[0,-1],[1,0],[-1,0]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<R and 0<=ny<C and field[nx][ny] != '#' and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
k_res = 0
v_res = 0
for i in range(R):
    for j in range(C):
        if field[i][j] != '#' and visited[i][j] == False:
            k_cnt = 0
            v_cnt = 0
            bfs(i,j)
            if k_cnt <= v_cnt:
                k_cnt = 0
            else:
                v_cnt = 0
            k_res += k_cnt
            v_res += v_cnt
          
print(k_res, v_res)