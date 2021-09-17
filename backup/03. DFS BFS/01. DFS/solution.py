# https://www.youtube.com/watch?v=5Lu34WIx2Us

def solution(m):

    visited = []
    
    def dfs(idx):

        nonlocal visited
        nonlocal m

        visited.append(idx)
        for midx in m[idx]:
            if midx not in visited:
                dfs(midx)

    dfs(1)

    return visited
            


