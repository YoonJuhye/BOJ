s = str(input())
zero = 0
one = 0

if s[0] == '0':
    zero += 1
else:
    one += 1
for i in range(1, len(s)):
    if s[i] != s[i-1]: # 이전 숫자와 다르면 start:i 까지 넣기
        if s[i] == '0':
            zero += 1
        else:
            one += 1
if zero < one:
    print(zero)
else:
    print(one)