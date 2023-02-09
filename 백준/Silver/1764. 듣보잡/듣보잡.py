N, M = map(int, input().split())

noLtn = set()
noLk = set()
for i in range(N):
  noLtn.add(input())
for j in range(M):
  noLk.add(input())

result = sorted(list(noLtn&noLk))

print(len(result))
for i in result:
  print(i)