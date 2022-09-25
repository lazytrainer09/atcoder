Y = int(input())

mod = Y % 4

ans = 0
while mod != 2:
    mod += 1
    mod %= 4
    ans += 1

print(ans + Y)
