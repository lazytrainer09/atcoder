N, M = map(int, input().split())

C = []
for m in range(M):
    c = int(input())
    a = list(map(int, input().split()))
    C.append(a)

ptns = []
for i in range(1 << M):
    p = []
    for j in range(M):
        if i >> j & 1:
            p.append(j + 1)
    ptns.append(p)

ptns.pop(0)

ans = 0
for p in ptns:
    nums = set()
    for k in p:
        nums.update(C[k - 1])

    flg = True
    for n in range(1, N + 1):
        if not n in nums:
            flg = False
            break

    if flg:
        ans += 1

print(ans)
