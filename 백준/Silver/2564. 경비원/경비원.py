x, y = map(int, input().split()) # 가로 세로
n = int(input()) # 상점의 개수
# 방향(1:북,2:남:3:서:4:동), 북/남: 왼쪽으로부터 거리, 동/서: 위쪽으로부터 거리
stores = [list(map(int, input().split())) for _ in range(n)]
sd, sl = map(int, input().split()) # 동근이 위치

def dir(i, j):
  if i == 1: # 북
    return j
  elif i == 2: # 남
    return x + y + (x-j)
  elif i == 3: # 서
    return (x + y) * 2 - j
  elif i == 4: # 동
    return x + j

sl = dir(sd, sl)

store = []
for i in range(n):
  d = dir(stores[i][0], stores[i][1])
  store.append(d)

for k in range(n):
  clock = abs(store[k]-sl)
  op_clock = (x+y) * 2 - clock
  store[k] = min(clock, op_clock)
print(sum(store))