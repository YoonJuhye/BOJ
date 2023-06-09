from itertools import combinations 

N, M = map(int, input().split())

chic = []
home = []
for i in range(N):
    city = list(map(int, input().split()))
    for j in range(N):
        if city[j] == 1: #집이면 좌표 추가
            home.append((i,j))
        elif city[j] == 2: # 치킨이면
            chic.append((i,j))

able = list(combinations(chic, M)) # 치킨집 M개 고르기

def get_sum(pos): # 치킨거리 합
    cnt = 0
    for a, b in home:
        minV = 1e9
        for c, d in pos:
            minV = min(minV, abs(a-c)+abs(b-d))
        cnt += minV
    return cnt

cnt = 1e9
for x in able:
    cnt = min(cnt, get_sum(x))

print(cnt)