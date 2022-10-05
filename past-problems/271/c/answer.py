from collections import deque

N = int(input())
A = list(map(int, input().split()))
altA = list(set(A))
altA.sort()

Q = deque()
Q.extend(altA)
Q.extend([10**10] * (N - len(altA)))


ans = 0
while len(Q) > 1:
    if Q[0] == ans + 1:
        Q.popleft()
        ans += 1
        continue

    Q.pop()
    Q.pop()
    ans += 1

if len(Q) > 0 and Q[0] == ans + 1:
    ans += 1

print(ans)
