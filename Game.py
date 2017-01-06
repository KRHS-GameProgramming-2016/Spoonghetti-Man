import pygame, sys, math, random
from Meatball import *
from spawn import *
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


player = Player(7, [width/10,height/4])
walls = level.walls
meatball = level.meatball

using = "keyboard"
lev = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if using == "keyboard":
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
        else:
            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                player.goMouse(event.pos)
    

    
    #for ball in meatball:
        #ball.move()
        #ball.bounceScreen(size)
        
    player.move()
    player.bounceScreen(size)
    for wall in walls:
        player.bounceWall(wall)
    
    for hitter in meatball:
        for hittie in meatball:
            if hitter != hittie:
                hitter.bounceBall(hittie)
        if player.bounceBall(hitter):
            meatball.remove(hitter)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    for ball in meatball:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60)
    
    
    
    
    
