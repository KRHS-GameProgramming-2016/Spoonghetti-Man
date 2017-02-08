import pygame, sys, math
from Meatball import *

class Specialmeatball(Meatball):
    def __init__(self, image, speed=[0,0], pos=[0,0], size=None):
        Meatball.__init__(self, image, speed, pos, size)
        self.points = 2
