N = int(input())
A = list(map(int, input().split()))

C = [0] * (N + 1)
for x in A:
    C[x] += 1

ans = 0
for i in range((N + 1) // 2):
    L = A[i]
    R = A[~i]
    ans += (N - 2 * i - C[L]) * (i + 1)
    ans += (N - 2 * i - C[R]) * (i + 1)
    if L != R:
        ans -= i + 1
    C[L] -= 1
    C[R] -= 1

print(ans)
