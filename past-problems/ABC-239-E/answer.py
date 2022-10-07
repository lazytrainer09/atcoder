import sys

readline = sys.stdin.readline
sys.setrecursionlimit(10**6)


def main():
    MAX_K = 20

    N, Q = map(int, input().split())
    X = [0] + list(map(int, input().split()))

    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    Tree = [[] for _ in range(N + 1)]

    def dfs(cur, pre):
        Tree[cur].append(X[cur])

        for nex in G[cur]:
            if nex == pre:
                continue
            dfs(nex, cur)
            Tree[cur].extend(Tree[nex])

        Tree[cur].sort(reverse=True)
        Tree[cur] = Tree[cur][:MAX_K]

    dfs(1, 0)

    for _ in range(Q):
        v, k = map(int, input().split())
        print(Tree[v][k - 1])


if __name__ == "__main__":
    main()
