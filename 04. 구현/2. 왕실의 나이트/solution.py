

def is_move(x, y):
    return 1 if 0 < x and x < 9 and 0 < y and y < 9 else 0


def solution(cp):

    x = 'abcdefgh'.index(cp[0]) + 1
    y = int(cp[1])

    knight_move = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]

    count = 0
    for dx, dy in knight_move:
        count += is_move(x+dx, y+dy)

    print(count)
    return count


def main():
    assert solution('a1') == 2
    assert solution('c2') == 6


if __name__ == "__main__":
    main()
