import pygame, sys, math
from Player  import *
from Wall import *
from Meatball import *
from specialmeatball import *

class Level():
    def __init__(self, levelFile, tileSize=40):
        self.walls = []
        self.meatballs = []
        self.tileSize = tileSize
        self.player = None
        self.loadLevel(levelFile)
    
    def unloadLevel(self):
        self.walls = []
      
               
    def loadLevel(self, levelFile):        
        f = open("rsc/levels/"+levelFile, 'r')
        lines = f.readlines()
        f.close()
        
        """
        print lines
        print "________________________"
        
        for line in lines:
            print line
        print "________________________"
        """
        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]
            
        lines = newlines
        
        for line in lines:
            print line
        print "________________________"
        
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c == '#':
                    self.walls += [Wall([x*self.tileSize + self.tileSize/7,
                                        y*self.tileSize + self.tileSize/7],
                                       self.tileSize)
                                  ]
                                  
                if c == "b":
                    self.player2 = Player (5,
                                        [x*self.tileSize + self.tileSize/.5,
                                         y*self.tileSize + self.tileSize/.5])
                if c == "p":
                    self.player = Player (5,  
                                        [x*self.tileSize + self.tileSize/.5,
                                         y*self.tileSize + self.tileSize/.5])
                if c == "o":
                    self.meatballs += [Meatball([x*self.tileSize + self.tileSize/2,
                                           y*self.tileSize + self.tileSize/2],
                                          self.tileSize)
                                ]
                if c == "s":
                    self.meatballs += [Specialmeatball([x*self.tileSize + self.tileSize/2,
                                           y*self.tileSize + self.tileSize/2],
                                          self.tileSize)
                                ]
                    print "MEAATBALL!!!!"

        
#Level("level1.lvl")
