S = input()
T = "atcoder"

ans = 0
for t in T:
    ans += S.find(t)
    S = S.replace(t, "")


print(ans)
