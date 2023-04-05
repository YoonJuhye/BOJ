N, K = map(int, input().split())
value = []
for _ in range(N):
    value.append(int(input()))
value = sorted(value, reverse=True)

cnt = 0
for i in value:
    cnt += K // i 
    K %= i
print(cnt)