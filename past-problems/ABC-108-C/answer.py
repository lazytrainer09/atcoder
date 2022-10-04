from collections import defaultdict


def main():
    N, K = map(int, input().split())

    dic = defaultdict(int)
    for i in range(1, N + 1):
        dic[i % K] += 1

    ans = 0
    for k in dic:
        if k == 0:
            ans += dic[k] ** 3
            continue

        if K != 2 * k:
            continue

        ans += dic[k] ** 3

    print(ans)


if __name__ == "__main__":
    main()
