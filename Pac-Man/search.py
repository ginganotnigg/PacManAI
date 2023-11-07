def nextPos(rc, board):
    row = rc[0]
    col = rc[1]
    arr = []
    if row - 1 >= 0 and board[row - 1][col] in (0, 2):
        arr.append((row - 1, rc[1]))
    if row + 1 <= len(board) - 1 and board[row + 1][col] in (0, 2):
        arr.append((row + 1, rc[1]))
    if col - 1 >= 0 and board[row][col - 1] in (0, 2):
        arr.append((rc[0], col - 1))
    if col + 1 <= len(board[0]) - 1 and board[row][col + 1] in (0, 2):
        arr.append((rc[0], col + 1))
    return arr

def min_list(a):
    minn = a[0]
    for i in a:
        if i < minn:
            minn = i
    return minn

#BFS
def BFS(start, end, board):
    browse = []
    temp = [start]
    visited = [start]
    prev={}
    while end not in browse:
        browse.extend(temp)
        temp2 = []
        for i in temp:
            for j in nextPos(i, board):
                if j not in visited:
                    temp2.append(j)
                    visited.append(j)
                    prev[j] = i
        temp = temp2
    path = [end]
    while start not in path:
        path.append(prev[path[len(path)-1]])
    path.reverse()
    return path, visited

#GBFS
def GBFS(start, end, board):
    h_array = []
    visited = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[0])):
            if board[i][j] != 1:
                row.append(float((end[0] - i)**2 + (end[1] - j)**2)**0.5)
            else:
                row.append(9999)
        h_array.append(row)
        
    openn = [start]
    close = []
    prev={}
    while openn != []:
        list = []
        for i in openn:
            list.append(h_array[i[0]][i[1]])
        p = ''
        for i in openn:
            if h_array[i[0]][i[1]] == min_list(list):
                p = i
                break
        openn.remove(p)
        close.append(p)
        if p == end:
            break
        for i in nextPos(p, board):
            if i not in openn and i not in close:
                openn.append(i)
                visited.append(i)
                prev[i] = p
    path = [end]
    while start not in path:
        path.append(prev[path[len(path)-1]])
    path.reverse()
    return path, visited
        

#A_star
def A_star(start, end, board):
    f_array = []
    visited = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[0])):
            if board[i][j] != 1:
                h = float((end[0] - i)**2 + (end[1] - j)**2)**0.5
                g = abs(start[0] - i) + abs(start[1] - j)
                row.append(h + g)
            else:
                row.append(9999)
        f_array.append(row)
    openn = [start]
    close = []
    prev={}
    while openn != []:
        list = []
        for i in openn:
            list.append(f_array[i[0]][i[1]])
        p = ''
        for i in openn:
            if f_array[i[0]][i[1]] == min_list(list):
                p = i
                break
        openn.remove(p)
        close.append(p)
        if p == end:
            break
        for i in nextPos(p, board):
            if i not in openn and i not in close:
                openn.append(i)
                visited.append(i)
                prev[i] = p
    path = [end]
    while start not in path:
        path.append(prev[path[len(path)-1]])
    path.reverse()
    return path, visited

#DFS
def DFS_run(start, end, visited, board, prev):
    visited.append(start)
    for v in nextPos(start, board):
        if v not in visited:
            prev[v] = start
            if v == end:
                return
            DFS_run(v, end, visited, board, prev)

def DFS(start, end, board):
    visited = [start]
    prev = {}
    DFS_run(start, end, visited, board, prev)
    path = [end]
    while start not in path:
        path.append(prev[path[len(path)-1]])
    path.reverse()
    return path, visited