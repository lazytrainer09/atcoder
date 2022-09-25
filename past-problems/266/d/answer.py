N = int(input())

times = []
for _ in range(N):
    times.append(list(map(int, input().split())))

max_t = times[N-1][0]

dp = [[0]*5 for _ in range(max_t+1)]

t_idx = 0
for i in range(max_t):
    flag = False
    if times[t_idx][0] == i+1:
        flag = True
        t, x, a = times[t_idx]
        t_idx += 1

    for j in range(5):
        if i+1 < j:
            break

        # 移動しないとき
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])

        # −1移動するとき
        if j >= 1:
            dp[i+1][j-1] = max(dp[i][j], dp[i+1][j-1])

        # +1移動するとき
        if j < 4:
            dp[i+1][j+1] = max(dp[i][j], dp[i+1][j+1])

    if flag and i+1 >= x:
        dp[i+1][x] += a

print(max(dp[-1]))
