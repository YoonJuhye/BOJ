winner = 0
maxV = 0
for i in range(1, 6):
  sumV = sum(list(map(int, input().split())))
  if sumV > maxV:
    maxV = sumV
    winner = i
print(winner, maxV)