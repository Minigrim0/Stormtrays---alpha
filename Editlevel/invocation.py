from constantes import *
from classes import *
from ennemis import *
import pygame
from pygame.locals import *
import math

pygame.init()

class Invocation(object):

    def __init__(self,  niveau, Tab, Tab_Ret, addDegats, King):
        
        self.myfont1 = pygame.font.SysFont("Viner Hand ITC",  25)
        
        self.Img = pygame.image.load(Invocation_1).convert_alpha()
        self.nanim = pygame.transform.scale(self.Img, (int(96), int(96)))
        if King.Level_Roi >= 5:
            self.Duree_Invocation = 20
            self.degats = 5
        if King.Level_Roi >= 6:
            self.Duree_Invocation = 25
            self.degats = 7.5
        if King.Level_Roi >= 7:
            self.Duree_Invocation = 30
            self.degats = 7.5
            niveau.capacite1 = True
        if King.Level_Roi >= 8:
            self.Duree_Invocation = 30
            self.degats = 16.5
            
        self.i = 0
        self.tic = 0
        self.Anim_King_i = 0
        self.Is_Returned = False
        self.posx = King.posx
        self.posy = King.posy
        
        self.InvocationAttak      = pygame.image.load(Invocation_Attak    ).convert_alpha()
        self.InvocationAttak2     = pygame.image.load(Invocation_Attak2   ).convert_alpha()
        
        self.InvocationRetAttak   = pygame.image.load(InvocationRet_Attak ).convert_alpha()
        self.InvocationRetAttak2  = pygame.image.load(InvocationRet_Attak2).convert_alpha()
        
        self.Invocation_Attak      = pygame.transform.scale(self.InvocationAttak,     (int(96), int(96)))
        self.Invocation_Attak2     = pygame.transform.scale(self.InvocationAttak2,    (int(96), int(96)))
        
        self.Invocation_Attak_ret  = pygame.transform.scale(self.InvocationRetAttak,  (int(96), int(96)))
        self.Invocation_Attak2_ret = pygame.transform.scale(self.InvocationRetAttak2, (int(96), int(96)))
        
        self.Tab = Tab
        self.TabRet = Tab_Ret
        
    def vit(self, fenetre, Liste_Mechants, niveau,  coin):
        
        self.tic += 1
        
        TimeLeftPrint = self.myfont1.render(str(self.Duree_Invocation), 1, (0, 0, 0))
        
        if self.tic == 24:
            self.Duree_Invocation -= 1
            self.tic = 0
            
        if Liste_Mechants:
            self.bouge_vers_ennemi(Liste_Mechants[0],  Liste_Mechants, niveau, fenetre, coin)
            
        if self.Duree_Invocation == 0:
            return False
            
        fenetre.blit(self.nanim   , (self.posx, self.posy))
        fenetre.blit(TimeLeftPrint, (self.posx, self.posy))
        
        return True
        
    def bouge_vers_ennemi(self, ennemi,  Liste_Mechants, niveau, fenetre, coin):
        
        if sqrt(((self.posx - ennemi.PosAbsolue[0]) ** 2) + ((self.posy - ennemi.PosAbsolue[1]) ** 2)) > 32 and self.Anim_King_i == 0:
        
            delta_y = ennemi.PosAbsolue[1] - self.posy
            delta_x = ennemi.PosAbsolue[0] - self.posx
            
            angle = FindAngle(delta_x, delta_y)
               
            if delta_x < 0:
                
                self.Is_Returned = True
            
            else:
                self.Is_Returned = False
            
            self.posx_Old = self.posx
            self.posy_Old = self.posy
            
            self.posy = self.posy + math.sin(angle)*10
            self.posx = self.posx + math.cos(angle)*10
            
            self.i += 1
            
            if self.Is_Returned:
                self.anim_ret(self.TabRet)
            else:
                self.anim(self.Tab)
            
            self.Anim_King_i = 0
            
        else:
            
            if not self.Is_Returned:
            
                self.Anim_King_i += 1
                
                if self.Anim_King_i == 1:
                    self.nanim = self.Invocation_Attak
                    fenetre.blit(self.nanim, (self.posx, self.posy))
                    
                elif self.Anim_King_i == 4:
                    self.nanim = self.Invocation_Attak2
                    fenetre.blit(self.nanim, (self.posx, self.posy))
                    
                elif self.Anim_King_i == 8:
                    self.i = 6
                    self.anim(self.Tab)
                    fenetre.blit(self.nanim, (self.posx, self.posy))
                    self.Anim_King_i = 0
                    ennemi.enleve_vie(self.degats, Liste_Mechants, ennemi, niveau, coin)
                    
                self.Is_Returned = False
                    
            else:
            
                self.Anim_King_i += 1
                
                if self.Anim_King_i == 1:
                    self.nanim = self.Invocation_Attak_ret
                    fenetre.blit(self.nanim, (self.posx, self.posy))
                    
                elif self.Anim_King_i == 4:
                    self.nanim = self.Invocation_Attak2_ret
                    fenetre.blit(self.nanim, (self.posx, self.posy))
                    
                elif self.Anim_King_i == 8:
                    self.i = 6
                    self.anim(self.TabRet)
                    fenetre.blit(self.nanim, (self.posx, self.posy))
                    self.Anim_King_i = 0
                    ennemi.enleve_vie(self.degats, Liste_Mechants, ennemi, niveau, coin)
                    
                self.Is_Returned = True
            
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