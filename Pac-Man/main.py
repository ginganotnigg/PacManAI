from search import BFS
import pygame
import time



# Read file

def readFile(fileName):
    board = []
    mapFile = open(fileName, 'r')
    head = mapFile.readline()
    row = int(head.split(' ')[0])
    for i in range(row):
        line = mapFile.readline()
        temp = [int(item) for item in line.split(' ')]
        board.append(temp)
    foot = mapFile.readline()
    pacX = int(foot.split(' ')[0])
    pacY = int(foot.split(' ')[1])
    board[pacX][pacY] = 4
    return board


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
pt = ((HEIGHT - 50) // 25) # = (WIDTH // 25)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = readFile('map.txt')
counter = 0
score = 0
time = 0 
length = 0
pac_img = []
for i in range(1, 5):
    pac_img.append(pygame.transform.scale(pygame.image.load(f'assets/{i}.png'), (30, 30)))
mons_img = pygame.transform.scale(pygame.image.load(f'assets/pink.png'), (26, 26))


# Function

def draw_board():
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.rect(screen, 'blue', pygame.Rect(j * pt + 2, i * pt + 2, pt - 4, pt - 4))
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', ((j + 0.5) * pt, (i + 0.5) * pt), 6)
            if level[i][j] == 3:
                screen.blit(mons_img, (j * pt + 2, i * pt + 2))
            if level[i][j] == 4:
                screen.blit(pac_img[(counter % 60) // 15], (j * pt, i * pt))
def draw_text():
    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (100, 770))
    time_text = font.render(f'Time: {time}', True, 'white')
    screen.blit(time_text, (330, 770))
    length_text = font.render(f'Length: {length}', True, 'white')
    screen.blit(length_text, (570, 770))


# Execute

pacman_pos = startPos(level)
end = endPos(level)
path = BFS(pacman_pos, end, level)
frame_count = 0
frame_delay = 5

run = True
game_over = False
while run:
    timer.tick(fps)
    if counter < 60:
        counter += 1
    else: 
        counter = 0
        if not game_over: time += 1
    screen.fill('black')
    draw_board()
    draw_text()

    if len(path) > 0 and frame_count >= frame_delay:
        current_cell = path.pop(0)
        level[pacman_pos[0]][pacman_pos[1]] = 0
        level[current_cell[0]][current_cell[1]] = 4
        pacman_pos = current_cell
        frame_count = 0
        if current_cell == end:
            game_over = True
            time += float("{:.3f}".format(counter / 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    frame_count += 1
    pygame.time.delay(2) # Pacman velocity
pygame.quit()
