N = int(input())
lst = []
for _ in range(N):
    lst.append(input())

idx1 = lst.index("KBS1")
idx2 = lst.index("KBS2")

if idx1 > idx2:
    idx2 += 1

print('1'*idx1 + '4'*idx1 + '1'*idx2+ '4'*(idx2-1))