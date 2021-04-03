
d = []
d.append(1)
d.append(1)


def fibo(x):

    if len(d) > x:
        return d[x-1]
    
    for i in range(len(d)-1, x):
        d.append(d[i] + d[i-1])

    return d[x-1]

