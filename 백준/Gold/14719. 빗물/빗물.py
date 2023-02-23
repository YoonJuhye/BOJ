import sys
input = sys.stdin.readline
H, W = map(int, input().split())
high = list(map(int, input().split()))

cnt = 0
for i in range(1, len(high)-1):
  left_max = max(high[:i])
  right_max = max(high[i+1:])
  wall = min(left_max, right_max)
  if high[i] < wall:
    cnt += wall - high[i]

print(cnt)