from sys import stdin


def main():
    input = stdin.readline
    N = int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    que = [[1, 0, 1]]
    LR = [[10**9, 0] for _ in range(N + 1)]
    num = 1

    while len(que) > 0:
        now, parent, cnt = que.pop()
        if cnt == 1:
            que.append([now, parent, 2])
            for g in G[now]:
                if g != parent:
                    que.append([g, now, 1])
        else:
            if now != 1 and len(G[now]) == 1:
                LR[now] = [num, num]
                num += 1

            LR[parent][0] = min(LR[parent][0], LR[now][0])
            LR[parent][1] = max(LR[parent][1], LR[now][1])

    for i in range(1, N + 1):
        print(*LR[i])


if __name__ == "__main__":
    main()
