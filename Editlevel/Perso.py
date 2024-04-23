import pygame
from pygame.locals import *
from constantes import *
from math import *

class Perso(object):
    
    def __init__(self):
        
        self.posx         = 0
        self.posy         = 0
        self.i            = 0
        self.targetCoordx = 576
        self.targetCoordy = 352
        self.objectif     = 10
        self.xp           = 0
        self.Level_Roi    = 0
        
        self.Is_Returned = False
        self.target      = None
        
        image_King = pygame.image.load(King_1).convert_alpha()
        self.nanim = pygame.transform.scale(image_King, (int(96), int(96)))
        
    def level_up(self):
        
        lvlUp = False
        
        lvlRoiV = self.Level_Roi
        
        if self.xp >= self.objectif:
            self.xp = 0
            self.Level_Roi += 1
            self.objectif = (self.Level_Roi ** 2)*20
            
        if lvlRoiV < self.Level_Roi:
            lvlUp = True
        
        return lvlUp
            
    def anim(self, tab):
        if self.i == 12:
            self.i = 0
        self.nanim = tab[self.i//2]
        self.Is_Returned = False
        
    def anim_ret(self, tab):
        if self.i == 12:
            self.i = 0
        self.nanim = tab[self.i//2]
        self.Is_Returned = True
        
    def vit(self, tab, tabret, vitesse):
        
        if self.target:
            
            try:
                self.targetCoordx = self.target.PosAbsolue[0]
                self.targetCoordy = self.target.PosAbsolue[1]
            except:
                pass
            
            if sqrt(((self.posx - self.target.PosAbsolue[0]) ** 2) + ((self.posy - self.target.PosAbsolue[1]) ** 2)) > vitesse:
        
                delta_y = self.target.PosAbsolue[1] - self.posy
                delta_x = self.target.PosAbsolue[0] - self.posx
                
                if delta_x != 0:
                    angle = atan(delta_y/delta_x)
                else:
                    if delta_y < 0:
                        angle = -pi/2
                    else :
                        angle =  pi/2
                
                if delta_x < 0:
                    angle = angle+pi
                    self.Is_Returned = True
                
                else:
                    self.Is_Returned = False
                
                self.posx_Old = self.posx
                self.posy_Old = self.posy
                
                self.posy = self.posy + sin(angle)*vitesse
                self.posx = self.posx + cos(angle)*vitesse
                
                self.i += 1
                if self.Is_Returned:
                    self.anim_ret(tabret)
                else:
                    self.anim(tab)
            else:
                return True
        
        else:
            
            if sqrt(((self.posx - self.targetCoordx) ** 2) + ((self.posy - self.targetCoordy) ** 2)) > vitesse:
        
                delta_y = self.targetCoordy - self.posy
                delta_x = self.targetCoordx - self.posx
                
                if delta_x != 0:
                    angle = atan(delta_y/delta_x)
                else:
                    if delta_y < 0:
                        angle = -pi/2
                    else :
                        angle =  pi/2
                
                if delta_x < 0:
                    angle = angle+pi
                    self.Is_Returned = True
                
                else:
                    self.Is_Returned = False
                
                self.posx_Old = self.posx
                self.posy_Old = self.posy
                
                self.posy = self.posy + sin(angle)*vitesse
                self.posx = self.posx + cos(angle)*vitesse
                
                self.i += 1
                if self.Is_Returned:
                    self.anim_ret(tabret)
                else:
                    self.anim(tab)
            
            else:
                
                self.nanim = tab[0]