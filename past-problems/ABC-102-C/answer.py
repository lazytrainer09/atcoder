N = int(input())
A = list(map(int, input().split()))

A_dash = []
for i in range(1, N + 1):
    A_dash.append(A[i - 1] - i)
A_dash.sort()

center = N // 2
if N % 2 == 0:
    b = (A_dash[center] + A_dash[center - 1]) // 2
else:
    b = A_dash[center]

ans = 0
for i in range(1, N + 1):
    ans += abs(A[i - 1] - b - i)

print(ans)
