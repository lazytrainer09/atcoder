N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())

mod = 998244353

hurdle = set()
for _ in range(M):
    x, y = map(int, input().split())
    hurdle.add((x, y))

dp = []
for _ in range(N + 1):
    arr = []
    for _ in range(N + 1):
        arr.append([0] * (N + 1))
    dp.append(arr)

dp[0][0][0] = 1

for i in range(1, N + 1):
    for x in range(i + 1):
        for y in range(i + 1):
            if x + y > i:
                continue

            z = i - x - y

            a = A * x + C * y + E * z
            b = B * x + D * y + F * z

            if (a, b) in hurdle:
                continue

            # xの操作をしたとき
            if x >= 1:
                dp[i][x][y] += dp[i - 1][x - 1][y]
            # yの操作をしたとき
            if y >= 1:
                dp[i][x][y] += dp[i - 1][x][y - 1]
            # zの操作をしたとき
            dp[i][x][y] += dp[i - 1][x][y]

            dp[i][x][y] %= mod

ans = 0
for x in range(N+1):
    for y in range(N+1):
        ans += dp[N][x][y]
        ans %= mod

print(ans)
