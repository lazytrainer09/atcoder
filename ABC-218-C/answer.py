def count(G, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if G[i][j] == "#":
                cnt += 1
    return cnt


def rot(S):
    return list(zip(*S[::-1]))


def find_left_top(G, n):
    for i in range(n):
        for j in range(n):
            if G[i][j] == ".":
                continue
            return i, j


def checker(S, T, n):
    si, sj = find_left_top(S, n)
    ti, tj = find_left_top(T, n)

    offset_i = ti - si
    offset_j = tj - sj

    for i in range(n):
        for j in range(n):
            i2 = i + offset_i
            j2 = j + offset_j

            if 0 <= i2 < n and 0 <= j2 < n:
                if S[i][j] != T[i2][j2]:
                    return False
            else:
                if S[i][j] == "#":
                    return False

    return True


N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

if count(S, N) != count(T, N):
    exit(print("No"))

for _ in range(4):
    S = rot(S)
    if checker(S, T, N):
        exit(print("Yes"))

print("No")
