import pygame, sys, math, random
from Player import *

class AIPlayer(Player):
    def __init__(self, maxSpeed =5 , pos=[10,10]):
        Player.__init__(self, maxSpeed, pos)
        self.goRandomDirection()
        
        
    def update(self):
        if random.randint(0,75) == 0:
            self.goRandomDirection()
        
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
        
