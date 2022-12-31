import math
from heapq import heappush, heappop

INF = math.inf
push = heappush
pop = heappop


def solution(data, start_node, node_count):
    N = node_count + 1
    o = [INF] * N

    gh = [[] for _ in range(N)]
    for a, b, v in data:
        gh[a].append((b, v))

    q = []
    push(q, (start_node, 0))
    o[start_node] = 0

    while q:
        node, d = pop(q)

        if o[node] < d:
            continue

        for b, v in gh[node]:
            d2 = d + v

            if d2 < o[b]:
                o[b] = d2
                push(q, (b, d2))

    return o[1:]


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
