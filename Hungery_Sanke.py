import random
import pygame
pygame.init()
pygame.mixer.init()
# colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
coral=(255,127,80)
# window size

window_width=1000
window_hight=600
Gamewindow=pygame.display.set_mode((window_width,window_hight))
bgimg=pygame.image.load('snake.jpg')
bgimg=pygame.transform.scale(bgimg,(window_width,window_hight)).convert_alpha()
gameName=pygame.display.set_caption("HungrySnake")
Gamewindow.fill(white)
pygame.display.update()


# creating spefic variable

# clock
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

    
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    Gamewindow.blit(screen_text,[x,y])

def plot_snake(Gamewindow,color,snk_list,snake_size):
     for x,y in  snk_list:
        pygame.draw.rect(Gamewindow,color,[x,y,snake_size,snake_size])

def welcome():
     exist_game=False
     while not exist_game:
          Gamewindow.fill(coral)
          text_screen("Welcome! Press space bar to play game",black,150,300)
         
          for event in pygame.event.get():
       
                if event.type==pygame.QUIT:
                    exist_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        game_loop()
          pygame.display.update()
          clock.tick(60)



# while loop
def game_loop():
    exist_game=False
    game_overs=False
  
    snake_x=45
    snake_y=55
    snake_size=30

    velocity_x=0
    velocity_y=0

    snk_list=[]
    snk_length=1

    food_size=10
    food_x=random.randint(30,window_width-200)
    food_y=random.randint(30,window_hight-100)

    score=0

    fps=30
    pygame.mixer.music.load('10.mp3')
    pygame.mixer.music.play()
    with open("highscore.txt","r") as f:
        highscore=f.read()
    while not exist_game:
        
    
        if game_overs:
             
            
             Gamewindow.fill(white)
             text_screen("GameOver!Press Enter to play again",red,150,300)
            
             for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        exist_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        with open("highscore.txt","w") as f:
                            f.write(str(highscore))
                        
                        game_loop()


        else:
            
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exist_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=10
                        velocity_y=0

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN:
                        velocity_y=6
                        velocity_x=-0


                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        velocity_x=-6
                        velocity_y=0

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        velocity_y=-6
                        velocity_x=0
            
                        

            snake_x=snake_x+velocity_x
            # print("size of",snake_x)
            
                
                    
            
            snake_y=snake_y+velocity_y
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                food_x=random.randint(30,window_width-200)
                food_y=random.randint(30,window_hight-100)
                snk_length+=5
                if score>int(highscore):
                    highscore=score
                


            # fill backgoundcolor

            Gamewindow.fill(white)
            Gamewindow.blit(bgimg,(0,0))
           
            text_screen("Score:"+str(score)+"                                             Highscore:"+str(highscore)  ,red,5,5)
            # pygame.draw.rect(Gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(Gamewindow,coral,snk_list,snake_size)
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list [:-1]:
                 game_overs=True
                 pygame.mixer.music.load('1.mp3')
                 pygame.mixer.music.play()
                 


            if(snake_x<0 or snake_x>window_width or snake_y<0 or snake_y>window_hight):
                 pygame.mixer.music.load('1.mp3')
                 pygame.mixer.music.play()
                 game_overs=True
                 pygame.mixer.music.load('1.mp3')
                 pygame.mixer.music.play()
                 

            pygame.draw.rect(Gamewindow,white,[food_x,food_y,snake_size,snake_size])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
# game_loop()

