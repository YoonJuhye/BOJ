import sys
sys.setrecursionlimit(100000)
n = int(input())
arr = ['0', '1', '2']
cnt = 0

def dfs(depth, a):
  global cnt
  for i in arr:
    if i == '0' and depth == 0:
      continue
    if depth == n:
      if a % 3 == 0:
        cnt += 1
        return cnt
    else:
      dfs(depth+1, int(str(a)+i))
  
dfs(0, 0)
print(cnt)