N, K = map(int, input().split())
S = input()

ans = ""
cnt = 0
passed = 0

for i in range(N):
    if passed == K:
        break

    if S[i] == "o":
        passed += 1

    ans += S[i]
    cnt += 1

ans += "x" * (N - cnt)

print(ans)
