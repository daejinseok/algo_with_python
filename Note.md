
# 시간 측정

```python
import time
start_time = time.time()

end_time = time.time()
print("time:", end_time - start_time)

```

```python

>>> [0] * 10
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

>>> [i for i in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> [i for i in range(10) if i % 2 == 0]
[0, 2, 4, 6, 8]

>>> [[0] * 5 for _ in range(4)]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

>>> list(map(int, '123'))
[1, 2, 3]

```