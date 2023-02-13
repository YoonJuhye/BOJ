T = int(input())
for _ in range(T):
  N = int(input())
  rank = [list(map(int, input().split())) for _ in range(N)]
  rank_s = sorted(rank)
  cnt = 1
  minV = rank_s[0][1]
  for i in range(1, N):
    if rank_s[i][1] < minV:
      minV = rank_s[i][1]
      cnt += 1
  print(cnt)