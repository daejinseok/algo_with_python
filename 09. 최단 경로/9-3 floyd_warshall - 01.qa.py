def solution(data):

    pass


def file_read(file_name: str, col_count: int):
    with open(file_name, 'rt') as f:
        other = []
        out = []
        for line in f:
            words = list(map(int, line.split()))
            if len(words) == col_count:
                out.append(words)
            else:
                other.append(words[0])
    return out, other


def main():

    data_file = '9-3 floyd_warshall - data.txt'
    output_file = '9-3 floyd_warshall - out.txt'

    data, other = file_read(data_file, 3)
    out, _ = file_read(output_file, 4)

    assert solution(data, other[0]) == out


if __name__ == "__main__":
    main()
