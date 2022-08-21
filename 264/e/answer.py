N, M, E = map(int, input().split())

codes = []

for _ in range(E):
    u, v = map(int, input().split())
    u = min(N + 1, u)
    v = min(N + 1, v)
    codes.append([u, v])

Q = int(input())
X = []
for _ in range(Q):
    X.append(int(input()))

set_X = set(X)


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


uf = UnionFind(N + 2)

for i, x in enumerate(codes):
    if i + 1 in set_X:
        continue
    uf.union(*codes[i])

cnt = uf.size(N + 1) - 1

answers = [cnt]

for x in reversed(X):
    u, v = codes[x - 1]
    if u == v:
        answers.append(cnt)
        continue

    u_check = uf.same(u, N + 1)
    v_check = uf.same(v, N + 1)

    if u_check and not v_check:
        cnt += uf.size(v)

    if not u_check and v_check:
        cnt += uf.size(u)

    uf.union(u, v)
    answers.append(cnt)

answers.pop(-1)

for ans in reversed(answers):
    print(ans)
