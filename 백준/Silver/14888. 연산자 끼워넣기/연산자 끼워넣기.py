import sys
input = sys.stdin.readline

from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
cel = list(map(int, input().split()))

temp = []
for _ in range(cel[0]):
    temp.append('+')
for _ in range(cel[1]):
    temp.append('-')
for _ in range(cel[2]):
    temp.append('*')
for _ in range(cel[3]):
    temp.append('//')

minV = 1e9
maxV = -1e9
for per in permutations(temp, len(temp)):
    res = num[0]
    for i in range(1, N):
        if per[i-1] == '+':
            res += num[i]
        elif per[i-1] == '-':
            res -= num[i]
        elif per[i-1] == '*':
            res *= num[i]
        elif per[i-1] == '//':
            if res <0:
                res = str(res)
                res =int(res[1:])
                res //= num[i]
                res = -res
            else:
                res //= num[i]
    minV = min(res, minV)
    maxV = max(res, maxV)

print(maxV)
print(minV)