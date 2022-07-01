def main():
    assert sol(3) == 5


def sol(n):

    d = [0]*n
    d[0] = 1
    d[1] = 3

    for i in range(2, n):
        d[i] = d[i-1] + 2*d[i-2]

    return d[-1]


if __name__ == '__main__':
    main()
