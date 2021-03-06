import pygame, sys, math, random
from Player import *

class AIPlayer(Player):
    def __init__(self, maxSpeed =5 , pos=[10,10]):
        Player.__init__(self, maxSpeed, pos)
        size = [45,45]
        self.images = [pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(11).png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(12).png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(13).png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(14).png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(15).png"), size),
                       #pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(16).png"), size),
                       #pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(15).png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(14).png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(13).png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(12).png"), size),
                       pygame.transform.scale(pygame.image.load("rsc/ball/SpoonerM(11).png"), size),
                      ]
        self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxFrame = len(self.images) - 1
        self.goRandomDirection()
        
        
    def update(self):
        if random.randint(0,75) == 0:
            self.goRandomDirection()
            
    def PlayerCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    self.hit = True
                    #self.speedx = -self.speedx
                    #self.move()
                    #self.speedy = 0
                    #self.didBounceX = True
                    #if not self.didBounceY:
                        #self.speedy = -self.speedy
                        #self.move()
                        #self.speedx = 0
                        #self.didBounceX = True
        
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
                self.goRandomDirection()
        
    def goRandomDirection(self):
        xs = ["left", "right", "stop left", "stop right"]
        ys = ["up", "down", "stop up", "stop down"]
        self.speed = [0, 0]
        while self.speed == [0,0]:
            self.go(xs[random.randint(0,3)])
            self.go(ys[random.randint(0,3)])
            self.speed = [self.speedx, self.speedy]
        
