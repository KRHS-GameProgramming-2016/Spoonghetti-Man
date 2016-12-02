import pygame, sys, math
from Meatball import *

class PlayerBall(Ball):
    def __init__(self, maxSpeed =0 , pos=[0,0]):
        Ball.__init__(self, "playerball_up_1.png", [0,0], pos, None)
        self.maxSpeed = maxSpeed     
        self.images = [pygame.image.load("rsc/ball/playerball_up_1.png"),
                       pygame.image.load("rsc/ball/playerball_up_2.png")
                      ]
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.animationTimer = 0
        self.animationTimerMax = .2 * 60 #seconds * 60 fps

    #def move(self):
        #player.move(self)
        #self.animate()
        
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
