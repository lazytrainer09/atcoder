N, M, K = map(int, input().split())
mod = 998244353

dp = [[0] * (M + 1) for _ in range(N)]

for i in range(1, M + 1):
    dp[0][i] = 1

for i in range(1, N):
    S = [0]
    for j in range(1, M + 1):
        S.append(S[j - 1] + dp[i - 1][j])
        S[j] %= mod

    for j in range(1, M + 1):
        if K == 0:
            dp[i][j] += S[M]
            continue

        if j - K >= 1:
            dp[i][j] += S[j - K] - S[0]
        if j + K <= M:
            dp[i][j] += S[M] - S[j + K - 1]

        dp[i][j] %= mod

print(sum(dp[N - 1]) % mod)
