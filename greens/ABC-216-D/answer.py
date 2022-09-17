from collections import deque
from collections import defaultdict

N, M = map(int, input().split())

cylinders = []
rest = [0]*M

colors = defaultdict(list)

for i in range(M):
    k = int(input())
    a = list(map(int, input().split()))
    cylinders.append(a)

    rest[i] = k - 1

    colors[a[-1]].append(i)

Q = deque()

for key in colors:
    if len(colors[key]) != 2:
        continue

    Q.append(key)

def operation(i):
    if rest[i] == 0:
        return

    new_key = cylinders[i][rest[i]-1]
    rest[i] -= 1

    colors[new_key].append(i)
    if len(colors[new_key]) == 2:
        Q.append(new_key)


while len(Q) > 0:
    key = Q.popleft()
    i, j = colors[key]
    operation(i)
    operation(j)

if sum(rest) == 0:
    print("Yes")
else:
    print("No")
