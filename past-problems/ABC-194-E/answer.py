from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

m_cnt = defaultdict(int)
for i in range(M):
    m_cnt[A[i]] += 1

mex = set()

for i in range(N + 1):
    if i in m_cnt:
        continue
    mex.add(i)

ans = min(mex)

for i in range(M, N):
    if A[i] == A[i - M]:
        continue

    m_cnt[A[i]] += 1
    mex.discard(A[i])

    m_cnt[A[i - M]] -= 1
    if m_cnt[A[i - M]] == 0:
        mex.add(A[i - M])
        ans = min(ans, A[i - M])

print(ans)
