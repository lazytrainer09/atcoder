
def main():
    S = input()
    T = input()

    if len(S) > len(T):
        print("No")
        exit()

    for i in range(len(S)):
        if S[i] == T[i]:
            continue

        print("No")
        exit()

    print("Yes")


if __name__ == "__main__":
    main()
