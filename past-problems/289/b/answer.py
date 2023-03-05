N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = []
j = 0
for i in range(1, N + 1):
    if i in A:
        continue
    for x in range(i, j, -1):
        ans.append(x)
    j = i

print(*ans)
