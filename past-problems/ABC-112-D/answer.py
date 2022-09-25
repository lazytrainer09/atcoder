N, M = map(int, input().split())

for i in range(M // N, 0, -1):
    rest = M - (N - 1) * i
    if rest % i != 0:
        continue

    print(i)
    exit()
