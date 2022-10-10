N = int(input())
A = list(map(int, input().split()))

odds = []
evens = []


def ope(num, array):
    array.append(A[num])

    if len(array) <= 2:
        return array

    array.sort(reverse=True)
    array.pop(-1)

    return array


for i in range(N):
    if A[i] % 2:
        odds = ope(i, odds)
    else:
        evens = ope(i, evens)

ans = -1

if len(odds) == 2:
    ans = max(ans, sum(odds))

if len(evens) == 2:
    ans = max(ans, sum(evens))

print(ans)
