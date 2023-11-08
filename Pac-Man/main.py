from search import *
from menuBar import *
from util import *
from monster import *
import pygame
import time


# Read file
    

# Init variables

pygame.init()
WIDTH = 750
HEIGHT = 800
MAPS_PER_LVL = 5
pt = ((HEIGHT - 50) // 25) # = (WIDTH // 25)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('PACMAN - MAIN')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
maps = read_file('map.txt')
algorithms = [DFS, A_star, BFS, GBFS]
counter = 0
score = 0
time = 0 
cost = 0
pac_img = []
frame_count = 0
frame_delay = 10
run = True
game_over = False
for i in range(1, 5):
    pac_img.append(pygame.transform.scale(pygame.image.load(f'assets/{i}.png'), (30, 30)))
food_img = pygame.transform.scale(pygame.image.load(f'assets/apple.svg'), (30, 30))
mons_img = pygame.transform.scale(pygame.image.load(f'assets/pink.png'), (26, 26))


# Function

def draw_board(mp):
    for i in range(len(mp)):
        for j in range(len(mp[i])):
            if mp[i][j] == 1:
                pygame.draw.rect(screen, 'blue', pygame.Rect(j * pt + 2, i * pt + 2, pt - 4, pt - 4))
            if mp[i][j] == 2:
                screen.blit(food_img, (j * pt + 2, i * pt))
            if mp[i][j] == 3:
                screen.blit(mons_img, (j * pt + 2, i * pt + 2))
            if mp[i][j] == 4:
                screen.blit(pac_img[(counter % 60) // 15], (j * pt, i * pt))

def draw_text():
    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (100, 770))
    time_text = font.render(f'Time: {time}', True, 'white')
    screen.blit(time_text, (325, 770))
    cost_text = font.render(f'Cost: {cost}', True, 'white')
    screen.blit(cost_text, (565, 770))


def draw_visited(start, path, visited, end):
    pygame.draw.circle(screen, 'green', ((start[1] + 0.5) * pt, (start[0] + 0.5) * pt), 5)
    for x in visited:
        if x != end and x != start and x != path:
            pygame.draw.circle(screen, 'cyan', ((x[1] + 0.5) * pt, (x[0] + 0.5) * pt), 3)

def draw_path(start, path, end):
    for x in path:
        if x != end and x != start:
            pygame.draw.circle(screen, 'yellow', ((x[1] + 0.5) * pt, (x[0] + 0.5) * pt), 5)


# Execute

def inc_counter():
    global counter, time    
    if counter < 60:
        counter += 1
    else: 
        counter = 0
        if not game_over: time += 1

def solve(lvl, mapIdx, algoIdx):
    mons_dict = {} # For level 3
    mp = maps[(lvl - 1) * MAPS_PER_LVL + mapIdx - 1]
    algo = algorithms[algoIdx]
    pacman_pos = startPos(mp)
    food = foodPos(mp)
    if lvl < 3:
        path, visited, _ = algo(pacman_pos, food[0], mp)
        last = food[0]
    elif lvl == 3:
        mons_dict = monsters_dict(mp)
        change_map(mp)
        path, visited, last = solve_lv3(pacman_pos, food, mp, algo)

    return mp, pacman_pos, last, path, visited, mons_dict

def get_score():
    global frame_count, pacman_pos, game_over, visited, counter, mons_dict, current_cell, path, score, cost, time, mp
    if len(path) > 0 and frame_count >= frame_delay:
        current_cell = path.pop(0)
        mp[pacman_pos[0]][pacman_pos[1]] = 0
        mp[current_cell[0]][current_cell[1]] = 4
        pacman_pos = current_cell
        frame_count = 0
        if lvl == 3: mp = move_monster(mons_dict, mp)
        if current_cell == last:
            game_over = True
            score -= len(saved_path)
            score += 20 * len_food
            cost += len(visited)
            time += float("{:.3f}".format(counter / 60))
    frame_count += 1

lvl, mapIdx, algo = start_game_params()
mp, pacman_pos, last, path, visited, mons_dict = solve(lvl, mapIdx, algo)
start = pacman_pos

len_food = len(foodPos(mp))
saved_path = [x for x in path]

while run:
    timer.tick(fps)
    inc_counter()

    screen.fill('black')
    draw_text()
    draw_visited(start, saved_path, visited, last)
    draw_path(start, saved_path, last)
    draw_board(mp)

    get_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    pygame.time.delay(2)
pygame.quit()