import sys, math
input = sys.stdin.readline
N, L = map(int, input().split())
pools = [list(map(int,input().split())) for _ in range(N)]
pools.sort()

cnt = 0 # 널빤지 개수
flag = pools[0][0] # 마지막으로 덮어진 웅덩이 위치
for start, end in pools:
  if flag > end:
    continue
  elif flag < start:
    flag = start
  d = math.ceil((end - flag) / L)
  flag += d*L
  cnt += d

print(cnt)