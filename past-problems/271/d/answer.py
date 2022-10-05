N, S = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    a, b = cards[i - 1]
    for j in range(1, S + 1):
        if j >= a:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - a])

        if j >= b:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - b])

if dp[N][S] == 0:
    print("No")
    exit()

print("Yes")

cur = S
ans = []
for i in range(N - 1, -1, -1):
    a, b = cards[i]
    if cur >= a and dp[i][cur - a] == 1:
        cur -= a
        ans.append("H")
    else:
        cur -= b
        ans.append("T")

ans.reverse()
print("".join(ans))
