N = int(input())

results = [input() for _ in range(N)]

judge = {"W": "L", "L": "W", "D": "D"}

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        a, b = results[i][j], results[j][i]
        if judge[a] == b:
            continue

        print("incorrect")
        exit()

print("correct")
