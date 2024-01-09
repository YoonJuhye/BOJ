n, w, L = map(int, input().split())
truck = list(map(int, input().split()))

bridge = [0] * w # 다리 1단위당 트럭 가능
time = 0 # 소요 시간
while bridge:
    bridge.pop(0) # 1타임 지날때마다 하나씩 빼줌
    if truck:
      if sum(bridge)+truck[0] <= L:
        x = truck.pop(0)
        bridge.append(x)
      else:
        bridge.append(0)
    time += 1
print(time)