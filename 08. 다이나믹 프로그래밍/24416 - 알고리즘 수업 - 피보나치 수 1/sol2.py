# 알고리즘 수업 - 피보나치 수 1
# https://www.acmicpc.net/problem/24416


def main():

    n = int(input())
    print(fibonacci(n), n-2)


def fibonacci(n: int) -> int:

    a1, a2 = 0, 1

    for _ in range(n):
        a1, a2 = a2, a1+a2

    return a1


if __name__ == '__main__':
    main()
