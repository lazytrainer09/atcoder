N, M, T = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(M):
    x, y = map(int, input().split())
    A[x-1] -= y

for i in range(N-1):
    T -= A[i]
    if T <= 0:
        print("No")
        exit()

print("Yes")
