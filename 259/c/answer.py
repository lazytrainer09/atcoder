S = input()
T = input()

# ["a", 1]
s_cnt = []

def str_compressor(arr):
    cnts = []
    bef = "1"
    for i in range(len(arr)):
        if arr[i] == bef:
            cnts[-1][1] += 1
        else:
            cnts.append([arr[i], 1])
            bef = arr[i]
    return cnts

s_cnt = str_compressor(S)
t_cnt = str_compressor(T)

def print_no():
    print("No")
    exit()


if len(s_cnt) != len(t_cnt):
    print_no()

for i in range(len(s_cnt)):
    if s_cnt[i][0] != t_cnt[i][0]:
        print_no()

    sc = s_cnt[i][1]
    tc = t_cnt[i][1]

    if sc > tc:
        print_no()

    if sc == tc:
        continue

    if sc == 1:
        print_no()

print("Yes")
