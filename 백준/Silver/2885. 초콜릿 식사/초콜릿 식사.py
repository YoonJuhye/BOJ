K = int(input())

i = 1
cnt = 0
while i < K:
    i = i << 1

res = i
while K > 0:
    if K >= i:
        K -= i
    else:
        i //= 2
        cnt += 1
print(res, cnt)