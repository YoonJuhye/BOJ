S = str(input())
T = str(input())

while (T != S):
  if len(T) <= len(S) and T != S:
    break
  if T[-1] == 'A':
    T = T[:len(T)-1]
  elif T[-1] == 'B':
    T = T[len(T)-2::-1]

if T == S:
  print(1)
else:
  print(0)