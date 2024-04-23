import os
import json
import pygame
from pygame.locals import *

class MapTile(object):
    
    def __init__(self, levelPath):
        
        f               = open(levelPath)
        contenu         = f.read()
        self.propriete  = json.loads(contenu)
        
        self.Font = pygame.font.Font("../Police/Viner Hand ITC.ttf",  30)
        self.Img = pygame.image.load(self.propriete["Image"]).convert_alpha()
        self.BlitProp = self.Font.render("Race : "+self.propriete["Race"]+" - Zones : "+
                                        str(self.propriete["Size"])+" - Zones controlees :"+
                                        str(self.propriete["PartsOwned"])+" ("+str(int((
                                        self.propriete["PartsOwned"]/self.propriete["Size"])*100))+"%)"
                                        , 1, (0, 0, 0))
        self.PosTxtX = (1152-self.BlitProp.get_width())/2
        self.IsBlitting = False
        self.HitBoxes = []
        for Box in self.propriete["HitBoxes"]:
            self.HitBoxes.append(pygame.Rect((Box["PosX"], Box["PosY"]), (Box["SizeX"]*30, Box["SizeY"]*18)))
        
    def BlitSelf(self, screen):
        
        if self.IsBlitting:
            screen.blit(self.BlitProp, (self.PosTxtX, 650))
            screen.blit(self.Img, (0, 0))
        
    def Collide(self, pos):
        
        for HitBox in self.HitBoxes:
            if HitBox.collidepoint(pos):
                self.IsBlitting = True
                return True
        self.IsBlitting = False
        return False