# 피로도 시스템
# 현재 남은 피로도 k >= 최소 필요 피로도 
# 소모 피로도 - 던전 탐험 후 소모되는 양
# return 하루에 최대한 많이 탐험할 수 있는 던전 수
# [최소 필요 피로도, 소모 피로도]
# 1-2-3 1-3-2 2-1-3 2-3-1 3-1-2 3-2-1

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    seq = [n for n in range(len(dungeons))]
    
    lst = []
    for i in permutations(seq, len(dungeons)):
        lst.append(list(i))
    maxCnt = 0
    for j in lst:
        minK = k
        cnt = 0
        for l in j:
            if minK >= dungeons[l][0]:
                cnt += 1
                minK -= dungeons[l][1]
            else:
                continue
        maxCnt = max(cnt, maxCnt)
    return maxCnt