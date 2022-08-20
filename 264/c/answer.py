import itertools

h1, w1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h1)]

h2, w2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(h2)]

lists_h = list(itertools.combinations(list(range(h1)), h2))
lists_w = list(itertools.combinations(list(range(w1)), w2))

completed = False
for l_h in lists_h:
    for l_w in lists_w:
        tmp_flag = True
        for i, h in enumerate(l_h):
            for j, w in enumerate(l_w):
                if A[h][w] != B[i][j]:
                    tmp_flag = False
        if tmp_flag:
            completed = True

if completed:
    print("Yes")
else:
    print("No")
