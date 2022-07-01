import sys


def sol(n: int) -> int:

    def f(i, div):
        if i % div == 0:
            return dp[i // div]
        else:
            return sys.maxsize

    dp = [0] * (n + 1)

    for i in range(2, n+1):

        dp[i] = min(
            dp[i-1],
            f(i, 2),
            f(i, 3),
            f(i, 5)) + 1

    return dp[n]


def main():
    assert sol(1) == 0
    assert sol(2) == 1
    assert sol(3) == 1
    assert sol(4) == 2
    assert sol(5) == 1
    assert sol(6) == 2
    assert sol(26) == 3


if __name__ == '__main__':
    main()
