
n = 15
grids = [["#"]*n for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        continue

    # 全部黒を白に変えていく
    for j in range(i, n-i):
        grids[i][j] = "."
        grids[n-1-i][j] = "."

        grids[j][i] = "."
        grids[j][n-1-i] = "."

R, C = map(int, input().split())
R -= 1
C -= 1

if grids[R][C] == "#":
    print("black")
else:
    print("white")
