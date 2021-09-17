d = []

def fibo(x):

    print(len(d), x)

    if len(d) >= x:
        return d[x-1]

    if x == 1 or x == 2:
        d.append(1)
    else:
        d.append(fibo(x-2) + fibo(x-1) )

    return d[x-1]
