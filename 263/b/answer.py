N = int(input())
P = [0] + list(map(int, input().split()))

cnt = 0
i = N
while i > 1:
    i = P[i - 1]
    cnt += 1

print(cnt)
