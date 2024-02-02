N, K = map(int, input().split())

height = list(map(int, input().split()))
height.sort()

st = []
for i in range(1, N):
  st.append(height[i] - height[i-1])

st.sort()
print(sum(st[:N-K]))