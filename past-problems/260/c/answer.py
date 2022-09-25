from collections import defaultdict

N, X, Y = map(int, input().split())

reds = defaultdict(int)
blues = defaultdict(int)

reds[N] += 1

for i in range(N):
    level = N - i
    if level == 1:
        break
    red_cnt = reds[level]

    reds[level - 1] += red_cnt
    blues[level] += red_cnt * X

    blue_cnt = blues[level]
    reds[level - 1] += blue_cnt
    blues[level - 1] += blue_cnt * Y

print(blues[1])
