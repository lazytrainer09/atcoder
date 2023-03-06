import math

T = int(input())

for _ in range(T):
    N, D, K = map(int, input().split())
    n = N // math.gcd(N, D)

    print((K - 1) // n + (K - 1) * D % N)
