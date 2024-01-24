arr = str(input())
stack = list(arr.split('-'))

answer = []
for i in range(len(stack)):
  s = list(map(int, stack[i].split('+')))
  answer.append(sum(s))
res = answer[0]
for i in range(1, len(answer)):
  res -= answer[i]
print(res)