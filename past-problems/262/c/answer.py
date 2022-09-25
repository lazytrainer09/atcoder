N = int(input())
a = list(map(int, input().split()))

cnt = 0
flags = [False] * N

for i in range(N):
    if a[i] == i + 1:
        flags[i] = True
        cnt += 1

ans = 0
for i in range(N):
    if flags[i]:
        continue

    if i + 1 == a[a[i] - 1]:
        ans += 1

ans //= 2

ans += cnt * (cnt - 1) // 2

print(ans)
