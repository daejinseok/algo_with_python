import sys

INF = sys.maxsize
N = 4
N1 = N + 1

def solution(data):
    
    graph = [[INF]*N1 for _ in range(N1)]

    for i in range(1, N1):
        graph[i][i] = 0

    for a, b, cost in data:
        graph[a][b] = cost
        #graph[b][a] = cost 완복이 같은 때

    for k in range(1, N1):
        for a in range(1, N1):
            for b in range(1, N1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    out = []
    for i in range(1, N1):
        out.append( graph[i][1:])

    return out


def main():

    data = [
        [1, 2, 4],
        [1, 4, 6],
        [2, 1, 3],
        [2, 3, 7],
        [3, 1, 5],
        [3, 4, 4],
        [4, 3, 2],
    ]

    out = [
        [0, 4,  8, 6],
        [3, 0,  7, 9],
        [5, 9,  0, 4],
        [7, 11, 2, 0],
    ]

    assert solution(data) == out


if __name__ == "__main__":
    main()