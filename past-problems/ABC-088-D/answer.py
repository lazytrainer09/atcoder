from collections import deque

H, W = map(int, input().split())
G = [input() for _ in range(H)]
dist = [[-1] * W for _ in range(H)]

dist[0][0] = 0
Q = deque()
Q.append([0, 0])

while len(Q) > 0:
    h, w = Q.popleft()
    for dh, dw in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        h2 = h + dh
        w2 = w + dw

        if not (0 <= h2 < H and 0 <= w2 < W):
            continue

        if G[h2][w2] == "#":
            continue

        if dist[h2][w2] == -1:
            Q.append([h2, w2])
            dist[h2][w2] = dist[h][w] + 1

dot_cnt = 0
for i in range(H):
    for j in range(W):
        if G[i][j] == ".":
            dot_cnt += 1

if dist[H - 1][W - 1] == -1:
    exit(print(-1))

print(dot_cnt - dist[H - 1][W - 1] - 1)
