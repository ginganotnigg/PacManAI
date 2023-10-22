from board import boards
import pygame


# Init variables

pygame.init()
WIDTH = 750
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards
counter = 0
score = 0
length = 0
pac_img = []
for i in range(1, 5):
    pac_img.append(pygame.transform.scale(pygame.image.load(f'assets/{i}.png'), (30, 30)))
mons_img = pygame.transform.scale(pygame.image.load(f'assets/pink.png'), (30, 30))


# Function

def draw_board():
    pt = ((HEIGHT - 50) // 25) # = (WIDTH // 25)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.rect(screen, 'blue', pygame.Rect(j * pt, i * pt, pt, pt))
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', ((j + 0.5) * pt, (i + 0.5) * pt), 6)
            if level[i][j] == 3:
                screen.blit(mons_img, (j * pt, i * pt))
            if level[i][j] == 4:
                screen.blit(pac_img[counter // 5], (j * pt, i * pt))

def draw_text():
    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (100, 770))
    length_text = font.render(f'Length: {length}', True, 'white')
    screen.blit(length_text, (570, 770))


# Execute

run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
    else: counter = 0
    screen.fill('black')
    draw_board()
    draw_text()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()