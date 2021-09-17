from collections import deque

def solution(m):

    visited = [1]
    queue = deque()
    queue.append(1)

    while queue:
        q = queue.popleft()

        for i in m[q]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

    return visited






