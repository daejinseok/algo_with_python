
def solution(data, n):

    N1 = n+1

    group = list(range(N1))

    for p1, p2 in data:

        pm = min( find_p(p1, group), find_p(p2, group) )

        group[p1] = pm
        group[p2] = pm

        print(group)

    out = []
    for p in group:
        out.append(find_p(p, group))

    return out[1:]


def find_p(p, group):
    if p == group[p]:
        return p

    group[p] = find_p(group[p], group)
    return group[p]



def main():

    n = 6

    data = [
        [1, 4],
        [2, 3],
        [2, 4],
        [5, 6],
    ]

    out = [1, 1, 1, 1, 5, 5]

    assert solution(data, n) == out

if __name__ == "__main__":
    main()