def solution(data):
    return max(map(min, data))


def main():

    data = [
        [3, 1, 2],
        [4, 1, 4],
        [2, 2, 2],
    ]

    assert solution(data) == 2

    data = [
        [7, 3, 1, 8],
        [3, 3, 3, 4],
    ]

    assert solution(data) == 3


if __name__ == "__main__":
    main()
