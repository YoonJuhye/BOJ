N, M = map(int, input().split())
numlist = list(map(int, input().split()))

sumlist = [0]
sub_sum = 0
for i in numlist:
    sub_sum += i
    sumlist.append(sub_sum)

res = 0 
for i in range(N+1):
    for j in range(i):
        if sumlist[i] - sumlist[j] == M:
            res += 1
print(res)