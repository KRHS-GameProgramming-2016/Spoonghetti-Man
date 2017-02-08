import pygame, sys, math
from Meatball import *

class Specialmeatball(Meatball):
    def __init__(self, pos=[0,0], size=None):
        self.image = pygame.image.load("rsc/ball/spicy.png")
        Meatball.__init__(self, pos, size)
        self.points = 2
