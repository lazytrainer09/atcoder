from collections import defaultdict

S = input()

cnt = defaultdict(int)

for s in S:
    cnt[s] += 1

for key in cnt:
    if cnt[key] == 1:
        print(key)
        exit()

print(-1)
