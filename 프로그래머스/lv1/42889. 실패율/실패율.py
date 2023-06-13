    # 1 -> 1 / 8
    # 2 -> 2의 개수 / 7
    # 3 -> 3의 개수 / len(stages) - 첫 3의 인덱스
    # 실패율 = stages에서 해당 stage의 개수 / 첫 해당 stage의 인덱스
    # 없으면 0
    # answer = [스테이지번호, 실패율]

def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        if length == 0:
            fail = 0
        else:
            fail = stages.count(i) / length
        answer.append([i, fail])
        length -= stages.count(i)
    answer = sorted(answer, key= lambda x: x[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer