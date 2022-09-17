from collections import defaultdict

N = int(input())

points = []

for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

pq = defaultdict(int)

eff = 10**10

for i in range(N):
    for j in range(i + 1, N):
        p = points[i][0] - points[j][0]
        q = points[i][1] - points[j][1]

        pq[p + q * eff] += 1
        pq[-p - q * eff] += 1

ans = N

for key in pq:
    ans = min(ans, N - pq[key])

print(ans)
