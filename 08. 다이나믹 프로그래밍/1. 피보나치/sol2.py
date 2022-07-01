def main():
    #assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(99) == 218922995834555169026


def fibonacci(n: int) -> int:

    d = [0]*n

    d[0] = 1
    d[1] = 1

    for i in range(2, n):
        d[i] = d[i-2] + d[i-1]

    return d[-1]


if __name__ == '__main__':
    main()
