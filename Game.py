import pygame, sys, math, random
from Meatball import *
from Level import *
from Player import *
from specialmeatball import *
from spicymeatball import *
from spoonghettimonster import *
from Wall import*  
pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 700
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0
bgImage = pygame.image.load("Background/YELLOW.png").convert()
bgRect = bgImage.get_rect() 

level = Level("level1.lvl")
print level

player = Player(7, [width/2,height/2])
walls = level.walls
meatballs = level.meatballs
#print len(meatballs)

lev = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_LEFT:
                player.go("left")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_LEFT:
                player.go("stop left")
    
    player.move()
    print player.speed
    player.bounceScreen(size)
    for wall in walls:
        player.bounceWall(wall)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    for meatball in meatballs:
        screen.blit(meatball.image, meatball.rect)
    screen.blit(player.image, player.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60)
    
    
    
    
    
