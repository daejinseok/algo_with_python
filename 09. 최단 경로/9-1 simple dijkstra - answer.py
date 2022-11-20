import math

INF = math.inf


def solution(data, start_node, node_count):

    n = node_count + 1  # 시작 노드가 0이 아니라 1 이라서 하나 더해 줌

    graph = [[] for i in range(n)]
    visited = [False] * n
    distance = [INF] * n

    for a, b, c in data:
        graph[a].append((b, c))

    # 처음
    distance[start_node] = 0
    visited[start_node] = True

    for b, v in graph[start_node]:
        distance[b] = v

    # n번
    for i in range(node_count - 1):
        now = get_smallest_node(visited, distance)
        visited[now] = True

        for b, v in graph[now]:
            cost = distance[now] + v
            distance[b] = min(distance[b], cost)

    return distance[1:]


# 방문하지 않은 노드 중에서 가장 최단 거리 노드 반환
def get_smallest_node(visited, distance):

    min_value = INF
    min_idx = 0

    for idx, (v, d) in enumerate(zip(visited, distance)):
        if not v and min_value > d:
            min_idx = idx
            min_value = d

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
