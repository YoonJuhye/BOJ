import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

n = int(input())
jump = list(map(int, input().split()))
s = int(input())
visited = [0]*n
cnt = 1

def dfs(x):
    global cnt
    for newS in (x+jump[x], x-jump[x]):
        if 0 <= newS < n and visited[newS] == 0:
            cnt += 1
            visited[newS] = 1
            dfs(newS)
        
dfs(s-1)
print(cnt)