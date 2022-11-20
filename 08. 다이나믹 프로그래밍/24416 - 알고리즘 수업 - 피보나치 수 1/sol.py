# 알고리즘 수업 - 피보나치 수 1
# https://www.acmicpc.net/problem/24416


def main():

    n = int(input())
    print(fibonacci(n), n-2)

    # assert fibonacci(5) == 5
    # assert fibonacci(30) == 832040


def fibonacci(n: int) -> int:

    dp = [0]*n
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


if __name__ == '__main__':
    main()
