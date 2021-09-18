from heapq import *

a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heap = []

for value in a:
    heappush(heap, value)
    print(heap)

a = [
    (5, 'write code'),
    (7, 'release product'),
    (1, 'write spec'),
    (3, 'create tests'),
    (1, 'write spec'),
]
heap = []

# 배열을 heap하게 변경
print('list를 heap으로 변경')
heapify(a)
print(a)

# 제거하지 않고 값 확인
print('root를 제거하지않고 root갑 확인')
print(a[0])
print(a)

# 제거
print('root를 팝')
print(a)
print(heappop(a))
print(a)
