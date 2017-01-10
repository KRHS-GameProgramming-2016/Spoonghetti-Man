import pygame, sys, math
from Player  import *
from Wall import *
from Meatball import *
class Level():
    def __init__(self, levelFile, tileSize=50):
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
                    self.walls += [Wall([x*self.tileSize + self.tileSize/15,
                                        y*self.tileSize + self.tileSize/15],
                                       self.tileSize)
                                  ]
                if x == "p":
                    self.player += [Player ("spony.png",
                                        [0,0]  
                                        [x*self.tileSize + self.tileSize/.5,
                                         y*self.tileSize + self.tileSize/.5],
                                        self.tileSize)
                                 ]
                if c == "o":
                    self.meatballs += [Meatball("regular.png",
                                          [0,0],
                                          [x*self.tileSize + self.tileSize/2,
                                           y*self.tileSize + self.tileSize/2],
                                          self.tileSize)
                                  ]
                    print "MEAATBALL!!!!"

        
#Level("level1.lvl")
