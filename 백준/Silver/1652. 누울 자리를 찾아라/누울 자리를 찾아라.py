N = int(input())
room = [list(input()) for _ in range(N)]

ableCnt = 0
sleepXCnt = 0
sleepYCnt = 0
for i in range(N):
    ableCnt = 0
    for j in range(N):
        if room[i][j] != 'X':
            ableCnt += 1
        else:
            ableCnt = 0 
        if ableCnt == 2:
            sleepXCnt += 1


for j in range(N):
    ableCnt = 0
    for i in range(N):
        if room[i][j] != 'X':
            ableCnt += 1
        else:
            ableCnt = 0
        if ableCnt == 2:
            sleepYCnt += 1


print(sleepXCnt, sleepYCnt)