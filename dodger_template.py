import sys, pygame, threading, time, os
from random import *
pygame.init()
os.environ['SDL_VIDEODRIVER'] = 'directx'

#start game loop
def game():
    global move, y, wx, current_obs
    while(done == False):
        screen.fill((255, 255, 255))
        #Playermovement
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP):
                    move = -1
                elif event.key == pygame.K_DOWN:
                    move = 1
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            else:
                move = 0
        y += 6 * move
        if y < 0:
            y = 0
        elif y > 950:
            y = 950
        pygame.draw.rect(screen, (252, 177, 3), (x, y, 50, 50), 0)

        #obstacledraw
        pygame.draw.rect(screen, (0, 0, 0), (wx[0], 0, 30, wy[0][0]), 0)
        pygame.draw.rect(screen, (0, 0, 0), (wx[0], wy[0][1], 30, 1000), 0)
        wx[0] -= 3

        pygame.draw.rect(screen, (0, 0, 0), (wx[1], 0, 30, wy[1][0]), 0)
        pygame.draw.rect(screen, (0, 0, 0), (wx[1], wy[1][1], 30, 1000), 0)
        wx[1] -= 3

        pygame.draw.rect(screen, (0, 0, 0), (wx[2], 0, 30, wy[2][0]), 0)
        pygame.draw.rect(screen, (0, 0, 0), (wx[2], wy[2][1], 30, 1000), 0)
        wx[2] -= 3

        text = font.render(str(score), True, (252, 177, 3))
        textRect = text.get_rect()
        textRect.center = ( 25, 25) 
        screen.blit(text, textRect)
    
        pygame.display.update()
        time.sleep(0.005)
        pass
    pygame.draw.rect(screen, (255, 0, 0), (wx[current_obs] + 3, 0, 30, wy[current_obs][0]), 0)
    pygame.draw.rect(screen, (255, 0, 0), (wx[current_obs] + 3, wy[current_obs][1], 30, 1000), 0)
    pygame.display.update()

def reset_walls():#real time wall check and reset
    while (done == False):
        for i in range(3):
            if(wx[i] < -50):
                cache = int(random() * 900)
                wy[i][0] = cache
                wy[i][1] = cache + 100
                wx[i] = 2400
        time.sleep(0.005)
    pass

def collision_test():#test player collisions and score responsible
    global score, done, screen, current_obs
    while (done == False):
        for i in range(3):
            if(wx[i] > 50 and wx[i] < 80):
                if (y > wy[i][0] and y + 50 < wy[i][1]):
                    score += 1
                    time.sleep(1)
                else:
                    current_obs = i
                    done = True
                    pass
                pass
            pass
        time.sleep(0.005)
    pass
        
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Dodger")

font = pygame.font.Font('freesansbold.ttf', 32) 

screen.fill((255, 255, 255))
#player variables
x = 50; y = 475
move = 0

score = 0
current_obs = 0
#initiate walls
cache = int(random() * 900)
wy = [[cache, cache + 100], 0, 0]
wx = [1500, 2300, 3100]

cache = int(random() * 900)
wy[1] = [cache, cache + 100]

cache = int(random() * 900)
wy[2] = [cache, cache + 100]

clock = pygame.time.Clock()
done = False

reseter = threading.Thread(target = reset_walls, daemon = True)
reseter.start()
collider = threading.Thread(target = collision_test, daemon = True)
collider.start()
game()
