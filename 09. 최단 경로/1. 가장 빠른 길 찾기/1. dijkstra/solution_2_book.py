import sys

INF = sys.maxsize
N = 6
N1 = N + 1

def solution(data, start, end):

    graph = [[] for i in range(N1)] 
    visited = [False] * (N1)
    distance = [INF] * (N1)

    for s, e, w in data:
        graph[s].append((e, w))

    dijkstra(start, graph, visited, distance)

    print(distance)
    return distance[1:]



def get_smallest_node(distance, visited):

    min_value = INF
    index = 0

    for i in range(1, N1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start, graph, visited, distance):

    distance[start] = 0
    visited[start] = True

    for e, w in graph[start]:
        distance[e] = w
    
    for _ in range(N-1):
        now = get_smallest_node(distance, visited)
        visited[now] = True

        for e, w in graph[now]:
            cost = distance[now] + w
            if cost < distance[e]:
                distance[e] = cost

        print(now, visited, distance)



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