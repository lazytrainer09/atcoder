N, M, X, T, D = map(int, input().split())

since = min(X, M)

ini = T - D * X

print(ini + since * D)
