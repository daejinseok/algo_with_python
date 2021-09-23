
def solution(n, m, k, data):

    data.sort()

    max0 = data[-1]
    max1 = data[-2]

    mok = m // (k+1)
    na = m % (k+1)

    return max0 * k * mok + max1 * mok + max0 * na

    #6*2*2 + 5*2 + 6*2


def main():

    n = 5
    m = 8
    k = 2

    data = [2, 4, 5, 4, 6]

    assert solution(n, m, k, data) == 46


if __name__ == "__main__":
    main()
