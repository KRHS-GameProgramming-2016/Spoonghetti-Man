
import pygame, sys, math
class Wall():
    def __init__(self, pos, tileSize=50):
        self.image = pygame.image.load("rsc/wall/wall.png")
        self.image = pygame.transform.scale(self.image, [tileSize,tileSize])
        self.rect = self.image.get_rect(center = pos)
