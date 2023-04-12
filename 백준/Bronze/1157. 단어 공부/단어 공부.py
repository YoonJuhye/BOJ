N = input().lower()
alphabet = list(range(97,123))
cnt = [0] * len(alphabet)
for i in N:
    idx = alphabet.index(ord(i))
    cnt[idx] += 1
res = ""
maxV = 0
for i in range(len(cnt)):
    if cnt[i] != 0: 
        if cnt[i] > maxV:
          maxV = cnt[i]
          res = chr(alphabet[i])
        elif cnt[i] == maxV:
            res = "?"
print(res.upper())