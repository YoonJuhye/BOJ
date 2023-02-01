lst = [list(map(int, input().split())) for _ in range(3)]

cnt = [0] * 3
result = ['D', 'C', 'B', 'A', 'E']
for i in range(3):
  a = sum(lst[i])
  cnt[i] += a
  print(result[cnt[i]])