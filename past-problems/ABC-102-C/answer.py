N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(1, N + 1):
    B.append(A[i - 1] - i)
B.sort()

if N % 2 == 0:
    b = (B[N // 2] + B[N // 2 - 1]) // 2
else:
    b = B[N // 2]

ans = 0
for i in range(1, N + 1):
    ans += abs(B[i - 1] - b)

print(ans)
