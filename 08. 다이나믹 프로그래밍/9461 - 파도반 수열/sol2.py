# 파도반 수열 다국어
# https://www.acmicpc.net/problem/9461

import sys

n = int(sys.stdin.readline())

t = [-1]*100
t[0] = 1
t[1] = 1
t[2] = 1
t[3] = 2
t[4] = 2
t[5] = 3
t[6] = 4
t[7] = 5
t[8] = 7

for i in range(9, 100):
    t[i] = t[i-2] + t[i-3]

for _ in range(n):
    i = int(sys.stdin.readline())
    print(t[i-1])
