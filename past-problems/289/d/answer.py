N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(list(map(int, input().split())))
X = int(input())


arrived = [False] * (X + 1)
arrived[0] = True

for i in range(X):
    if not arrived[i]:
        continue

    for a in A:
        if i + a > X:
            break

        if i + a in B:
            continue

        arrived[i + a] = True

if arrived[X]:
    print("Yes")
else:
    print("No")
