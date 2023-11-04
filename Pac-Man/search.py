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
    