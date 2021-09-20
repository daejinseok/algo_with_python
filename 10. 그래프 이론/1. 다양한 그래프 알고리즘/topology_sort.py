
"""
Topology Sort (위상 정렬)
순서가 정해져 있는 일련의 작업을
차례대로 수행해야 할 때 사용할 수 있는 정렬 알고리즘

진입차수 : indegree

"""
from collections import deque


def topology_sort(N1, indegree, graph):

    result = []
    que = deque()

    for i in range(1, N1):
        if indegree[i] == 0:
            que.append(i)
    
    while que:
        node = que.popleft()
        result.append(node)

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                que.append(i)

    return result

def solution(data, N1):

    indegree = [0] * N1
    graph = [[] for _ in range(N1)]

    for a, b in data:
        graph[a].append(b)
        indegree[b] += 1

    return topology_sort(N1, indegree, graph)



def main():

    n = 7

    data = [
        [1, 2],
        [1, 5],
        [2, 3],
        [2, 6],
        [3, 4],
        [4, 7],
        [5, 6],
        [6, 4],
    ]

    assert solution(data, n+1) == [1, 2, 5, 3, 6, 4, 7]


if __name__ == "__main__":
    main()