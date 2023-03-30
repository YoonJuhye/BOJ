N, M = map(int, input().split())
seq = list(map(int, input().split()))
tap = []
cnt = 0
for i in range(M):
    if seq[i] in tap: # 탭에 있으면 건너뜀
        continue
    if len(tap) < N: # 탭에 다 꽂히기 전
        tap.append(seq[i])
        continue
    inIdx = 0
    out = 0
    for j in range(N):
        if tap[j] not in seq[i:]: # 뒤에 겹치는 게 없는 플러그면 해당 플러그 아웃해야함
            out = j
            break
        elif seq[i:].index(tap[j]) > inIdx:
            inIdx = seq[i:].index(tap[j])
            out = j
    tap[out] = seq[i]
    cnt += 1
print(cnt)