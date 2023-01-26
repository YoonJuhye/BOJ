lst = [n for n in range(9)]

for i in range(1, 9):
  n = int(input())
  lst[i] = n
rst = sorted(lst)
print(sum(rst[4:9]))
idx = []
for i in rst[4:9]:
  idx.append(lst.index(i))
res = sorted(idx)
for i in res:
  print(i, end=' ')