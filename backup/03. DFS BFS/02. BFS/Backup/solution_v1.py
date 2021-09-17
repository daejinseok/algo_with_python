from collections import deque

def solution(m):


    def bfs(idx):

        nonlocal m

        visited = [idx]
        queue = deque([idx])

        while queue:
            v = queue.popleft()

            for i in m[v]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

        return visited

    return bfs(1)
