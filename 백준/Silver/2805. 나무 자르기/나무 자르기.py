N, M = map(int, input().split())
height = sorted(list(map(int, input().split())))

start = 0
end = max(height)
result = 0
while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in height:
        if i > mid:
          total += i - mid
    if total < M: # 덜 잘랐으면 더 잘라야 함 왼쪽 부분 탐색
        end = mid - 1
    else: # 더 많이 잘랐으면 덜 잘라야 함
        result = mid
        start = mid + 1
print(result)