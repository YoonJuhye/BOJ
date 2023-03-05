N = int(input())
cnt = 0
num = N
while True:
    A = num // 10
    B = num % 10
    num = (B*10) + (A + B)%10
    cnt += 1
    if num == N:
        break
print(cnt)