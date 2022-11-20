# 연속합
# https://www.acmicpc.net/problem/1912

import sys


def main():

    readline = sys.stdin.readline

    _ = readline()
    arr = list(map(int, readline().split()))
    print(sol1(arr))


def sol1(arr: list) -> int:

    o = -sys.maxsize
    n = len(arr)

    prefix = [0]
    sum_value = 0
    for i in arr:
        sum_value += i
        prefix.append(sum_value)

    for i in range(len(arr)):
        cur = 0
        for j in arr[i:]:
            cur = cur + j
            o = max(o, cur)
    return o


if __name__ == '__main__':
    main()
