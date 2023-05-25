N = int(input())
graph = []
teacher = 0
for _ in range(N):
  data = list(input().split())
  teacher += data.count('T')
  graph.append(data)

# 같은 방향으로 쭉 확인하기 dx[0] -> dx[0]으로
dx = [-1, 1, 0,0] # 상하좌우
dy = [0, 0, -1,1]
def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0<=nx<N and 0<= ny <N and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':
                return True # 감시가능
            else:
                nx += dx[i]
                ny += dy[i]
    return False # 감시 불가능

def install(cnt):
    global res
    if cnt == 3:
        teacherCnt = 0
        for a in range(N):
            for b in range(N):
                if graph[a][b] == 'T'and not check(a, b): #감시불가능
                    teacherCnt += 1
        if teacherCnt == teacher:
            res = True
        return res
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                cnt += 1
                install(cnt)
                graph[i][j] = 'X'
                cnt -= 1

res = False
install(0)
if res:
    print('YES')
else:
    print('NO')