def main():
    N = int(input())
    S = input()

    x_sum, m = 0, 0

    for i in range(1, N - 1):
        if S[i - 1 : i + 2] != "ARC":
            continue

        l, r = i - 1, i + 1
        while l - 1 >= 0 and S[l - 1] == "A":
            l -= 1

        while r + 1 < N and S[r + 1] == "C":
            r += 1

        x = min(i - l, r - i)
        x_sum += x
        m += 1

    print(min(x_sum, m * 2))


if __name__ == "__main__":
    main()
