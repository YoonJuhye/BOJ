X = int(input())
rod_sum = 64
cnt = 0
while X > 0:
    if rod_sum > X:
        rod_sum //= 2
    else:
        cnt += 1
        X -= rod_sum
print(cnt)