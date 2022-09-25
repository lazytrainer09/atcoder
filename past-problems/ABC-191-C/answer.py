from sys import stdin


def main():
    input = stdin.readline
    H, W = map(int, input().split())
    S = [input().rstrip() for _ in range(H)]

    edge_cnt = 0
    for h in range(1, H):
        for w in range(1, W):
            cnt = 0
            for dh, dw in [[-1, -1], [-1, 0], [0, -1], [0, 0]]:
                if S[h + dh][w + dw] == "#":
                    cnt += 1
            if cnt % 2 != 0:
                edge_cnt += 1

    print(edge_cnt)


if __name__ == "__main__":
    main()
