from collections import deque 

def bfs(n):

  q = deque()
  q.append(n)
  while q:
    s = q.popleft()
    if s == K:
      return visited[s]

    for nx in [s-1, s+1, 2*s]:
      if 0<= nx <= 100000 and not visited[nx]:
        visited[nx] = visited[s] + 1
        q.append(nx)

N, K = map(int, input().split())

visited = [0 for _ in range(100001)]
print(bfs(N))