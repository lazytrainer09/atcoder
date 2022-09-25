N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = R * N
current = 0

for i in range(N):
    current = min(current + A[i], L * (i + 1))
    ans = min(ans, current + R * (N - 1 - i))

print(ans)
