from collections import defaultdict

cards = list(map(int, input().split()))

cnt = defaultdict(int)

for c in cards:
    cnt[c] += 1

three = False
two = False

if 2 in cnt.values() and 3 in cnt.values():
    print("Yes")
else:
    print("No")
