n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

cnt = 0
if boxes[0] > cranes[0]:
  print(-1)
  exit()
while len(boxes) > 0:
  for i in range(len(cranes)):
    for j in range(len(boxes)):
      if cranes[i] >= boxes[j]:
        boxes.remove(boxes[j])
        break
  cnt += 1
print(cnt)