H, W = map(int, input().split())

after = [input() for _ in range(H)]

bef = []
for i in range(H):
    s = ""
    for j in range(W):
        if after[i][j] == ".":
            s += "."
            continue

        flag = True

        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                if not (0 <= i + di < H):
                    continue
                if not (0 <= j + dj < W):
                    continue

                if after[i+di][j+dj] == ".":
                    flag = False
                    break

        if flag:
            s += "#"
        else:
            s += "."
    bef.append(s)

best = [["."]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if bef[i][j] == ".":
            continue

        for di in range(-1, 2):
            for dj in range(-1, 2):
                if not (0 <= i + di < H):
                    continue
                if not (0 <= j + dj < W):
                    continue

                best[i+di][j+dj] = "#"

for i in range(H):
    for j in range(W):
        if after[i][j] != best[i][j]:
            print("impossible")
            exit()

print("possible")
for i in range(H):
    print(bef[i])
