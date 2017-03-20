import pygame, sys, math, random
from Meatball import *
from Level import *
from LevelIndicator import *
from Player import *
from AIPlayer import *
from specialmeatball import *
from spicymeatball import *
from Wall import*  
from Timer import*
from Spoonghettimonster import *
#from LevelIndicator import *
#from Goal import *
pygame.init()

clock = pygame.time.Clock()

width = 1290 
height = 700
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0

lev = 1

while True:
    level = Level("level"+str(lev)+".lvl")                                                                                                                                                                                             
    print level
    bgImage = pygame.image.load("Background/hdspaghet.jpg").convert()
    bgRect = bgImage.get_rect() 
    player = level.player
    player2 = level.player2
    walls = level.walls
    #goal = level.goal
    meatballs = level.meatballs
    timer = Timer([132, 50])
    score = Score([100, height - 30])
    score2 = Score([width - 100, height - 30])
    #print len(meatballs)
    levelIndicator = LevelIndicator([width-10, 16], lev)
    while len(meatballs)>0:
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
                #if event.key == pygame.K_w:
                    #player2.go("up")
                #if event.key == pygame.K_s:
                    #player2.go("down")
                #if event.key == pygame.K_d:
                    #player2.go("right")
                #if event.key == pygame.K_a:
                    #player2.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_LEFT:
                    player.go("stop left")
                #if event.key == pygame.K_w:
                    #player2.go("stop up")
                #if event.key == pygame.K_s:
                    #player2.go("stop down")
                #if event.key == pygame.K_d:
                    #player2.go("stop right")
                #if event.key == pygame.K_a:
                    #player2.go("stop left")

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
                meatball.kill()
                score.setValue(player.points)
            if player2.bounceMeatball(meatball):
                score2.setValue(player2.points)
                meatball.kill()
                
        for meatball in meatballs:
            if not meatball.living:
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
        screen.blit(score.image, score.rect)
        screen.blit(score2.image, score2.rect)
        screen.blit(levelIndicator.image, levelIndicator.rect)
        pygame.display.flip()
        clock.tick(100)
    level.unloadLevel()
    lev += 1
    scoreScreen = True
    
    gamefont = pygame.font.Font("rsc/Fonts/comic sans/comic.ttf", 51)
    
    
    
    if score > score2:
        bgImage = pygame.image.load ("Background/SPOONERRRR.png")
        gameimage = gamefont.render("Spoonghettiman Wins :( ", True, (100,0,00))
        bgRect = bgImage.get_rect()
    else:
        bgImage = pygame.image.load ("Background/SPOONERRRR.png")
        gameimage = gamefont.render("Spooners Inner Demons Were Defeated!", True, (100,0,00))
        bgRect = bgImage.get_rect()
        
    gamerect = gameimage.get_rect(center = [width/2, height/2])

    while scoreScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    scoreScreen = False
        
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(gameimage, gamerect)
        pygame.display.flip()
        clock.tick(100)
