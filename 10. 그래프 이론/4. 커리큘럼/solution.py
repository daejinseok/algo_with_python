from collections import deque
import copy


def topology_sort(N1, time, graph, indegree):

    out = copy.deepcopy(time)
    que = deque()

    print(graph)
    print(indegree)
    for idx in range(1, N1):
        if indegree[idx] == 0:
            print(idx)
            que.append(idx)

    while que:
        now = que.popleft()
        for xx in graph[now]:

            print(f"now : {now}")
            print(f"xx : {xx}")
            print(f"out : {out}")

            indegree[xx] -= 1
            out[xx] = max(out[xx], out[now]+time[xx])

            print(f"out : {out}")
            if indegree[xx] == 0:
                que.append(xx)
    print(out)
    return out[1:]


def solution(n, data):

    N1 = n + 1

    graph = [[] for _ in range(N1)]
    indegree = [0] * N1
    time = [0] * N1

    for idx, xx in enumerate(data):
        time[idx+1] = xx[0]
        for x in xx[1:-1]:
            graph[x].append(idx+1)
            indegree[idx+1] += 1

    return topology_sort(N1, time, graph, indegree)


def main():

    n = 5
    data = [
        [10, -1],
        [10, 1, -1],
        [4, 1, -1],
        [4, 3, 1, -1],
        [3, 3, -1],
    ]

    assert solution(n, data) == [10, 20, 14, 18, 17]


if __name__ == "__main__":
    main()
