import sys
input = sys.stdin.readline
graph = [list(map(str, input().split())) for _ in range(5)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, word):
    if len(word) == 6:
        if word not in lst:
            lst.append(word)
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, word + graph[nx][ny])

lst = []
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
print(len(lst))