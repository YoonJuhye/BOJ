import sys
def back_tracking(cnt, idx):
    if cnt == l:
        cnt_a, cnt_b = 0, 0
        for i in arr:
            if i in ['a', 'e','i','o','u']:
                cnt_a += 1
            else:
                cnt_b += 1
        if cnt_a >= 1 and cnt_b >=2:
            print("".join(arr))
        return
    for i in range(idx, c):
        arr.append(array[i])
        back_tracking(cnt + 1, i + 1)
        arr.pop()


l, c = map(int, sys.stdin.readline().split())
array = sorted(list(map(str, sys.stdin.readline().split())))
arr = []
back_tracking(0, 0)