n = int(input())
lopes = []
for _ in range(n):
  lope = int(input())
  lopes.append(lope)
lopes.sort()

answer = []
for i in range(n):
  answer.append(lopes[i]*(n-i))
print(max(answer))