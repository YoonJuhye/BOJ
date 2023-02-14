N, L = map(int, input().split())
water = list(map(int, input().split()))
waterS = sorted(water)
cnt = 1
start = waterS[0] - 0.5
end = start + L
for i in range(1, N):
  if start < waterS[i] < end:
    continue
  else:
    cnt += 1
    start = waterS[i] - 0.5
    end = start + L
print(cnt)