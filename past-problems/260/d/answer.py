from bisect import bisect

N, K = map(int, input().split())
P = list(map(int, input().split()))

keys = [0]
cards = [[]]

ans = [-1] * N

for i, p in enumerate(P):
    j = bisect(keys, p)
    if j == len(keys):
        keys.append(p)
        cards.append([p])
    else:
        keys[j] = p
        cards[j].append(p)

    if len(cards[j]) == K:
        for k in cards[j]:
            ans[k - 1] = i + 1
        keys.pop(j)
        cards.pop(j)

print(*ans, sep="\n")
