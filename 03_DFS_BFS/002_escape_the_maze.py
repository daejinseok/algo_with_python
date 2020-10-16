"""
<문제> 미로 탈출

동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴
물이 있어 이를 피해 탈출해야 합니다.

동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸
씩 이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표
시되어 있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.

이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 칸을 셀 때
는 시작 칸과 마지막칸을 모두 포함해서 계산합니다.
"""

raw = """
101010
111111
000001
111111
111111
"""

def loga(a):
    for l in a:
        print(l)

data = []
for l in raw.split():
    data.append(list(map(int, l)))

N = len(data)
M = len(data[0])

# loga(data)

from collections import deque

def bfs(x, y):

    queue = deque([(x, y)])
    data[x][y] = 0

    c = 0
    while queue:
        p = queue.popleft()
        
        if addq(p[0]-1, p[1], queue):
            break
        if addq(p[0]+1, p[1], queue):
            break
        if addq(p[0], p[1]-1, queue):
            break
        if addq(p[0], p[1]+1, queue):
            break

        c = c + 1

    print(c)


def addq(x, y, queue):

    if x == (N-1) and y == (M-1):
        return True

    if x < 0 or (N-1) < x:
        return False
    if y < 0 or (M-1) < y:    
        return False

    print(x, y, queue)
    

    if data[x][y] == 1:
        queue.append((x, y))
        data[x][y] = 0
    
    return False

bfs(0,0)



