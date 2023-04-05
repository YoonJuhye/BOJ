import sys
input = sys.stdin.readline
N = int(input())
meets = [list(map(int, input().split())) for _ in range(N)]
meets.sort(key=lambda x: (x[1],x[0]))

cnt = 1
end = meets[0][1]

for i in range(1, N):
    if end <= meets[i][0]:
        end = meets[i][1]
        cnt += 1
print(cnt)