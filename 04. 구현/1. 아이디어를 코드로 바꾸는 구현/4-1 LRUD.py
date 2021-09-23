def solution(n, data):

    x = 0
    y = 0

    for go in data:

        if go == 'R':
            if x != n:
                x += 1
        elif go == 'L':
            if x != 0:
                x -= 1
        elif go == 'D':
            if y != n:
                y += 1
        else:
            if y != 0:
                y -= 1

    return [x, y]


def main():
    assert solution(5, ['R', 'R', 'R', 'U', 'D', 'D']) == [3, 4]


if __name__ == "__main__":
    main()
