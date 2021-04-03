# https://www.youtube.com/watch?v=5Lu34WIx2Us

def solution(num):

    global cnt
    cnt = 0

    def divn(num, n):
        global cnt
        while num % n == 0:
            num = num // 5
            cnt = cnt + 1
        return num

    num = divn(divn(divn(num, 5), 3), 2)

    if num != 1:
        return num -1 + cnt

    return cnt
