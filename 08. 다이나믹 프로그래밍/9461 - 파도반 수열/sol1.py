# 파도반 수열 다국어
# https://www.acmicpc.net/problem/9461

table = [-1]*100
table[0] = 1
table[1] = 1
table[2] = 1


def main():

    n = int(input())
    for _ in range(n):
        print(sol1(int(input())))


def sol1(n: int) -> int:

    global table

    m = n - 1

    if m in {0, 1, 2}:
        return 1

    if table[m] != -1:
        return table[m]

    for i in range(3, n):
        table[i] = table[i-2] + table[i-3]

    return table[m]


if __name__ == '__main__':
    main()
