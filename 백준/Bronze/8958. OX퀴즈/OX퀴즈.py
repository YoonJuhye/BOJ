T = int(input())
for _ in range(T):
    quiz = str(input())
    cnt = [0] * len(quiz)
    if quiz[0] == 'O':
        cnt[0] += 1
    for i in range(1, len(quiz)): 
        if quiz[i] == 'O':
            if quiz[i] == quiz[i-1]:
                cnt[i] = cnt[i-1] + 1
            else:
                cnt[i] += 1
    print(sum(cnt))