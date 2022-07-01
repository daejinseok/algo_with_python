
gdata = {1: 1, 2: 1}


def fibonacci(n: int) -> int:

    global gdata
    if n in gdata:
        return gdata[n]

    gdata[n] = fibonacci(n-1) + fibonacci(n-2)
    return gdata[n]


def main():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(99) == 218922995834555169026

    print(gdata)


if __name__ == '__main__':
    main()
