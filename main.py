#!/usr/bin/python3
import pygame
import wave


def up(x,y):
    if y == 180 and (x >=85 and x <= 185):
        return False
    if y == 330 and x>=260 and x <=385:
        return False
    if y == 180 and x>=260 and x <=385:
        return False
    else:
        return True
    
def left(x,y):
    if (x == 410 or x == 210) and y >=80 and y <= 155:
        return False
    if x == 410 and y >=230 and y <= 305:
        return False
    if x == 235 and y > 380:
        return False
    else:
        return True
def down(x,y):
    if y == 205 and (x>=260 and x <=385): 
        return False
    if y == 55 and (x>=285 and x<=385):
        return False
    if y == 55 and x >= 85 and x <= 185:
        return False
    if x == 260 and y == 130:
        return False
    if y == 380 and x >= 135 and x <= 210:
        return False

    else:
        return True
def right(x,y):
    if x == 60 and y >=80 and y <= 155:
        return False
    if y >=80 and y <= 130 and x == 260:
        return False 
    if x == 235 and y == 155:
        return False
    if y >=230 and y <= 305 and x == 235:
        return False
    if x == 110 and y >= 405:
        return False
    else:
        return True
    
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pokémon Poison Sting: Virus Age")
mu = wave.open("output.wav")
freq = mu.getframerate()
pygame.mixer.init(frequency=freq)
pygame.mixer.music.load("output.wav")
pygame.mixer.music.play(-1)
go = True
pallet = pygame.image.load("index.jpeg")
pallet = pygame.transform.scale(pallet, (500,500))
zub = pygame.image.load("zub.png")
zub = pygame.transform.scale(zub, (50, 50))
zubat = pygame.image.load("as.png")
zubat = pygame.transform.scale(zubat, (30,30))

x=335
y=330 
i=260
z=55

while go:
    pygame.time.delay(72)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
    screen.blit(pallet, (0, 0))
    screen.blit(zubat, (x, y))
    screen.blit(zub, (i, z))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        print ('z',i, z)
        z -= 25
    if keys[pygame.K_s]:
        z += 25
        print("z",i, z)
    if keys[pygame.K_q]:
        print("z",i, z)
        i -= 25
    if keys[pygame.K_d]:
        print("z",i, z)
        i += 25


    if keys[pygame.K_LEFT] and x > 50  and left(x,y) == True:
        x -= 25
        print(x, y)
    if keys[pygame.K_RIGHT] and x < 435 and right(x,y) == True:
        x += 25
        print(x, y)
    if keys[pygame.K_UP] and y > 50 and up(x,y) == True:
        y -= 25
        print(x,y)
    if keys[pygame.K_DOWN] and y < 450 and down(x, y) == True:
        y += 25
        print(x,y)
    if x==i and y==z:
        pygame.quit()
    pygame.display.update()
pygame.quit()
