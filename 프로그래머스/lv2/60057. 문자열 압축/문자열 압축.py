def solution(s):
    answer = 0
    answer = len(s)
    for step in range(1, len(s) // 2 + 1): # 1step부터 절반step까지 압축단위 증가
        result = ""
        prev = s[0:step]
        cnt = 1
        for j in range(step, len(s), step): # step만큼 증가시키며 비교
            if prev == s[j:j+step]:
                cnt += 1
            else:
                result += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j+step] #초기화
                cnt = 1
        result += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(result))
    return answer