N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    for a in A:
        if i - a < 0:
            continue
        dp[i] = max(dp[i], a + (i - a - dp[i - a]))

print(dp[N])
