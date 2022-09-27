N = int(input())
F = [0] + list(map(int, input().split()))

used = [False] * (N + 1)
pairs = []

for i in range(1, N + 1):
    if used[i]:
        continue

    used[i] = True

    pair = set()
    pair.add(i)
    cur = i
    flg = False

    while True:
        cur = F[cur]

        if cur == i:
            flg = True
            break

        if used[cur]:
            break

        if cur in pair:
            break

        pair.add(cur)

    if flg:
        pairs.append(pair)

mod = 998244353
print(pow(2, len(pairs), mod) - 1)
