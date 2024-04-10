'''
bandage = [t, x, y]
attack = [공격 시간, 피해량]
t초 x 만큼 회복
연속성공시간: t초 y 만큼 회복, 공격 시 0 초기화
time = 0 , 
    if attack[0]-time-1 >= t:
        health += y*((attack[0]-time-1) // t), 
    time=attack[0] 
    health -= attack[1]
health <= 0 - 죽음 : return -1 
return 끝 생존 여부
'''
def solution(bandage, health, attacks):
    answer = health
    time = 0
    for attack in attacks:
        print(time, answer)
        if answer <= 0:
            return -1
        if attack[0]-time-1 >= bandage[0]:
            answer += bandage[2]*((attack[0]-time-1) // bandage[0])
        answer += (attack[0]-time-1)*bandage[1]
        if answer > health:
                answer = health
        time = attack[0] 
        answer -= attack[1]
    print(time, answer)
    if answer <= 0:
        return -1
    return answer