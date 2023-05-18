N = str(input())
length = len(N)
left = 0
right = 0
for i in range(length//2):
    left += int(N[i])
    
for j in range(length//2, length):
    right += int(N[j])

if left == right:
    print("LUCKY")
else:
    print("READY")