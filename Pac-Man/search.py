def nextPos(rc): #rc: chuỗi lưu vị trí ban đầu
    row = int(rc[0])
    col = int(rc[1])
    arr = []
    if row - 1 >= 0 and boards[row - 1][col] == 0:
        arr.append(str(row - 1) + rc[1])
    if row + 1 <= len(boards) - 1 and boards[row + 1][col] == 0:
        arr.append(str(row + 1) + rc[1])
    if col - 1 >= 0 and boards[row][col - 1] == 0:
        arr.append(rc[0] + str(col - 1))
    if col + 1 <= len(boards) - 1 and boards[row][col + 1] == 0:
        arr.append(rc[0] + str(col - 1))
    return arr

def BFS(startPos, endPos, boards): #start/endPos: vị trí bắt đầu/đích
    path = [startPos]
    visited = [startPos]
    next = path
    while endPos not in path:
        nnext = []
        for i in next:
            for j in nextPos(i):
                if j not in visited:
                    nnext.append(j)
                    visited.append(j)
        for i in next:
            if endPos not in path:
                path.append(i)
            else:
                break
        next = nnext
    return path

def DFS_implement(path, visited, boards, pos, endPos):
    if pos not in visited:
        path.append(pos)
        visited.append(pos)
        if end in path:
            return path
        for i in nextPos(pos):
            DFS_implement(path, visited, boards, i, endPos)

def DFS(startPos, endPos, boards):
    visited = []
    path = []
    return DFS_implement(path, visited, boards, startPos, endPos)

#A_start
def min_list(a):
    minn = a[0]
    for i in a:
        if i < minn:
            minn = i
    return minn

def A_star(startPos, endPos, board):
    f_array = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[0])):
            if board[i][j] == 0 or board[i][j] == 2 or board[i][j] == 3:
                h = float((int(end[0]) - i)**2 + (int(end[1]) - j)**2)**0.5
                g = abs(int(start[0]) - i) + abs(int(start[1]) - j)
                row.append(h + g)
            else:
                row.append(9999)
        f_array.append(row)
    openn = [startPos]
    close = []
    prev={}
    while openn != []:
        list = []
        for i in openn:
            list.append(f_array[int(i[0])][int(i[1])])
        p = ''
        for i in openn:
            if f_array[int(i[0])][int(i[1])] == min_list(list):
                p = i
                break
        openn.remove(p)
        close.append(p)
        if p == end:
            break
        for i in nextPos(p):
            if i not in openn and i not in close:
                openn.append(i)
                prev[i] = p
    path = [end]
    while start not in path:
        path.append(prev[path[len(path)-1]])
    path.reverse()
    return path
