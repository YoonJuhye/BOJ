n = int(input())
stack = list(i for i in range(1, n+1))

out = []
while len(stack) > 1:
  out.append(stack[0])
  stack = stack[1:]
  a = stack[0]
  stack = stack[1:]
  stack.append(a)

print(*out, *stack)