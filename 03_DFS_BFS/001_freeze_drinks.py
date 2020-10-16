'''
N * M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부
분은 1로 표시됩니다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 
서로 연결되어 있는 것으로 간주합니다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는
총 아이스크립의 개수를 구하는 프로그램을 작성하세요. 다음의 4*5 얼음 틀 예시에서
는 아이스크립이 총 3개 생성됩니다.
'''


input_data = \
    '00110' + '\n' + \
    '00011' + '\n' + \
    '11111' + '\n' + \
    '00000'

data = []
for d in input_data.split('\n'):
    data.append(list(d))
#print(data)

N = len(data)
M = len(data[0])

visited = [[False] * M for _ in range(N)]

#print(visited)

def get(x, y):
    if x < 0 or x > (N-1):
        return False
    if y < 0 or y > (M-1):
        return False

    return data[x][y] == '0'

# print(get(0,0))
# print(get(2,0))
# print(get(-1,0))

def graph(x, y):

    out = []

    if get(x-1, y):
        out.append((x-1, y))
    if get(x+1, y):
        out.append((x+1, y))
    if get(x, y-1):
        out.append((x, y-1))
    if get(x, y+1):
        out.append((x, y+1))

    return out

# print(graph(0,0))
# print(graph(1,0))


def dfs(x, y) :

    #print(x,y)
    visited[x][y] = True
    if data[x][y] == '1':
        return 0
    
    for i in graph(x, y):
        if not visited[i[0]][i[1]]:
            dfs(i[0], i[1])

    return 1    

# dfs(0, 0)
# print(visited)

count = 0
for i in range(N) :
    for j in range(M):
        if visited[i][j]:
            continue
        count += dfs(i, j)

print(count)




# dfs(0, 0)
# print(visited)




