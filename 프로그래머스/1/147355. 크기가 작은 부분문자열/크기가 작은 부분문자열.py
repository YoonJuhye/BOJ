def solution(t, p):
    answer = 0
    # 314 159 2
    n = len(p) # p의 길이
    for i in range(0, len(t)-len(p)+1):
        if int(t[i:i+n]) <= int(p): # t의 부분문자열
            answer += 1
    return answer