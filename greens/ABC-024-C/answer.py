from sys import stdin


def main():
    input = stdin.readline

    N, D, K = map(int, input().split())
    moves = [list(map(int, input().split())) for _ in range(D)]

    for _ in range(K):
        s, t = map(int, input().split())
        cur_min = cur_max = s
        for i in range(D):
            l, r = moves[i]
            if cur_min <= r:
                cur_min = min(cur_min, l)
            if cur_max >= l:
                cur_max = max(cur_max, r)

            if cur_min <= t <= cur_max:
                print(i + 1)
                break


if __name__ == "__main__":
    main()
