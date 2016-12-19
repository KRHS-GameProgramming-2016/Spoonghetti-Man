import pygame, sys, math
from Meatball import *

class Player(Ball):
    def __init__(self, maxSpeed =5 , pos=[0,0]):
        Ball.__init__(self, "Spoony.png", [0,0], pos, None)
        self.maxSpeed = maxSpeed     
        self.images = [pygame.image.load("rsc/ball/Spoony.png"),
                       pygame.image.load("rsc/ball/Spoony.png")
                      ]
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.animationTimer = 0
        self.animationTimerMax = .2 * 60 #seconds * 60 fps
        
    def move(self):
        Ball.move(self)
        self.animate()
        
    def animate(self):
        if self.animationTimer < self.animationTimerMax:
            self.animationTimer += 1
        else:
            self.animationTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]
        
    def go(self, direction):
        if direction == "up":
            self.speedy = -self.maxSpeed
        if direction == "down":
            self.speedy = self.maxSpeed
        if direction == "left":
            self.speedx = -self.maxSpeed
        if direction == "right":
            self.speedx = self.maxSpeed 
            
        if direction == "stop up":
            self.speedy = 0
        if direction == "stop down":
            self.speedy = 0
        if direction == "stop left":
            self.speedx = 0
        if direction == "stop right":
            self.speedx = 0
    
    def goMouse(self, pos):
        self.rect.center = pos
               
    def bounceScreen(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0
            self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
            self.didBounceY = True
            
    def bounceBall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.dist(other.rect.center) < self.radius + other.radius:
                    return True
        return False
        
    def bounceWall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.speedx = -self.speedx
                self.speedy = -self.speedy
                self.move()
                self.speedx = 0
                self.didBounceX = True
                self.speedy = 0
                self.didBounceY = True
                    
