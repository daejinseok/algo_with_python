# 01타일
# https://www.acmicpc.net/problem/1904


mod = 15746


def main():

    n = int(input())
    print(sol1(n) % mod)


def sol1(n: int) -> int:

    if n == 1:
        return 1

    a1, a2 = 1, 1

    for _ in range(1, n):
        a1, a2 = a2, (a1+a2) % mod

    return a2


if __name__ == '__main__':
    main()
