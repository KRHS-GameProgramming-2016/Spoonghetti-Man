
import pygame, sys, math
class Wall():
    def __init__(self, pos, tileSize=40):
        self.image = pygame.image.load("rsc/wall/SpoonerF(1).png")
        self.image = pygame.transform.scale(self.image, [tileSize,tileSize])
        self.rect = self.image.get_rect(center = pos)
