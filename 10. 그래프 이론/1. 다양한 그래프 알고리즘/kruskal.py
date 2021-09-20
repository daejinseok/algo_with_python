
"""
Spanning Tree (신장 트리)
하나의 그래프가 있을 때 모든 노드를 포함하면서
사이클이 존재하지 않는 부분 그래프

최소 신장 트리를 구하는 방법 중 하나가 Kruskal Algorithm
"""

def find_p(p, a):
    if p[a] == a:
        return a
    
    p[a] = find_p(p, p[a])
    return p[a]

def union(p, a, b):
    pa = find_p(p, a)
    pb = find_p(p, b)

    if pa < pb:
        p[pb] = pa
    else:
        p[pa] = pb


def solution(data, n):

    N1 = n + 1

    edges = []
    for a, b, cost in data:
        edges.append((cost, a, b))
    edges.sort()

    # parent 부모
    p = list(range(N1))

    sum = 0
    for cost, a, b in edges:
        print('---------------------')

        pa = find_p(p, a)
        pb = find_p(p, b)

        print(a, b)
        print(pa, pb)
        print(p)

        if pa == pb:
            continue

        union(p, a, b)
        sum += cost
        print(p)

    print(sum)
    return sum


def main():

    data = [
        [1, 2, 29],
        [1, 5, 75],
        [2, 3, 35],
        [2, 6, 34],
        [3, 4, 7],
        [4, 6, 23],
        [4, 7, 13],
        [5, 6, 53],
        [6, 7, 25],
    ]

    assert solution(data, 7) == 159

if __name__ == "__main__":
    main()