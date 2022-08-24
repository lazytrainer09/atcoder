import itertools

N, M = map(int, input().split())

l = list(range(1, M + 1))

for v in itertools.combinations(l, N):
    print(*list(v))
