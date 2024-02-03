T = int(input())
for _ in range(T):
  N = int(input())
  stocks = list(map(int, input().split()))
  
  profit = 0
  max_price = 0
  for i in range(len(stocks)-1, -1, -1):
    if stocks[i] > max_price:
      max_price = stocks[i]
    else:
      profit += max_price - stocks[i]
  print(profit)