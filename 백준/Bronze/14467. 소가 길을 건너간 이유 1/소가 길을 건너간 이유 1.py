N = int(input())
cnt = 0
cow = [-1] * 11
for _ in range(N):
  num, cross = map(int, input().split())
  if cow[num] == -1:
    cow[num] = cross
  elif cow[num] != cross:
    cow[num] = cross
    cnt += 1
print(cnt)