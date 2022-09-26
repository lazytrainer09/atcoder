N, K = map(int, input().split())
S = input()

cnt = 1
ini = S[0]

for i in S:
    if i != ini:
        ini = i
        cnt += 1

print(N - max(1, cnt - 2 * K))
