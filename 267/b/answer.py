S = input()

# 立っているものがtrue, 倒れていたらfalse
state = [False]*7

pins = {
    1:  3,
    2:  2,
    3:  4,
    4:  1,
    5:  3,
    6:  5,
    7:  0,
    8:  2,
    9:  4,
    10: 6
}

for i in range(10):
    if i == 0 and int(S[i]) == 1:
        print("No")
        exit()

    if int(S[i]) == 0:
        continue

    state[pins[i+1]] = True


for i in range(5):
    if not state[i]:
        continue

    if state[i+1]:
        continue

    for j in range(i+2, 7):
        if state[j]:
            print("Yes")
            exit()

print("No")
