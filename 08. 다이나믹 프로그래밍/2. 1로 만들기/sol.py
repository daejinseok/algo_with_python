dp = {1: 0}


def sol(n: int) -> int:

    global dp
    if n in dp:
        return dp[n]

    mid_dp = []

    if n % 5 == 0:
        mid_dp.append(sol(n/5))
    if n % 3 == 0:
        mid_dp.append(sol(n/3))
    if n % 2 == 0:
        mid_dp.append(sol(n/2))

    mid_dp.append(sol(n-1))

    dp[n] = min(mid_dp) + 1

    print(f'{n} : {dp[n]}')
    return dp[n]


def main():
    assert sol(1) == 0
    assert sol(2) == 1
    assert sol(3) == 1
    assert sol(4) == 2
    assert sol(5) == 1
    assert sol(6) == 2

    for i in range(6, 26):
        sol(i)

    assert sol(26) == 3

    for k in dp:
        print(f'{k} : {dp[k]}')


if __name__ == '__main__':
    main()
