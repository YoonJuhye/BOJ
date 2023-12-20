def solution(today, terms, privacies):
    answer = []
    today_y, today_m, today_d = map(int, today.split("."))
    today_cnt = (today_y*(12*28))+(today_m*28)+today_d
    n_terms = dict()
    for term in terms:
        t, m = term.split()
        n_terms[t] = int(m)*28
    # print(n_terms)
    for i, privacy in enumerate(privacies):
        info_day, info_t = privacy.split()
        y, m, d = map(int, info_day.split("."))
        info_cnt = (y*(12*28))+(m*28)+d
        if today_cnt >= info_cnt+n_terms[info_t]:
            answer.append(i+1)
    return answer