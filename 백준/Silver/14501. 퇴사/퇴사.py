N = int(input())
day = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i+day[i][0], N+1):
        if dp[j] < dp[i] + day[i][1]:
            dp[j] = dp[i] + day[i][1]
print(dp[-1])