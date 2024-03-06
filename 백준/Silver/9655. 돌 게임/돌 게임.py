n = int(input())
cnt = 0
while n > 0:
  if n-3 >= 0:
    n -= 3
    cnt += 1
  else:
    n -= 1
    cnt += 1

if cnt % 2:
  print('SK')
else:
  print('CY')