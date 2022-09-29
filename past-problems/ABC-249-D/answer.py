from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


ans = 0
for i in range(N):
    divs = make_divisors(A[i])
    for d in divs:
        cnt_j = cnt[d]
        cnt_k = cnt[A[i] // d]

        ans += cnt_j * cnt_k

print(ans)
