import pygame
#!/usr/bin/python

pygame.init()

# Tạo cửa sổ trò chơi
screen = pygame.display.set_mode((800, 400))

# Tạo font cho văn bản
font = pygame.font.Font(None, 36)
WHITE = (255,255,255)
# Tạo danh sách các ô văn bản
text_boxes = []
buttons = []

# Thay đổi levels, maps, al tại đây 
levels = ["Easy", "Medium", "Hard"]
selected_level = 0
len_level = len(levels)
maps = ["Map 1", "Map 2", "Map 3"]
selected_map = 0
len_map = len(maps)
algorithms = ["DFS", "A*", "Noen"]
selected_algorithm = 0
len_algorithm = len(algorithms)


#button
class Button2:
    def __init__(self, text, x, y,enable):
        self.text = text
        self.x = x
        self.y = y
        self.enable = enable
        self.draw()
        
    def draw(self):
        bt_text = font.render(self.text,True,WHITE)
        bt_rect = pygame.rect.Rect((self.x,self.y), (140, 60))   
        if self.enable:
            if self.check_list():
                pygame.draw.rect(screen,"dark gray", bt_rect, 0, 5)
            else:
                pygame.draw.rect(screen,"light gray", bt_rect, 0, 5)
        else:
            pygame.draw.rect(screen,"black", bt_rect, 0, 5)
        
        pygame.draw.rect(screen, 'gray', bt_rect, 0, 5)
        pygame.draw.rect(screen, 'black', bt_rect, 2, 5)
        screen.blit(bt_text,(self.x+3,self.y+3))

    def check_list(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        bt_rect = pygame.rect.Rect((self.x,self.y), (140, 60))
        if left_click and bt_rect.collidepoint(mouse_pos) and self.enable :
            return True
        else: 
            return False


class Button:
    def __init__(self,  text, x, y,enable):
        self.text = text
        self.x = x
        self.y = y
        self.enable = enable
        self.draw()
        
    def draw(self):
        bt_text = font.render(self.text,True,WHITE)
        self.bt_rect = pygame.rect.Rect((self.x,self.y), (60, 30))   
        pygame.draw.rect(screen, 'gray', self.bt_rect, 0, 5)
        pygame.draw.rect(screen, 'black', self.bt_rect, 2, 5)
        screen.blit(bt_text,(self.x+3,self.y+3))
    
    def is_clicked(self, event):
        return self.bt_rect.collidepoint(event.pos)


# Define draw_text function
def draw_text(text, font, text_color, x, y):
    imgx = font.render(text, True, text_color)
    screen.blit(imgx, (x, y))
    return imgx

def draw_menu():
    Name_game = draw_text("Pac Man AI", font, WHITE, 340, 70)
    
    text_surface1 = draw_text("Level", font, WHITE, 280, 150)
    
    text_level_down = font.render("<", True, (255, 255, 255))
    text_level_down_rect = text_level_down.get_rect()
    text_level_down_rect.center = (370, 160)
    text_boxes.append({"text": "Level", "rect": text_level_down_rect,"action":"down"})
    screen.blit(text_level_down,text_level_down_rect)
    
    text_listlevel = font.render(f"{levels[selected_level]}", True, WHITE)
    screen.blit(text_listlevel, (436, 150))
    
    text_level_up = font.render(">", True, (255, 255, 255))
    text_level_up_rect = text_level_up.get_rect()
    text_level_up_rect.center = (570, 160)
    text_boxes.append({"text": "Level", "rect": text_level_up_rect,"action":"up"})
    screen.blit(text_level_up,text_level_up_rect)
    
   
    
    
    text_surface2 = draw_text("Map", font, WHITE, 290, 200)
    
    text_map_down = font.render("<", True, (255, 255, 255))
    text_map_down_rect = text_map_down.get_rect()
    text_map_down_rect.center = (370, 210)
    text_boxes.append({"text": "map", "rect": text_map_down_rect,"action":"down"})
    screen.blit(text_map_down,text_map_down_rect)
    
    text_listmap = font.render(f"{maps[selected_map]}", True, WHITE)
    screen.blit(text_listmap, (436, 200))
    
    text_map_up = font.render(">", True, (255, 255, 255))
    text_map_up_rect = text_map_up.get_rect()
    text_map_up_rect.center = (570, 210)
    text_boxes.append({"text": "map", "rect": text_map_up_rect,"action":"up"})
    screen.blit(text_map_up,text_map_up_rect)


    text_surface3 = draw_text("Algorithm", font, WHITE, 223, 250)
    
    text_algorithm_down = font.render("<", True, (255, 255, 255))
    text_algorithm_down_rect = text_algorithm_down.get_rect()
    text_algorithm_down_rect.center = (370, 260)
    text_boxes.append({"text": "algorithm", "rect": text_algorithm_down_rect,"action":"down"})
    screen.blit(text_algorithm_down,text_algorithm_down_rect)
    
    text_listalgorithm = font.render(f"{algorithms[selected_algorithm]}", True, WHITE)
    screen.blit(text_listalgorithm, (436, 250))
    
    text_algorithm_up = font.render(">", True, (255, 255, 255))
    text_algorithm_up_rect = text_algorithm_up.get_rect()
    text_algorithm_up_rect.center = (570, 260)
    text_boxes.append({"text": "algorithm", "rect": text_algorithm_up_rect,"action":"up"})
    screen.blit(text_algorithm_up,text_algorithm_up_rect)
    
    global bt_run  
    button_start = Button("RUN", 360, 360, True)
    buttons.append(button_start)


def start_game():
    # Initialize the game with the selected options
    print("Starting the game with the following options:")
    print("Level:", levels[selected_level])
    print("Screen:", maps[selected_map])
    print("Algorithm:", algorithms[selected_algorithm])
    

running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for box in text_boxes:
                if box["rect"].collidepoint(event.pos):
                    if box["action"]=='up' and box["text"]=="Level":
                        print(f"Đã click vào up level")
                        if selected_level == len_level - 1:
                            break;
                        else: 
                            selected_level +=1;
                        break;
                    elif box["action"]=='down' and box["text"]=="Level":
                        print(f"Đã click vào down level")
                        if selected_level == 0:
                            break;
                        else: 
                            selected_level -= 1;
                        break;
                    elif box["action"]=='up' and box["text"]=="map":
                        print(f"Đã click vào up level")
                        if selected_map == len_map - 1:
                            break;
                        else: 
                            selected_map +=1;
                        break;
                    elif box["action"]=='down' and box["text"]=="map":
                        print(f"Đã click vào down level")
                        if selected_map == 0:
                            break;
                        else: 
                            selected_map -= 1;
                        break;
                    elif box["action"]=='up' and box["text"]=="algorithm":
                        print(f"Đã click vào up level")
                        if selected_algorithm == len_algorithm - 1:
                            break;
                        else: 
                            selected_algorithm +=1;
                        break;
                    elif box["action"]=='down' and box["text"]=="algorithm":
                        print(f"Đã click vào down level")
                        if selected_algorithm == 0:
                            break;
                        else: 
                            selected_algorithm -= 1;
                        break;
                    else:
                        pass
            
            for button in buttons:
                if button.is_clicked(event):
                    start_game()
                    running = False
                    break;
            
                
            
            
    screen.fill((52, 78, 91))
    draw_menu()
    

    pygame.display.flip()

pygame.quit()
