# -*- coding: utf-8 -*-
import os
import json
import pygame
from pygame.locals import *

class RaceObj(object):

    def __init__(self, AccesPath, x):
        
        dirname, file = os.path.split(AccesPath)
        file, ext = os.path.splitext(file)
        
        self.police = pygame.font.Font("../Police/Viner Hand ITC.ttf",  25)
        self.Image = pygame.image.load(AccesPath).convert_alpha()
        self.Cursor = pygame.image.load("../Img/HUD/RaceButtons/Properties/Cursor.png").convert_alpha()
        self.HitBox = Rect((600, 51+x*45), (160,  40))
        
        f               = open(dirname+"/Properties/"+file+".json")
        contenu         = f.read()
        self.propriete  = json.loads(contenu)
        self.PosY = x
        self.Name = self.propriete["Name"]
        self.description = self.propriete["Description"]
        self.Appercu = pygame.image.load(dirname+"/Preview/"+file+".png").convert_alpha()
        self.TabImgDescription = []
        self.IsSelected = False
        x = 0
        Row = ""
        for Char in self.description:
            if Char != '|':
                Row += Char
            else:
                self.TabImgDescription.append(self.police.render(Row, 1, (255, 255, 255)))
                Row = ""
                x = 0
            x+=1
        if Row != "":
            self.TabImgDescription.append(self.police.render(Row, 1, (255, 255, 255)))
        
    def GotSelected(self):
        return self.IsSelected

    def GetName(self):
        return self.Name
    
    def SetState(self, TOF):
    
        self.IsSelected = TOF
            
    def GetSelected(self, posevent, TabButtons):
    
        if self.HitBox.collidepoint(posevent):
            for Buttons in TabButtons:
                Buttons.SetState(False)
            self.IsSelected = True
        
    def BlitDescription(self, screen):
        
        x = 0
        screen.blit(self.Image, (595, 51+self.PosY*45))
        if self.IsSelected:
            screen.blit(self.Cursor, (580, 64+self.PosY*45))
            screen.blit(self.Appercu, ( 764,  60))
            for Image in self.TabImgDescription:
                screen.blit(Image, (615, 460+x))
                x += 35