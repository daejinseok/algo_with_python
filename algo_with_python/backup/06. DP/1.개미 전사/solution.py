# https://www.youtube.com/watch?v=5Lu34WIx2Us

def solution(arr):

    # assert len(arr) > 2, '배열은 3 보다 커야 함'

    # d = []
    # d.append((arr[0], 0))
    # d.append((arr[1], arr[0]))

    # for i in range(2, len(arr)):
    #     d.append(( max(d[i-2]) + arr[i], max(d[i-1])))

    # return max(d[i])


    d = []
    d.append(arr[0])
    d.append(max(arr[0], arr[1]))

    for idx in range(2, len(arr)):
        d.append( max(d[idx-1], d[idx-2]+arr[idx]))

    return d[idx]