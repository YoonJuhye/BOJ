import sys
input = sys.stdin.readline
M = int(input())
cup = [0] * 4
cup[1] = 1
tmp = 0
for _ in range(M):
  x, y = map(int, input().split())
  tmp = cup[x] 
  cup[x] = cup[y]
  cup[y] = tmp
print(cup.index(1))