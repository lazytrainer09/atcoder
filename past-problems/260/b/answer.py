N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

math = []
english = []
sum_point = []

for i in range(N):
    math.append([-A[i], i])
    english.append([-B[i], i])
    sum_point.append([-A[i] -B[i], i])

math.sort()
english.sort()
sum_point.sort()

ans = []
idx = set()

def pickup(lim, arr):
    global idx
    global ans
    cnt = 0
    i = 0
    while cnt < lim and i < N:
        if arr[i][1] in idx:
            i += 1
            continue

        ans.append(arr[i][1]+1)
        idx.add(arr[i][1])
        cnt += 1
        i += 1

pickup(X, math)
pickup(Y, english)
pickup(Z, sum_point)

ans.sort()

for a in ans:
    print(a)
