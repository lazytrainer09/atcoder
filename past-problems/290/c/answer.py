N, K = map(int, input().split())
A = list(map(int, input().split()))

k_set = set(A)

ans = K
for i in range(K):
    if i in k_set:
        continue

    ans = i
    break

print(ans)
