N, M = map(int, input().split())
A = list(map(int, input().split()))

B = A[0:M]

now = 0
for i in range(M):
    now += B[i] * (i + 1)

for i in range(M, N):
    idx = -1
    sum_B = sum(B)
    max_i = now
    for j in range(M):
        tmp = now - sum_B - (B[j] * j) + (A[i] * M)
        sum_B -= B[j]

        if max_i >= tmp:
            continue

        idx = j
        max_i = tmp

    if idx == -1:
        continue

    B.pop(idx)
    B.append(A[i])
    now = max_i

print(now)
