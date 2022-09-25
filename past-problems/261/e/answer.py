N, C = map(int, input().split())


def operation(t, num1, num2):
    if t == 1:
        return num1 & num2
    elif t == 2:
        return num1 | num2
    else:
        return num1 ^ num2


all_zero = [0]

ini_one = 1
for _ in range(31):
    ini_one = ini_one << 1
    ini_one += 1
all_one = [ini_one]

for i in range(N):
    t, a = map(int, input().split())
    all_zero.append(operation(t, all_zero[i], a))
    all_one.append(operation(t, all_one[i], a))

x = C
for i in range(N):
    z = all_zero[i + 1] & (~x)
    o = all_one[i + 1] & x

    x = z | o
    print(x)
