def main():
    N = int(input())
    X, Y = map(int, input().split())

    LIMIT = 10**3

    dp = [[LIMIT] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = 0

    for _ in range(N):
        a, b = map(int, input().split())
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                dx = min(x + a, X)
                dy = min(y + b, Y)
                dp[dx][dy] = min(dp[dx][dy], dp[x][y] + 1)

    if dp[X][Y] == LIMIT:
        dp[X][Y] = -1

    print(dp[X][Y])


if __name__ == "__main__":
    main()
