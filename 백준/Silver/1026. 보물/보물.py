N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sortA = sorted(A)
sortB = sorted(B)

S = 0
for i in range(N):
  S += sortA[i] * sortB[N-i-1]
print(S)