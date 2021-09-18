import sys

INF = sys.maxsize

def solution(data, start, end):

    out = [INF] * (end + 1);

    out[start] = 0

    for s, p, w in data:
        if s == start:
            out[p] = w
    
    done = {0, start}

    print(out)

    while True:
        start_node = next(out, done)
        if start_node == None:
            break

        print(f"start_node : {start_node}")
        start_weight = out[start_node]

        for s, p, w in data:
            if s == start_node:
                if out[p] > (start_weight + w):
                    out[p] = start_weight + w
        done.add(start_node)
        print(out)

    return out[1:]


def next_node_list(out, done):
    for i, v in enumerate(out):
        if v != INF and i not in done:
            yield (i, v)


def next(out, done):

    min_idx = None
    min_val = INF

    for i, v in next_node_list(out, done):
        if min_val > v:
            min_idx = i
            min_val = v

    return min_idx





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