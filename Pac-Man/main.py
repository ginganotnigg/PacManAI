from search import *
import pygame
import time
from menuBar import *


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

def endPos(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                return (i, j)
    return
    

# Init variables

pygame.init()
WIDTH = 750
HEIGHT = 800
MAPS_PER_LVL = 5
pt = ((HEIGHT - 50) // 25) # = (WIDTH // 25)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
maps = read_file('map.txt')
counter = 0
score = 0
time = 0 
length = 0
pac_img = []
frame_count = 0
frame_delay = 5
run = True
game_over = False
for i in range(1, 5):
    pac_img.append(pygame.transform.scale(pygame.image.load(f'assets/{i}.png'), (30, 30)))
mons_img = pygame.transform.scale(pygame.image.load(f'assets/pink.png'), (26, 26))


# Function

def draw_board(mp):
    screen.fill('black')
    for i in range(len(mp)):
        for j in range(len(mp[i])):
            if mp[i][j] == 1:
                pygame.draw.rect(screen, 'blue', pygame.Rect(j * pt + 2, i * pt + 2, pt - 4, pt - 4))
            if mp[i][j] == 2:
                pygame.draw.circle(screen, 'white', ((j + 0.5) * pt, (i + 0.5) * pt), 6)
            if mp[i][j] == 3:
                screen.blit(mons_img, (j * pt + 2, i * pt + 2))
            if mp[i][j] == 4:
                screen.blit(pac_img[(counter % 60) // 15], (j * pt, i * pt))

def draw_text():
    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (100, 770))
    time_text = font.render(f'Time: {time}', True, 'white')
    screen.blit(time_text, (325, 770))
    length_text = font.render(f'Length: {length}', True, 'white')
    screen.blit(length_text, (565, 770))


def draw_visited(start, path, visited, end):
    pygame.draw.circle(screen, 'red', ((start[1] + 0.5) * pt, (start[0] + 0.5) * pt), 5)
    for x in visited:
        if x != end and x != start and x != path:
            pygame.draw.circle(screen, 'cyan', ((x[1] + 0.5) * pt, (x[0] + 0.5) * pt), 3)

def draw_path(path, end):
    for x in path:
        if x != end:
            pygame.draw.circle(screen, 'yellow', ((x[1] + 0.5) * pt, (x[0] + 0.5) * pt), 3)


# Execute

def inc_counter(counter):    
    if counter < 60:
        counter += 1
    else: 
        counter = 0
        if not game_over: time += 1

def solve(lvl, mapIdx, algoIdx):
    mp = maps[(lvl - 1) * MAPS_PER_LVL + mapIdx - 1]
    pacman_pos = startPos(mp)
    end = endPos(mp)
    if algoIdx == 1:
        path, visited = A_star(pacman_pos, end, mp)
    elif algoIdx == 2:
        path, visited = BFS(pacman_pos, end, mp)
    elif algoIdx == 2:
        path, visited = GBFS(pacman_pos, end, mp)
    else:
        path, visited = DFS(pacman_pos, end, mp)
    cost = len(visited)
    return mp, pacman_pos, end, path, visited, cost

lvl, mapIdx, algo = start_game_params()
mp, pacman_pos, end, path, visited, cost = solve(lvl, mapIdx, algo)
start = pacman_pos
saved_path = path.copy()
len_path = len(path)

while run:
    timer.tick(fps)
    if counter < 60:
        counter += 1
    else: 
        counter = 0
        if not game_over: time += 1

    draw_board(mp)
    draw_text()
    draw_visited(start, saved_path, visited, end)
    
    if len(path) > 0 and frame_count >= frame_delay:
        current_cell = path.pop(0)
        mp[pacman_pos[0]][pacman_pos[1]] = 0
        mp[current_cell[0]][current_cell[1]] = 4
        pacman_pos = current_cell
        frame_count = 0
        if current_cell == end:
            game_over = True
            draw_path(saved_path, end)
            score -= cost
            length += len_path
            time += float("{:.3f}".format(counter / 60))
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    pygame.time.delay(2)
pygame.quit()