def balance(array): # 균형잡힌 괄호 문자열 검사
    left = 0
    for i in range(len(array)):
        if array[i] == '(':
            left += 1
        else:
            left -= 1
        if left == 0:
            return i
            

def good(array): # 올바른 괄호 문자열 검사
    st = []
    for i in range(len(array)):
        if array[i] == '(':
            st.append(array[i])
        elif array[i] == ')':
            if len(st) != 0:
                st.pop()
            else:
                return False
    if len(st) == 0:
        return True
    return False

def solution(p):
    answer = ''
    if good(p):
        return p
    idx = balance(p)
    u = p[0:idx+1]
    v = p[idx+1:]
    if good(u) == True: # 올바른 문자열이면
        answer = u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        temp = u[1:-1]
        u = ''
        for i in range(len(temp)):
            if temp[i] == '(':
                u += ')'
            else:
                u += '('
        answer += u
    return answer