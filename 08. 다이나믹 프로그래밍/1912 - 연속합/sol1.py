# 연속합
# https://www.acmicpc.net/problem/1912


def sol1(arr, n):

    m = arr[0]
    cur = m

    for i in range(1, n):
        if cur > 0 and (cur + arr[i]) > 0:
            cur = cur + arr[i]
        else:
            cur = arr[i]

        if m < cur:
            m = cur
    return m


n = int(input())
arr = list(map(int, input().split()))
print(sol1(arr, n))
