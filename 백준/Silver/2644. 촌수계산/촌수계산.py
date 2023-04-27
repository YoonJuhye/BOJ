n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
cnt = [0] * (n+1)
def dfs(v):

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            cnt[i] = cnt[v] + 1
            dfs(i)
dfs(a)
if cnt[b] != 0:
    print(cnt[b])
else:
    print(-1)