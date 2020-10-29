from functools import reduce

def calc(arr, cut):

    def l(acc, cur):
        v = cur - cut
        return acc + ( v >= 0 and v or 0 )

    return reduce(l, arr, 0)

def solution(arr, m):

    a_max = max(arr)
    a_min = 0

    while (a_max - a_min) != 1 :

        a_cur = round((a_max + a_min) / 2)
        print(a_cur)

        if calc(arr, a_cur) > m :
            a_min = a_cur
        else :
            a_max = a_cur

    return calc(arr, a_max) >= m and a_max or a_min

out = solution([19, 15, 10, 17], 6)
print(out)
assert  out == 15