import math

t = int(input())
for _ in range(t):
  n, *lst = list(map(int, input().split()))
  sumV = 0
  for i in range(len(lst)):
    for j in range(i+1, len(lst)):
      sumV += math.gcd(lst[i], lst[j])
  
  print(sumV)