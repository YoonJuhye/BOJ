import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

lst = []
def per(arr, c):
    if arr:
        for i in range(N-len(c)):
            tmp = list(c)
            tmp.append(arr[i])
            new_arr = arr[:i] + arr[i+1:]
            per(new_arr, tmp)
    else:
        lst.append(c)

A = sorted(A)
per(A,[])

maxV = 0
for i in lst:
    sumV = 0
    for j in range(1, N):
        sumV += abs(i[j] - i[j-1])
    if maxV < sumV:
        maxV = sumV
print(maxV)