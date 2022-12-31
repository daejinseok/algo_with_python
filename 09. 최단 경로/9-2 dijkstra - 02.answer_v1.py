import math
from heapq import heappush, heappop

INF = math.inf


def solution(data, start_node, node_count):

    N = node_count + 1

    graph = [[] for i in range(N)]
    distance = [INF] * N

    for a, b, v in data:
        graph[a].append((b, v))

    q = []
    heappush(q, (0, start_node))
    distance[start_node] = 0

    while q:
        d, node = heappop(q)

        if distance[node] < d:
            continue

        for b, v in graph[node]:
            cost = d + v
            if distance[b] > cost:
                distance[b] = cost
                heappush(q, (distance[b], b))

    return distance[1:]


def main():

    data = [
        [1, 2, 2],
        [1, 3, 5],
        [1, 4, 1],
        [2, 3, 3],
        [2, 4, 2],
        [3, 2, 3],
        [3, 6, 5],
        [4, 3, 3],
        [4, 5, 1],
        [5, 3, 1],
        [5, 6, 2],
    ]

    assert solution(data, 1, 6) == [0, 2, 3, 1, 2, 4]


if __name__ == "__main__":
    main()
