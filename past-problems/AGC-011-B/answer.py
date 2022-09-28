def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    A.sort(reverse=True)

    cnt = 0
    for i in range(N):
        cnt += 1
        if A[i] > (sum_A - A[i]) * 2:
            break
        sum_A -= A[i]

    print(cnt)


if __name__ == "__main__":
    main()
