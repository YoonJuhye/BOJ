K = int(input())

graph = []
x = []
y = []
for i in range(6):
  d, l = map(int, input().split())
  if d == 1 or d == 2:
    x.append(l)
  elif d == 3 or d == 4:
    y.append(l)
  graph.append([d,l])
graph *= 2
max_x = max(x)
max_y = max(y)

min_1 = 0
min_2 = 0
for i in range(11):
  # 두번 전이 같으면서, 한번 앞뒤가 같은지 체크
  if graph[i][0] == graph[i-2][0] and graph[i-1][0] == graph[i+1][0]:
    min_1 = graph[i-1][1]
    min_2 = graph[i][1]
    break
res= ((max_x*max_y) - abs(min_1*min_2))*K
print(res)