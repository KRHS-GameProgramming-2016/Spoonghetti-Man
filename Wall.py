
import pygame, sys, math
class Wall():
    def __init__(self, pos, tileSize=40):
        self.image = pygame.image.load("background/SpoonerF(1)")
        self.image = pygame.transform.scale(self.image, [tileSize,tileSize])
        self.rect = self.image.get_rect(center = pos)
