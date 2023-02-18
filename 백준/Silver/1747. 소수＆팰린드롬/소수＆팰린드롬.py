import math

def isPrime(x):
  if x == 1:
    return False
  for i in range(2, int(math.sqrt(x)+1)):
    if x % i == 0:
      return False
  return True

res = int(input())
ck = 0

while True:
  if isPrime(res) and str(res) == str(res)[::-1]:
    print(res)
    break
  res += 1