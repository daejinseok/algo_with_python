import sys


def find_root(group, a):
    if group[a] == a:
        return a

    group[a] = find_root(group, group[a])
    return group[a]


def union(group, root_a, root_b):

    if root_a < root_b:
        group[root_b] = root_a
    else:
        group[root_a] = root_b


def solution():

    input = sys.stdin.readline
    n, e = map(int, input().split())

    edge = []
    for _ in range(e):
        edge.append(tuple(map(int, input().split())))
    edge.sort(key=lambda x: x[2])

    group = list(range(n+1))

    sum = 0
    max = 0
    count = 0
    n_1 = n - 1

    for a, b, cost in edge:

        root_a = find_root(group, a)
        root_b = find_root(group, b)

        if root_a == root_b:
            continue

        union(group, root_a, root_b)
        sum += cost
        max = cost
        count += 1

        # 크루스칼 알고리즘에서 간선의 개수는 노드의 개수 -1 과 같음
        if count == n_1:
            break

    return sum - max


print(solution())
