N, K = map(int, input().split()) # 국가 수, 지정국가
nat = [list(map(int, input().split())) for _ in range(N)]


nat_gold = [0]*(N+1)
nat_silver = [0]*(N+1)
nat_bronze = [0]*(N+1)
for i in range(N):
    nat_gold[nat[i][0]] = nat[i][1]
    nat_silver[nat[i][0]] = nat[i][2]
    nat_bronze[nat[i][0]] = nat[i][3]
cnt = 1
for j in range(N+1):
    if j != K:
        if nat_gold[j] > nat_gold[K]:
            cnt += 1
        elif nat_gold[j] == nat_gold[K]:
            if nat_silver[j] > nat_silver[K]:
                cnt += 1
            elif nat_silver[j] == nat_silver[K]:
                if nat_bronze[j] > nat_bronze[K]:
                    cnt += 1
print(cnt)