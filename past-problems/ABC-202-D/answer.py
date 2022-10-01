import math


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def create_str(A, B, K, S):
    if A == 0 or B == 0:
        return S + A * "a" + B * "b"

    c = comb(A + B - 1, A - 1)
    if K <= c:
        S += "a"
        A -= 1
    else:
        S += "b"
        B -= 1
        K -= c

    return create_str(A, B, K, S)


def main():
    A, B, K = map(int, input().split())
    ans = create_str(A, B, K, "")
    print(ans)


if __name__ == "__main__":
    main()
