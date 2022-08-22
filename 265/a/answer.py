X, Y, N = map(int, input().split())

cost = 10**19

for i in range(100):
    for j in range(100):
        if i + j * 3 != N:
            continue

        cost = min(cost, i * X + j * Y)

print(cost)
