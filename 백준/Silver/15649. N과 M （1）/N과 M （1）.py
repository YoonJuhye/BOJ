import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
visited = [False] * (N+1)

def dfs():
    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return
    for i in range(1, N+1):
      if visited[i]:
          continue
      visited[i] = True
      lst.append(i)
      dfs()
      lst.pop()
      visited[i] = False

dfs()      