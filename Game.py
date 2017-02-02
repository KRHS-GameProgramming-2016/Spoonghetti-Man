import pygame, sys, math, random
from Meatball import *
from Level import *
from Player import *
from specialmeatball import *
from spicymeatball import *
from Wall import*  
from Timer import*
from Spoonghettimonster import *
pygame.init()

clock = pygame.time.Clock()

width = 1290 
height = 700
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0
bgImage = pygame.image.load("Background/YELLOW.png").convert()
bgRect = bgImage.get_rect() 

level = Level("level1.lvl")                                                                                                                                                                                             
print level

player = level.player
player2 = level.player2
walls = level.walls
meatballs = level.meatballs
timer = Timer([width/2, 50])
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
            if event.key == pygame.K_w:
                player2.go("up")
            if event.key == pygame.K_s:
                player2.go("down")
            if event.key == pygame.K_d:
                player2.go("right")
            if event.key == pygame.K_a:
                player2.go("left")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_LEFT:
                player.go("stop left")
            if event.key == pygame.K_w:
                player2.go("stop up")
            if event.key == pygame.K_s:
                player2.go("stop down")
            if event.key == pygame.K_d:
                player2.go("stop right")
            if event.key == pygame.K_a:
                player2.go("stop left")
            
    
    player.move()
    player2.move()
    print player.speed
    player.bounceScreen(size)
    player2.bounceScreen(size)
    for wall in walls:
        player.bounceWall(wall)
        player2.bounceWall(wall)
        
    timer.update()
     
    for meatball in meatballs:
        if player.bounceMeatball(meatball):
            meatballs.remove(meatball)
        if player2.bounceMeatball(meatball):
            meatballs.remove(meatball)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    for meatball in meatballs:
        screen.blit(meatball.image, meatball.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    screen.blit(player.image, player.rect)
    screen.blit(player2.image, player2.rect)
    screen.blit(timer.image, timer.rect)
    pygame.display.flip()
    clock.tick(60)
    
    
    
    
    
