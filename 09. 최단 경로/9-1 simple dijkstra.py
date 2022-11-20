from dis import dis
import math
from tkinter import N

inf = math.inf


def solution(data, start_node, node_count):

    n = node_count + 1  # 시작 노드가 0이 아니라 1 이라서 하나 더해 줌

    graph = [[] for i in range(n)]
    visited = [False] * n
    distance = [inf] * n

    for a, b, c in data:
        graph[a].append((b, c))

    distance[start_node] = 0
    visited[start_node] = True

    for j in graph[start_node]:
        distance[j[0]] = j[1]

    for i in range(node_count - 1):
        now = get_smallest_node(visited, distance)
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            if distance[j[0]] > cost:
                distance[j[0]] = cost

    return distance[1:]


# 방문하지 않은 노드 중에서 가장 최단 거리 노드 반환
def get_smallest_node(visited, distance):

    min_value = inf
    min_idx = 0

    for idx, b in enumerate(visited):
        if not b:
            if min_value > distance[idx]:
                min_idx = idx
                min_value = distance[idx]

    return min_idx


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
