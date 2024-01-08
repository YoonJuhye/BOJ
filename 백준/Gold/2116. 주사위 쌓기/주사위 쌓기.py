n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
dict = {1:6, 2:4, 3:5, 4:2, 5:3, 6:1}
res = 0
for k in range(1,7):
  bottom, top = dice[0][dict[dice[0].index(k)+1]-1], k
  answer = []
  temp = [1, 2, 3, 4, 5, 6]
  temp.remove(top)
  temp.remove(bottom)
  answer.append(max(temp))
  for i in range(1, n):
    for idx, j in enumerate(dice[i]):
      if j == top:
        temp = [1, 2, 3, 4, 5, 6]
        bottom = j
        top = dice[i][dict[idx+1]-1]
        temp.remove(top)
        temp.remove(bottom)
        answer.append(max(temp))
        # print(temp)
        break
      else:
        continue
  if res < sum(answer):
    res = sum(answer)
print(res)