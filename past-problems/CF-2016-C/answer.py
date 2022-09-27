import string

alphabet = string.ascii_lowercase

S = input()
K = int(input())

dic = {}
cnt = 26
for s in alphabet:
    dic[s] = cnt % 26
    cnt -= 1

ans = []
for s in S:
    if K >= dic[s]:
        K -= dic[s]
        ans.append("a")
    else:
        ans.append(s)

if K > 0:
    i = alphabet.find(ans[-1])
    ans[-1] = alphabet[(i + K) % 26]


print("".join(ans))
