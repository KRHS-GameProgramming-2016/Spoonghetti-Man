
import pygame, sys, math

class Ball():
    def __init__(self, image, speed=[5,5], pos=[0,0], size=None):
        self.image = pygame.image.load("rsc/ball/"+image)
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        self.speedx = speed[0]
        self.speedy = speed[0]
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2 -1
        self.didBounceX = False
        self.didBounceY = False

        
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

