N, M = map(int, input().split())

G = [set() for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].add(v-1)
    G[v-1].add(u-1)

cnt = 0
for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if b in G[a] and c in G[b] and a in G[c]:
                cnt += 1

print(cnt)
