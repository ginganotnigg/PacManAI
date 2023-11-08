# Read file

def read_file(file_path): 
    maps = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        size = []
        matrix = []
        coordinate = []
        for line in lines:
            line = line.strip()
            if line:
                if len(size) == 0:
                    size = list(map(int, line.split()))
                elif len(matrix) < size[0]:
                    matrix.append(list(map(int, line.split())))
                else:
                    coordinate = list(map(int, line.split()))
                    matrix[coordinate[0]][coordinate[1]] = 4
                    maps.append(matrix)
                    size = []
                    matrix = []
                    coordinate = []
    return maps


# Read boards

def startPos(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 4:
                return (i, j)
    return

def foodPos(board):
    foods = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                foods.append((i, j))
    return foods


# Algorithm

def min_distance(start, end, board, algo):
    dis = {}
    for i in end:
        dis[i] = len(algo(start, i, board)[0])
    return sorted(dis, key=dis.get)[0]

def solve_lv3(start, end, board, algo):
    visited = []
    path = [start]
    current = start
    while end != []:
        i = min_distance(current, end, board, algo)
        a, b, current = algo(current, i, board)
        path.extend(a)
        visited.extend(b)
        last = i
        end.remove(i)
    return path, visited, last
