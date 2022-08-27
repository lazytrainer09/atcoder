N = int(input())
a = list(map(int, input().split()))

MOD = 998244353
ans = 0

for div in range(1, N + 1):
    dp = [[[0] * div for _ in range(div + 1)] for _ in range(N + 1)]
    # 先頭からi項目までからj個選んだ時の余りkの個数
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(div+1):
            for k in range(div):
                # i項目を選ばない
                dp[i + 1][j][k] += dp[i][j][k]
                dp[i + 1][j][k] %= MOD

                # 分母より多くなるときは計算しない
                if j == div:
                    continue
                # i項目を選ぶ
                k2 = (k + a[i]) % div
                dp[i + 1][j + 1][k2] += dp[i][j][k]
                dp[i + 1][j + 1][k2] %= MOD

    ans += dp[N][div][0]
    ans %= MOD

print(ans)
