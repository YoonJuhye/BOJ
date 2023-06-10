N = int(input())
score = []
for _ in range(N):
    name, kor, eng, math = map(str, input().split())
    score.append([name,int(kor),int(eng),int(math)])

score = sorted(score, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(score[i][0])