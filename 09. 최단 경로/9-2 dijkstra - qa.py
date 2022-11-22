import math
from heapq import heappush, heappop

INF = math.inf


def solution(data, start_node, node_count):

    N = node_count + 1

    graph = [[] for i in range(N)]
    visited = [False] * N
    distance = [INF] * N

    for a, b, v in data:
        graph[a].append((b, v))

    visited[start_node] = True
    distance[start_node] = 0
    for b, v in graph[start_node]:
        distance[b] = v

    for _ in range(N-1):
        node = smallest_node(distance, visited)

        visited[node] = True
        for b, v in graph[node]:
            distance[b] = min(distance[b], distance[node]+v)

    return distance[1:]


def smallest_node(distance, visited):

    cur_d = INF
    cur_idx = 0

    for idx, (d, v) in enumerate(zip(distance, visited)):
        if not v and cur_d > d:
            cur_idx = idx
            cur_d = d

    return cur_idx


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
