from sys import stdin
import bisect

def main():
    input = stdin.readline
    N, M = map(int, input().split())
    X, Y = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    now = 0
    cnt = 0

    while True:
        idx = bisect.bisect_left(A, now)
        if idx == N:
            break
        now = A[idx] + X

        idx = bisect.bisect_left(B, now)
        if idx == M:
            break
        now = B[idx] + Y

        cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
