x, y, w, s = map(int, input().split())

sx, sy = 0, 0

line = w * (x+y)
if (x+y) % 2:
  cross = (max(x, y) - 1) * s + w
else:
  cross = max(x, y) * s

all = (min(x,y)*s) + (abs(x-y) * w)

time = min(line, cross, all)
print(time)