def solution(n, k):

    count = 0
    while True:

        if n == 1:
            break

        if n < k:
            break

        if n % k == 0:
            n = n / k
        else:
            n -= 1

        count += 1

    if n != 1:
        count += n - 1

    return count


def main():
    assert solution(25, 5) == 2
    assert solution(25, 26) == 24


if __name__ == "__main__":
    main()
