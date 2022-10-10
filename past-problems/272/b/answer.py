N, M = map(int, input().split())

judge = [[False] * N for _ in range(N)]

for _ in range(M):
    k, *x = list(map(int, input().split()))
    x.sort()
    for i in range(k):
        for j in range(i + 1, k):
            a = x[i] - 1
            b = x[j] - 1
            judge[a][b] = True

for i in range(N):
    for j in range(i + 1, N):
        if judge[i][j]:
            continue
        print("No")
        exit()

print("Yes")
