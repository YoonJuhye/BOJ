N = int(input())
R = int(input())
recNum = list(map(int, input().split())) # 추천받은 학생 번호
cnt = [0]*101 # 추천 횟수
recPic = [] # 사진틀

for i in range(R):
    if recNum[i] in recPic:
        cnt[recNum[i]] += 1
    else:
        if len(recPic) < N:
            recPic.append(recNum[i])
            cnt[recNum[i]] += 1
        elif len(recPic) >= N:
            picCnt = []
            for j in range(N):
                picCnt.append(cnt[recPic[j]])
            for k in range(N):
                if picCnt[k] == min(picCnt):
                    cnt[recPic[k]] = 0
                    del recPic[k]
                    break
            recPic.append(recNum[i])
            cnt[recNum[i]] += 1

recPic.sort()
print(*recPic)