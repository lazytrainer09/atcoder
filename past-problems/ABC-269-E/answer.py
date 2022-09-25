N = int(input())

A = C = 1
B = D = N

while B - A > 0:
    mid = (A + B) // 2
    print("?", A, mid, 1, N)

    t = int(input())
    if t == -1:
        exit()

    if t < mid - A + 1:
        B = mid
    else:
        A = mid + 1

while D - C > 0:
    mid = (C + D) // 2
    print("?", 1, N, C, mid)

    t = int(input())
    if t == -1:
        exit()

    if t < mid - C + 1:
        D = mid
    else:
        C = mid + 1

print("!", A, C)
