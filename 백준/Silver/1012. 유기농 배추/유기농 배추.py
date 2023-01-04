# 재귀 limit 설정
import sys
sys.setrecursionlimit(10000)

# 유기농 배추 재배
# 배추 - 해충 
# 상하좌우 인접 배추 해충 O, 이동 가능
# 0:배추 없는 땅, 1:배추 땅

# T:테스트케이스 개수
# 배추밭 M:가로길이, N:세로길이, K:배추 심어져 있는 위치 개수
# 배추의 위치 (X, Y)

# print(최소 해충 수)

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]    

def dfs(x, y):
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M and field[nx][ny]==1:
      field[nx][ny] = -1
      dfs(nx, ny)
      



T = int(input())
for t in range(T):
  M, N, K = map(int, input().split())
  field = list([0]*M for _ in range(N))

  for _ in range(K):
    j, i = map(int, input().split())
    field[i][j] = 1

  cnt = 0
  for x in range(M):
    for y in range(N):
      if field[y][x] == 1:
        dfs(y, x)
        cnt += 1

  print(cnt)

