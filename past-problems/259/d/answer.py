class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


N = int(input())
uf = UnionFind(N)

sx, sy, tx, ty = map(int, input().split())

S = []
T = []

circles = []


def dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


for i in range(N):
    x, y, r = map(int, input().split())
    circles.append([x, y, r])

    if dist(sx, sy, x, y) == r**2:
        S.append(i)

    if dist(tx, ty, x, y) == r**2:
        T.append(i)

for i in range(N):
    for j in range(i + 1, N):
        x1, y1, r1 = circles[i]
        x2, y2, r2 = circles[j]

        d = dist(x1, y1, x2, y2)

        if d > (r1 + r2) ** 2:
            continue

        if d < (max(r1, r2) - min(r1, r2)) ** 2:
            continue

        uf.union(i, j)

for s in S:
    for t in T:
        if uf.same(s, t):
            print("Yes")
            exit()

print("No")
