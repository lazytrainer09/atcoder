N = int(input())

s_dict = dict()

for i in range(N):
    s = input()

    if not s in s_dict:
        print(s)
        s_dict[s] = 1
        continue

    print(f"{s}({s_dict[s]})")
    s_dict[s] += 1
