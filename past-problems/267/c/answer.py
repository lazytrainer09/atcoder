N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0]

for i in range(N):
    S.append(A[i] + S[i])

B = 0
for i in range(M):
    B += A[i] * (i + 1)

now = B
for i in range(0, N - M):
    now += A[i + M] * M - (S[i + M] - S[i])
    B = max(B, now)

print(B)
