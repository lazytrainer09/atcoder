def main():
    N = int(input())
    p = list(map(int, input().split()))
    happy = [0] * N

    for i in range(N):
        diff = (p[i] - i + N) % N
        happy[diff - 1] += 1
        happy[diff] += 1
        happy[(diff + 1) % N] += 1

    print(max(happy))


if __name__ == "__main__":
    main()
