# 신나는 함수 실행
# https://www.acmicpc.net/problem/9184

import sys


def main():

    arr = []
    dp = {}

    while True:
        input = sys.stdin.readline
        a, b, c = map(int, input().split())

        if a == -1 and b == -1 and c == -1:
            break

        arr.append((a, b, c, sol1(a, b, c, dp)))
        for d in dp:
            print(d, dp[d])

    for a, b, c, o in arr:
        print(f'w({a}, {b}, {c}) = {o}')


def sol1(a: int, b: int, c: int, dp: list) -> int:

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return sol1(20, 20, 20, dp)

    if (a, b, c) in dp:
        return dp[(a, b, c)]

    if a < b and b < c:
        o = sol1(a, b, c-1, dp) + sol1(a, b-1, c-1, dp) - sol1(a, b-1, c, dp)
        dp[(a, b, c)] = o
        return o

    o = sol1(a-1, b, c, dp) + sol1(a-1, b-1, c, dp) + \
        sol1(a-1, b, c-1, dp) - sol1(a-1, b-1, c-1, dp)
    dp[(a, b, c)] = o
    return o


if __name__ == '__main__':
    main()
