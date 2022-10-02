def rot_str(s, l, r):
    rot_s = ""
    for i in range(r - l + 1):
        if s[l + i] == "p":
            rot_s += "d"
        else:
            rot_s += "p"

    return "".join(reversed(rot_s)) + s[r + 1 :]


def main():
    N = int(input())
    S = input()

    ps = []
    for i in range(N):
        if S[i] == "p":
            ps.append(i)

    if len(ps) == 0:
        exit(print(S))

    l = ps[0]
    ans = S[l:]

    for r in ps:
        ans = min(ans, rot_str(S, l, r))

    print(S[:l] + ans)


if __name__ == "__main__":
    main()
