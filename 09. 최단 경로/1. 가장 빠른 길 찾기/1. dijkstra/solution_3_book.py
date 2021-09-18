import sys
from heapq import *

INF = sys.maxsize
N = 6
N1 = N + 1

def solution(data, start, end):

    graph = [[] for i in range(N1)] 

    for s, e, w in data:
        graph[s].append((e, w))

    return dijkstra(start, graph)


def dijkstra(start, graph):

    out = [INF] * N1

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
    
    return out[1:]
    

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