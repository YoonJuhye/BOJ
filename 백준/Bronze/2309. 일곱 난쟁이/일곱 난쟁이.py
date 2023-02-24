from itertools import combinations

height = []
for _ in range(9):
  height.append(int(input()))

for i in combinations(height, 7):
  if sum(i) == 100:
    res = sorted(i)
    for j in res:
      print(j)
    break