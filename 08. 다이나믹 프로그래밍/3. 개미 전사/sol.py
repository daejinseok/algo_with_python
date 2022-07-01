def main():
    assert sol([1, 3, 1, 5]) == 8
    assert sol([3, 4, 1, 2, 4, 5, 18]) == 26


def sol(arr: list):
    n = len(arr)
    dp = [0] * n

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])

    return dp[n-1]


if __name__ == '__main__':
    main()
