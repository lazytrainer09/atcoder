K = int(input())

fibs = [1, 1]

for i in range(K):
    fibs.append(fibs[i]+fibs[i+1])

print(fibs[-1], fibs[-2])
