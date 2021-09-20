import time

N = 10000000

start_time = time.time()

group = list(range(N))

end_time = time.time()
print("time:", end_time - start_time)


start_time = time.time()

parent = [0] * (N)
for i in range(1, N):
    parent[i] = i

end_time = time.time()
print("time:", end_time - start_time)
