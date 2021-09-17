# 1로 만들기

# https://www.youtube.com/watch?v=5Lu34WIx2Us

def solution(num):

    def divn(num, n):

        if num % n != 0:
            return -1

        return num // n

    def process(l1):

        l2 = []

        for num in l1:
            for n in [5, 3, 2]:
                r = divn(num, n)
                if r == 1:
                    return []
                if r != -1:
                    l2.append(r)

            r = num - 1
            if r == 1:
                return []
            else:
                l2.append(r)

        return l2

    l1 = [num]
    c = 0        
    while l1 != []:
        l1 = process(l1)
        c = c+1
    return c



if __name__ == "__main__":
	main()




