

def find_root(group, a):
    if group[a] == a:
        return a
    group[a] = find_root(group, group[a])
    return group[a]

def union(group, a, b):
    root_a = find_root(group, a)
    root_b = find_root(group, b)

    if root_a < root_b:
        group[root_b] = root_a
    else:
        group[root_a] = root_b


def solution(n , data):

    group = list(range(n+1))

    out = []
    for cmd, a, b in data:
        if cmd == 0:
            union(group, a, b)
        if cmd == 1:
            ra = find_root(group, a)
            rb = find_root(group, b)

            if ra == rb:
                out.append('YES')
            else:
                out.append('NO')

    return out


def main():

    n = 7

    data = [
        [0, 1, 3],
        [1, 1, 7],
        [0, 7, 6],
        [1, 7, 1],
        [0, 3, 7],
        [0, 4, 2],
        [0, 1, 1],
        [1, 1, 1],
    ]

    assert solution(n, data) == ['NO', 'NO', 'YES']

if __name__ == "__main__":
    main()