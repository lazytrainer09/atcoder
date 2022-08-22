import bisect

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

S = [0]

for i in range(N):
    S.append(S[i] + A[i])

for x in range(N):
    y = bisect.bisect_left(S, P + S[x])
    if y >= N or S[y] - S[x] != P:
        continue

    z = bisect.bisect_left(S, Q + S[y])
    if z >= N or S[z] - S[y] != Q:
        continue

    w = bisect.bisect_left(S, R + S[z])
    if w == N + 1 or S[w] - S[z] != R:
        continue

    print("Yes")
    exit()

print("No")
