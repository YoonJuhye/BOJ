n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
# 사과의 위치
board = [[0]*(n) for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = -1

rot = []
l = int(input()) # 방향 변환 횟수
for _ in range(l):
    x, c = map(str, input().split()) # 방향 변환 정보 x초 후 왼쪽:L 오른쪽:D 90도 회전
    rot.append((int(x), c))

# 방향변환횟수가 나오면 회전함 
# 사과 없으면 이전칸 0으로 만들고
# 사과 있으면 이전칸 냅두고 진행 + 
# 벽 만나면 끝

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def turn(direction, c):
    if c == 'L': # 왼쪽
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction
def move():
    x, y = 0,0
    board[x][y] = 1
    direction = 0
    time = 0
    index = 0
    q= [(x,y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx <n and 0<=ny<n and board[nx][ny] != 1:
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx,ny))
                px, py = q.pop(0) # 제일 처음에 들어간거
                board[px][py] = 0
            if board[nx][ny] == -1:
                board[nx][ny] = 1
                q.append((nx,ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < l and time == rot[index][0]:
            direction = turn(direction, rot[index][1])
            index += 1
    return time
print(move())