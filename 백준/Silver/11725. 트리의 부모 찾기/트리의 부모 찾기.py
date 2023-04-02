import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
def dfs(s):
    for i in graph[s]:
        if visited[i] == False:
            visited[i] = s
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(visited[i])