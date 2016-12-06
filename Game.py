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
height = 600
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0

level = Level("level1.lvl")

balls = [Ball("spicy.png",
              [random.randint(1, 10), random.randint(1, 10)],
              [random.randint(0, width-100), random.randint(0, height-100)],
              random.randint(20, 100))
        ]

player = Player(5, [width/2,height/2])
walls = level.walls

using = "keyboard"
level = 1

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
    
    if len(balls) == 0:
        level += 1
        for b in range(level):
            balls += [Ball("ball.png",
                  [random.randint(1, 10), random.randint(1, 10)],
                  [random.randint(0, width-100), random.randint(0, height-100)],
                  random.randint(20, 100))
            ]
    
    #for ball in balls:
        #ball.move()
        #ball.bounceScreen(size)
        
    player.move()
    player.bounceScreen(size)
    for wall in walls:
        player.bounceWall(wall)
    
    for hitter in balls:
        for hittie in balls:
            if hitter != hittie:
                hitter.bounceBall(hittie)
        if player.bounceBall(hitter):
            balls.remove(hitter)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60)
    
    
    
    
    
