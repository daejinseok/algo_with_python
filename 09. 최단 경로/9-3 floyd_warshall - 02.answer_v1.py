import math

INF = math.inf


def solution(data, n):

    o = [[INF]*n for _ in range(n)]

    for i in range(n):
        o[i][i] = 0

    for a, b, v in data:
        o[a-1][b-1] = v

    for i in range(n):
        for a in range(n):
            for b in range(n):
                o[a][b] = min(o[a][b], o[a][i] + o[i][b])

    return o


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
