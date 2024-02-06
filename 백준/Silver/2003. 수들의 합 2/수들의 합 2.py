n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right <= n and left <= right:
  sum_value = a[left:right]
  total_value = sum(sum_value)

  if total_value == m:
    cnt += 1
    right += 1
  elif total_value > m:
    left += 1
  else:
    right += 1
print(cnt)