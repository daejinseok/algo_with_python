

def sol(n: int) -> int:

    #dp = [0, 0]
    dp = [0] * (n + 1)

    for i in range(2, n+1):

        #dp.append(dp[i-1] + 1)
        dp[i] = dp[i-1] + 1

        if i % 5 == 0:
            dp[i] = min(dp[i//5] + 1, dp[i])
        if i % 3 == 0:
            dp[i] = min(dp[i//3] + 1, dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i//2] + 1, dp[i])

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
