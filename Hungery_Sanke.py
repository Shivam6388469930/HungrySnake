# import random
# import pygame
# pygame.init()
# pygame.mixer.init()
# # colors
# white=(255,255,255)
# red=(255,0,0)
# black=(0,0,0)
# coral=(255,127,80)
# # window size

# window_width=1000
# window_hight=600
# Gamewindow=pygame.display.set_mode((window_width,window_hight))
# bgimg=pygame.image.load('snake.jpg')
# bgimg=pygame.transform.scale(bgimg,(window_width,window_hight)).convert_alpha()
# gameName=pygame.display.set_caption("HungrySnake")
# Gamewindow.fill(white)
# pygame.display.update()


# # creating spefic variable

# # clock
# clock=pygame.time.Clock()
# font=pygame.font.SysFont(None,55)

    
# def text_screen(text,color,x,y):
#     screen_text=font.render(text,True,color)
#     Gamewindow.blit(screen_text,[x,y])

# def plot_snake(Gamewindow,color,snk_list,snake_size):
#      for x,y in  snk_list:
#         pygame.draw.rect(Gamewindow,color,[x,y,snake_size,snake_size])

# def welcome():
#      exist_game=False
#      while not exist_game:
#           Gamewindow.fill(coral)
#           text_screen("Welcome! Press space bar to play game",black,150,300)
         
#           for event in pygame.event.get():
       
#                 if event.type==pygame.QUIT:
#                     exist_game=True
#                 if event.type==pygame.KEYDOWN:
#                     if event.key==pygame.K_SPACE:
#                         game_loop()
#           pygame.display.update()
#           clock.tick(60)



# # while loop
# def game_loop():
#     exist_game=False
#     game_overs=False
  
#     snake_x=45
#     snake_y=55
#     snake_size=30

#     velocity_x=0
#     velocity_y=0

#     snk_list=[]
#     snk_length=1

#     food_size=10
#     food_x=random.randint(30,window_width-200)
#     food_y=random.randint(30,window_hight-100)

#     score=0

#     fps=30
#     pygame.mixer.music.load('10.mp3')
#     pygame.mixer.music.play()
#     with open("highscore.txt","r") as f:
#         highscore=f.read()
#     while not exist_game:
        
    
#         if game_overs:
             
            
#              Gamewindow.fill(white)
#              text_screen("GameOver!Press Enter to play again",red,150,300)
            
#              for event in pygame.event.get():
#                 if event.type==pygame.QUIT:
#                         exist_game=True
#                 if event.type==pygame.KEYDOWN:
#                     if event.key==pygame.K_RETURN:
#                         with open("highscore.txt","w") as f:
#                             f.write(str(highscore))
                        
#                         game_loop()


#         else:
            
#             for event in pygame.event.get():
#                 # print(event)
#                 if event.type==pygame.QUIT:
#                     exist_game=True
#                 if event.type==pygame.KEYDOWN:
#                     if event.key==pygame.K_RIGHT:
#                         velocity_x=10
#                         velocity_y=0

#                 if event.type==pygame.KEYDOWN:
#                     if event.key==pygame.K_DOWN:
#                         velocity_y=6
#                         velocity_x=-0


#                 if event.type==pygame.KEYDOWN:
#                     if event.key==pygame.K_LEFT:
#                         velocity_x=-6
#                         velocity_y=0

#                 if event.type==pygame.KEYDOWN:
#                     if event.key==pygame.K_UP:
#                         velocity_y=-6
#                         velocity_x=0
            
                        

#             snake_x=snake_x+velocity_x
#             # print("size of",snake_x)
            
                
                    
            
#             snake_y=snake_y+velocity_y
#             if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
#                 score+=10
#                 food_x=random.randint(30,window_width-200)
#                 food_y=random.randint(30,window_hight-100)
#                 snk_length+=5
#                 if score>int(highscore):
#                     highscore=score
                


#             # fill backgoundcolor

#             Gamewindow.fill(white)
#             Gamewindow.blit(bgimg,(0,0))
           
#             text_screen("Score:"+str(score)+"                                             Highscore:"+str(highscore)  ,red,5,5)
#             # pygame.draw.rect(Gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
#             plot_snake(Gamewindow,coral,snk_list,snake_size)
#             head=[]
#             head.append(snake_x)
#             head.append(snake_y)
#             snk_list.append(head)
#             if len(snk_list)>snk_length:
#                 del snk_list[0]
#             if head in snk_list [:-1]:
#                  game_overs=True
#                  pygame.mixer.music.load('1.mp3')
#                  pygame.mixer.music.play()
                 


#             if(snake_x<0 or snake_x>window_width or snake_y<0 or snake_y>window_hight):
#                  pygame.mixer.music.load('1.mp3')
#                  pygame.mixer.music.play()
#                  game_overs=True
#                  pygame.mixer.music.load('1.mp3')
#                  pygame.mixer.music.play()
                 

#             pygame.draw.rect(Gamewindow,white,[food_x,food_y,snake_size,snake_size])
#         pygame.display.update()
#         clock.tick(fps)
#     pygame.quit()
#     quit()
# welcome()
# # game_loop()

import random
import pygame
import sys
from datetime import datetime

pygame.init()
pygame.mixer.init()

# Colors with better palette
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)
CORAL = (255, 127, 80)
GREEN = (50, 205, 50)
DARK_GREEN = (34, 139, 34)
GOLD = (255, 215, 0)
DARK_RED = (139, 0, 0)
LIGHT_BLUE = (173, 216, 230)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

# Window size
window_width = 1000
window_height = 600
Gamewindow = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("🐍 Hungry Snake - Classic Arcade Game")

# Load and scale background
try:
    bgimg = pygame.image.load('snake.jpg')
    bgimg = pygame.transform.scale(bgimg, (window_width, window_height)).convert_alpha()
except:
    # Create gradient background if image not found
    bgimg = pygame.Surface((window_width, window_height))
    for i in range(window_height):
        color_value = 50 + (i * 155 // window_height)
        pygame.draw.line(bgimg, (0, color_value, 0), (0, i), (window_width, i))

# Load sounds with error handling
def load_sound(filename):
    try:
        sound = pygame.mixer.Sound(filename)
        return sound
    except:
        return None

eat_sound = load_sound('eat.wav')
game_over_sound = load_sound('game_over.wav')
try:
    pygame.mixer.music.load('10.mp3')
except:
    pass

# Clock and fonts
clock = pygame.time.Clock()
font_large = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 36)
font_title = pygame.font.Font(None, 96)

def text_screen(text, color, x, y, font=font_medium, center=False):
    screen_text = font.render(text, True, color)
    if center:
        text_rect = screen_text.get_rect(center=(x, y))
        Gamewindow.blit(screen_text, text_rect)
    else:
        Gamewindow.blit(screen_text, [x, y])

def draw_gradient_background():
    """Draw a gradient background for menus"""
    for i in range(window_height):
        color_value = 50 + (i * 155 // window_height)
        pygame.draw.line(Gamewindow, (0, color_value, 0), (0, i), (window_width, i))

def plot_snake(Gamewindow, color, snk_list, snake_size):
    """Draw snake with gradient and rounded corners effect"""
    for i, (x, y) in enumerate(snk_list):
        # Create gradient effect - head is brighter
        if i == len(snk_list) - 1:
            # Snake head with different color
            pygame.draw.rect(Gamewindow, DARK_GREEN, [x, y, snake_size, snake_size])
            pygame.draw.rect(Gamewindow, GREEN, [x + 2, y + 2, snake_size - 4, snake_size - 4])
            # Draw eyes
            pygame.draw.circle(Gamewindow, WHITE, (x + snake_size - 8, y + 8), 4)
            pygame.draw.circle(Gamewindow, WHITE, (x + 8, y + 8), 4)
            pygame.draw.circle(Gamewindow, BLACK, (x + snake_size - 8, y + 8), 2)
            pygame.draw.circle(Gamewindow, BLACK, (x + 8, y + 8), 2)
        else:
            pygame.draw.rect(Gamewindow, color, [x, y, snake_size, snake_size])
            pygame.draw.rect(Gamewindow, DARK_GREEN, [x + 2, y + 2, snake_size - 4, snake_size - 4])

def draw_food(x, y, size, pulse_effect):
    """Animated food with pulse effect"""
    # Pulsing animation
    pulse_size = size + int(pulse_effect * 3)
    pygame.draw.circle(Gamewindow, RED, (x + size//2, y + size//2), pulse_size//2)
    pygame.draw.circle(Gamewindow, ORANGE, (x + size//2, y + size//2), pulse_size//3)
    pygame.draw.circle(Gamewindow, GOLD, (x + size//2, y + size//2), pulse_size//6)

def show_particle_effect(x, y):
    """Create particle effect when eating food"""
    for _ in range(10):
        particle_x = x + random.randint(-15, 15)
        particle_y = y + random.randint(-15, 15)
        pygame.draw.circle(Gamewindow, GOLD, (particle_x, particle_y), 3)

def draw_button(text, x, y, width, height, color, hover_color, action=None):
    """Create interactive button"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    button_rect = pygame.Rect(x, y, width, height)
    
    # Check if mouse is over button
    if button_rect.collidepoint(mouse):
        pygame.draw.rect(Gamewindow, hover_color, button_rect)
        pygame.draw.rect(Gamewindow, WHITE, button_rect, 3)
        if click[0] == 1 and action != None:
            pygame.time.wait(200)
            action()
    else:
        pygame.draw.rect(Gamewindow, color, button_rect)
        pygame.draw.rect(Gamewindow, WHITE, button_rect, 2)
    
    # Draw text on button
    text_screen(text, WHITE, x + width//2, y + height//2, font_small, center=True)
    return button_rect

def show_game_over_screen(score, highscore):
    """Enhanced game over screen with options"""
    draw_gradient_background()
    
    # Title
    text_screen("GAME OVER!", RED, window_width//2, 100, font_title, center=True)
    
    # Score display
    text_screen(f"Your Score: {score}", WHITE, window_width//2, 200, font_large, center=True)
    text_screen(f"High Score: {highscore}", GOLD, window_width//2, 270, font_medium, center=True)
    
    # Buttons
    def restart_game():
        game_loop()
    
    def quit_game():
        pygame.quit()
        sys.exit()
    
    draw_button("PLAY AGAIN", window_width//2 - 150, 350, 130, 50, GREEN, DARK_GREEN, restart_game)
    draw_button("QUIT", window_width//2 + 20, 350, 130, 50, RED, DARK_RED, quit_game)
    
    text_screen("Press ENTER to restart or ESC to quit", GRAY, window_width//2, 450, font_small, center=True)
    
    pygame.display.update()
    
    # Handle keyboard input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_loop()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

def welcome():
    """Enhanced welcome screen with name input and instructions"""
    player_name = ""
    name_entered = False
    active_input = False
    
    # Load high score
    try:
        with open("highscore.txt", "r") as f:
            highscore = f.read()
    except:
        highscore = "0"
    
    while not name_entered:
        draw_gradient_background()
        
        # Game title with animation
        title_y = 100 + abs(pygame.time.get_ticks() % 1000 - 500) / 10
        text_screen("HUNGRY SNAKE", GOLD, window_width//2, int(title_y), font_title, center=True)
        
        # Subtitle
        text_screen("The Classic Arcade Game", WHITE, window_width//2, 180, font_medium, center=True)
        
        # Instructions box
        instruction_box = pygame.Rect(window_width//2 - 300, 350, 600, 150)
        pygame.draw.rect(Gamewindow, BLACK, instruction_box)
        pygame.draw.rect(Gamewindow, WHITE, instruction_box, 2)
        
        text_screen("INSTRUCTIONS:", GOLD, window_width//2, 375, font_small, center=True)
        instructions = [
            "⬆️ ⬇️ ⬅️ ➡️  - Use Arrow Keys to Move",
            "🍎 Eat Food to Grow and Increase Score",
            "⚠️ Avoid Hitting Walls or Yourself"
        ]
        for i, instruction in enumerate(instructions):
            text_screen(instruction, WHITE, window_width//2, 410 + i * 30, font_small, center=True)
        
        # High score display
        text_screen(f"HIGH SCORE: {highscore}", GOLD, window_width//2, 550, font_medium, center=True)
        
        # Start text with pulse animation
        pulse = abs(pygame.time.get_ticks() % 1000 - 500) / 500
        alpha = int(155 + pulse * 100)
        start_color = (GREEN[0], GREEN[1], GREEN[2])
        text_screen("PRESS SPACE BAR TO START", start_color, window_width//2, 280, font_medium, center=True)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    name_entered = True
                    game_loop()
        
        pygame.display.update()
        clock.tick(60)

def game_loop():
    """Main game loop with enhanced features"""
    game_exit = False
    game_over = False
    
    # Snake initial position
    snake_x = window_width // 2
    snake_y = window_height // 2
    snake_size = 25
    
    # Movement
    velocity_x = 0
    velocity_y = 0
    speed = 8
    
    # Snake body
    snk_list = []
    snk_length = 1
    
    # Food
    food_size = 25
    food_x = random.randint(50, window_width - 50)
    food_y = random.randint(50, window_height - 50)
    
    # Score
    score = 0
    
    # Animation variables
    pulse_effect = 0
    pulse_direction = 1
    
    # Load high score
    try:
        with open("highscore.txt", "r") as f:
            highscore = int(f.read())
    except:
        highscore = 0
    
    # Play background music
    try:
        pygame.mixer.music.play(-1)  # Loop indefinitely
    except:
        pass
    
    while not game_exit:
        if game_over:
            if game_over_sound:
                game_over_sound.play()
            show_game_over_screen(score, highscore)
            return
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and velocity_x == 0:
                    velocity_x = speed
                    velocity_y = 0
                elif event.key == pygame.K_LEFT and velocity_x == 0:
                    velocity_x = -speed
                    velocity_y = 0
                elif event.key == pygame.K_DOWN and velocity_y == 0:
                    velocity_y = speed
                    velocity_x = 0
                elif event.key == pygame.K_UP and velocity_y == 0:
                    velocity_y = -speed
                    velocity_x = 0
        
        # Update snake position
        snake_x += velocity_x
        snake_y += velocity_y
        
        # Food collision detection with better accuracy
        if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
            score += 10
            if eat_sound:
                eat_sound.play()
            
            # Show particle effect
            show_particle_effect(food_x, food_y)
            
            # Generate new food position
            food_x = random.randint(50, window_width - 50)
            food_y = random.randint(50, window_height - 50)
            snk_length += 3
            
            # Update high score
            if score > highscore:
                highscore = score
                with open("highscore.txt", "w") as f:
                    f.write(str(highscore))
        
        # Animate food pulse
        pulse_effect += 0.1 * pulse_direction
        if pulse_effect >= 1:
            pulse_effect = 1
            pulse_direction = -1
        elif pulse_effect <= 0:
            pulse_effect = 0
            pulse_direction = 1
        
        # Draw game elements
        Gamewindow.blit(bgimg, (0, 0))
        
        # Draw animated food
        draw_food(food_x, food_y, food_size, pulse_effect)
        
        # Draw snake
        head = [snake_x, snake_y]
        snk_list.append(head)
        
        if len(snk_list) > snk_length:
            del snk_list[0]
        
        # Check collision with self
        if head in snk_list[:-1]:
            game_over = True
            continue
        
        # Check boundary collision
        if (snake_x < 0 or snake_x > window_width - snake_size or 
            snake_y < 0 or snake_y > window_height - snake_size):
            game_over = True
            continue
        
        plot_snake(Gamewindow, CORAL, snk_list, snake_size)
        
        # Draw score and high score with better styling
        score_text = f"SCORE: {score}"
        highscore_text = f"HIGH SCORE: {highscore}"
        
        # Score background
        score_rect = pygame.Rect(10, 10, 180, 45)
        pygame.draw.rect(Gamewindow, BLACK, score_rect)
        pygame.draw.rect(Gamewindow, GOLD, score_rect, 2)
        text_screen(score_text, GOLD, 20, 20, font_small)
        
        # High score background
        highscore_rect = pygame.Rect(window_width - 220, 10, 210, 45)
        pygame.draw.rect(Gamewindow, BLACK, highscore_rect)
        pygame.draw.rect(Gamewindow, GOLD, highscore_rect, 2)
        text_screen(highscore_text, GOLD, window_width - 210, 20, font_small)
        
        # Draw length indicator
        length_text = f"LENGTH: {snk_length}"
        text_screen(length_text, WHITE, 20, 65, font_small)
        
        pygame.display.update()
        clock.tick(30)  # 30 FPS for smoother gameplay

# Start the game
if __name__ == "__main__":
    welcome()