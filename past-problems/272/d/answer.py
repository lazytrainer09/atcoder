import math
from collections import defaultdict
from collections import deque

N, M = map(int, input().split())

moves = defaultdict(set)

lim = math.ceil(math.sqrt(M))


def add_moves(i, j):
    for di in [1, -1]:
        for dj in [1, -1]:
            moves[i * di].add(j * dj)
            moves[j * dj].add(i * di)


for i in range(lim + 1):
    for j in range(i, lim + 1):
        if i**2 + j**2 == M:
            add_moves(i, j)

dist = [[-1] * (N) for _ in range(N)]
dist[0][0] = 0

Q = deque()
Q.append([0, 0])

while len(Q) > 0:
    i, j = Q.popleft()

    for di in moves:
        for dj in list(moves[di]):
            if not (0 <= i + di < N and 0 <= j + dj < N):
                continue

            if dist[i + di][j + dj] != -1:
                continue

            dist[i + di][j + dj] = dist[i][j] + 1
            Q.append([i + di, j + dj])

for i in range(N):
    print(*dist[i])
