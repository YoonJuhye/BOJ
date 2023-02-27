N = int(input())
K = 0
cnt = 0
while N >0:
  if N < K:
    K = 1
  N -= K
  K += 1
  cnt += 1
print(cnt-1)