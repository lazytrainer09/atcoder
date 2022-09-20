from sys import stdin
import heapq


def main():
    input = stdin.readline
    Q = int(input())

    sorted_list = []
    tmp = []
    tmp_i = 0

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            tmp.append(query[1])
        elif query[0] == 2:
            if len(sorted_list) > 0:
                print(heapq.heappop(sorted_list))
            else:
                print(tmp[tmp_i])
                tmp_i += 1
        else:
            while tmp_i < len(tmp):
                heapq.heappush(sorted_list, tmp[tmp_i])
                tmp_i += 1
            tmp = []
            tmp_i = 0


if __name__ == "__main__":
    main()
