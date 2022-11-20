import sys
from heapq import *

INF = sys.maxsize


def solution(data, n, start):

    N1 = n+1

    graph = [[] for _ in range(N1)]

    for a, b, c in data:
        graph[a].append((b, c))
    

    return dijkstra(graph, n, start)


def dijkstra(graph, n, start):

    N1 = n+1

    out = [INF]*N1
    q = []

    out[start] = 0
    heappush(q, (0, start))

    while q:
        qcost, qnode = heappop(q)
        if qcost > out[qnode]:
            continue

        for gnode, gcost in graph[qnode]:
            cost = qcost + gcost
            if cost < out[gnode]:
                out[gnode] = cost
                heappush(q, (cost, gnode))

    count = 0
    m = -1
    for c in out[1:]:
        if c != INF:
            count += 1
            m = max(m, c)

    return [c, m]

def main():

    n = 3
    start = 1

    data = [
        [1, 2, 4],
        [1, 3, 2],
    ]

    assert solution(data, n, start) == [2, 4]

if __name__ == "__main__":
    main()