import sys

INF = sys.maxsize

def solution(data, n, x, k):

    N1 = n + 1
    
    graph = [[INF]*N1 for _ in range(N1)]

    for i in range(1, N1):
        graph[i][i] = 0

    for a, b in data:
        graph[a][b] = 1
        graph[b][a] = 1

    for k in range(1, N1):
        for a in range(1, N1):
            for b in range(1, N1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    if graph[1][x] == INF or graph[x][k] == INF:
        return -1

    return graph[1][x] + graph[x][k]



def main():

    n = 5
    x = 4
    k = 5

    data = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 4],
        [3, 4],
        [3, 5],
        [4, 5],
    ]

    solution(data, n, x, k) == 3

    n = 4
    x = 3
    k = 4

    data = [
        [1, 3],
        [2, 4],
    ]

    solution(data, n, x, k) == -1

if __name__ == "__main__":
    main()