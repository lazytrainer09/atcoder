l1, r1, l2, r2 = map(int, input().split())

L = max(l1, l2)
R = min(r1, r2)

print(max(R - L, 0))
