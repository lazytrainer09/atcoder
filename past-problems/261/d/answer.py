N, M = map(int, input().split())
X = list(map(int, input().split()))

bonus = {}
for _ in range(M):
    c, y = map(int, input().split())
    bonus[c] = y

dp = [[-1] * (N + 1) for _ in range(N + 1)]

dp[0][0] = 0

for i in range(N):
    for j in range(N):
        # i回以上カウンタは大きくならない
        if i < j:
            continue

        # 表を出したとき
        if j + 1 in bonus:
            bonus_yen = bonus[j + 1]
        else:
            bonus_yen = 0

        dp[i + 1][j + 1] = dp[i][j] + X[i] + bonus_yen

        # 裏を出したとき
        dp[i + 1][0] = max(dp[i][j], dp[i + 1][0])

print(max(dp[N]))
