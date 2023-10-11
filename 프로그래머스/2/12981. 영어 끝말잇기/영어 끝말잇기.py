def solution(n, words):
    answer = [0,0]
    num = 0
    order = 0
    for i in range(1, len(words)):
        # 이전 등장 단어 or 마지막문자 시작 아닌 단어
        if words[i] in words[:i] or words[i][0] != words[i-1][-1]:
            num = (i%n)+1
            order = i//n + 1
            answer = [num, order]
            break
    return answer