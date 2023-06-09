from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (n+1)
visited[x] = 0 
def bfs(x):
    q = deque([x])
    while q:
        i = q.popleft()
        for d in graph[i]:
            if visited[d] == -1:
                visited[d] = visited[i] + 1
                q.append(d)
bfs(x)
check = False
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)