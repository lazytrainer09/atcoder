H, W = map(int, input().split())

G = [input() for _ in range(H)]
bools = [[True] * W for _ in range(H)]

current = [0, 0]

while True:
    i, j = current

    g = G[i][j]

    if g == "U":
        if i == 0:
            print(i + 1, j + 1)
            exit()
        i -= 1
    elif g == "D":
        if i == H - 1:
            print(i + 1, j + 1)
            exit()
        i += 1
    elif g == "L":
        if j == 0:
            print(i + 1, j + 1)
            exit()
        j -= 1
    elif g == "R":
        if j == W - 1:
            print(i + 1, j + 1)
            exit()
        j += 1

    if not bools[i][j]:
        print(-1)
        exit()

    bools[i][j] = False
    current = [i, j]
