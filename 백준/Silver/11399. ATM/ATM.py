N = int(input())
P = list(map(int, input().split()))
sortP = sorted(P)

sumLst = [0] * N
sumLst[0] = sortP[0]
for i in range(1, len(sortP)):
  sumLst[i] = sumLst[i-1] + sortP[i]
print(sum(sumLst))