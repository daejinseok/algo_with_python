def solution(arr, m):

    start = 0
    end = max(arr)
    out = 0

    while start <= end :

        mid = (start + end) // 2
        print(start, mid, end)

        total = 0
        for x in arr:
            if x > mid :
                total += x - mid
            if total > m:
                break
        
        if total < m :
            end = mid - 1
        else :
            out = mid
            start = mid + 1

    return out

out = solution([19, 15, 10, 17], 6)
print(out)
assert  out == 15