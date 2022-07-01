import sys


def main():
    assert sol([2, 3], 15) == 5
    assert sol([3, 5, 7], 4) == -1


def sol(coins: list, m: int):

    m1 = m+1

    d = [sys.maxsize]*m1
    d[0] = 0

    for coin in coins:
        for j in range(coin, m1):
            if d[j - coin] != sys.maxsize:
                d[j] = min(d[j], d[j-coin]+1)

    for i in d:
        print(i)

    if d[m] == sys.maxsize:
        return -1

    return d[m]


if __name__ == '__main__':
    main()
