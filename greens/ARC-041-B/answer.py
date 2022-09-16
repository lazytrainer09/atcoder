N, M = map(int, input().split())

B = []
for _ in range(N):
    B.append(list(map(int, list(input()))))

A = [[0]*M for _ in range(N)]

edge = 0

def ope_line(edge):
    for j in range(M):
        i = edge
        if B[i][j] == 0:
            continue

        cnt = B[i][j]
        A[i+1][j] += cnt

        B[i][j] = 0
        B[i+1][j-1] -= cnt
        B[i+1][j+1] -= cnt
        B[i+2][j] -= cnt

for i in range(N):
    ope_line(i)

for i in range(N):
    print("".join(map(str, A[i])))
