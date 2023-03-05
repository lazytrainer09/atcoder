from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    C = [0] + list(map(int, input().split()))
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    res = [[-1] * (N + 1) for _ in range(N + 1)]
    res[1][N] = 0
    que = deque()
    que.append((1, N))

    while len(que) > 0:
        t, a = que.popleft()
        for t2 in G[t]:
            for a2 in G[a]:
                if res[t2][a2] != -1:
                    continue
                if C[t2] == C[a2]:
                    continue

                res[t2][a2] = res[t][a] + 1
                que.append((t2, a2))

    print(res[N][1])
