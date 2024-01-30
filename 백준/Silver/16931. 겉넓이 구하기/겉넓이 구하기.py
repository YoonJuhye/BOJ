n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
  cur = 0
  for j in range(m):
    if box[i][j] != 0:
      cnt += 2
    if box[i][j] > cur:
      cnt += (box[i][j] - cur)
    cur = box[i][j]

for j in range(m):
  cur = 0
  for i in range(n):
    if box[i][j] > cur:
      cnt += (box[i][j] - cur)
    cur = box[i][j]

for i in range(n):
  cur = 0
  for j in range(m-1, -1, -1):
    if box[i][j] > cur:
      cnt += (box[i][j] - cur)
    cur = box[i][j]

for j in range(m):
  cur = 0
  for i in range(n-1, -1, -1):
    if box[i][j] > cur:
      cnt += (box[i][j] - cur)
    cur = box[i][j]

print(cnt)