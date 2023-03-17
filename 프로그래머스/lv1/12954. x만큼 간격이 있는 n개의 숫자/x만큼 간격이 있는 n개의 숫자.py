def solution(x, n):
    answer = []
    tmp = x
    for _ in range(1, n+1):
        answer.append(x)
        x += tmp
    return answer