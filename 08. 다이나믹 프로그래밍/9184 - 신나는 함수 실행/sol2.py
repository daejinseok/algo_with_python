# 신나는 함수 실행
# https://www.acmicpc.net/problem/9184

import sys

# global table
gt = [[[sys.maxsize]*21 for _ in range(21)] for _ in range(21)]


def main():

    while True:
        input_line = sys.stdin.readline()
        a, b, c = map(int, input_line.split())

        if a == -1 and b == -1 and c == -1:
            break

        o = sol2(a, b, c)
        print(f'w({a}, {b}, {c}) = {o}')


def sol2(a: int, b: int, c: int) -> int:

    global gt

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return sol2(20, 20, 20)

    if gt[a][b][c] != sys.maxsize:
        return gt[a][b][c]

    if a < b and b < c:
        gt[a][b][c] = sol2(a, b, c-1) + sol2(a, b-1, c-1) - sol2(a, b-1, c)
        return gt[a][b][c]

    gt[a][b][c] = sol2(a-1, b, c) + sol2(a-1, b-1, c) + \
        sol2(a-1, b, c-1) - sol2(a-1, b-1, c-1)
    return gt[a][b][c]


if __name__ == '__main__':
    main()
