import random
from search import *

def monsters_dict(board): #make dict
    monsters = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 3:
                monsters[(i, j)] = nextPos((i, j), board)
    return monsters

def move_monster(monsters, board): #thay doi dau +
    for key in monsters.keys():
        if board[key[0]][key[1]] == 3:
            board[key[0]][key[1]] = 5
            next_cell = monsters[key][random.randint(0, len(monsters[key]) - 1)]
            board[next_cell[0]][next_cell[1]] = 3
        elif board[key[0]][key[1]] == 5:
            board[key[0]][key[1]] = 3
            for value in monsters[key]:
                board[value[0]][value[1]] = 5
    return board

def change_map(mp):
    for i in range(len(mp)):
        for j in range(len(mp[0])):
            if mp[i][j] == 3:
                for k in nextPos((i, j), mp):
                    mp[k[0]][k[1]] = 5

def move(mon, monsters_dict):
    temp = mon
    for i in range(0, 4): #so luong buoc chay
        x = move_monster(monsters_dict, temp)
        temp = x

