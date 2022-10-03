N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
A.sort(reverse=True)

ans = 0

for i in range(N):
    cnt = min(A[i] - A[i + 1], K // (i + 1))
    sum_a = (A[i] + A[i] - cnt + 1) * cnt // 2
    ans += sum_a * (i + 1)
    K -= cnt * (i + 1)

    if cnt < A[i] - A[i + 1]:
        ans += (A[i] - cnt) * (K % (i + 1))
        K -= K % (i + 1)

    if K == 0:
        break

print(ans)
