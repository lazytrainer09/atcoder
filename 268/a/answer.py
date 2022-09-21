from sys import stdin


def main():
    input = stdin.readline
    a = list(map(int, input().split()))
    print(len(set(a)))


if __name__ == "__main__":
    main()
