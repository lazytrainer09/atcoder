N = int(input())

P = [0] * (N + 1)

for i in range(1, N + 1):
    exp_val = 0

    for j in range(1, 7):
        exp_val += max(P[i - 1], j)

    P[i] = exp_val / 6

print(P[N])
