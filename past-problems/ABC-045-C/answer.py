S = input()

n = len(S) - 1
pos = []

for i in range(1 << n):
    l = []
    for j in range(n):
        if i >> j & 1:
            l.append(0)
        else:
            l.append(1)
    pos.append(l)

ans = 0
for p in pos:
    tmp = 0
    cur = S[0]
    for i in range(n):
        if p[i] == 0:
            cur += S[i + 1]
        else:
            tmp += int(cur)
            cur = S[i + 1]
    ans += tmp + int(cur)

print(ans)
