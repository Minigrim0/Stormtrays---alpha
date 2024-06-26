import pygame
import random
from pygame.locals import *
from constantes import *
from classes import *
import math
import json
import codecs
import glob

pygame.init()
   
#-------------------------------------------------------------------------------------------

class EnnemiIM(object):
    
    def __init__(self, FichierEnnemi):
        
        self.posx       = 0
        self.posy       = 0
        self.TargetX    = random.randrange(1050)
        self.TargetY    = random.randrange(650)
        self.count      = 0
        self.i          = 0
        self.Returned   = False
        self.IsAttacked = False
        self.BlitLife   = False
        self.tab        = []
        self.tab_ret    = []
        self.Tics       = 0
        
        f               = open(FichierEnnemi)
        contenu         = f.read()
        self.propriete  = json.loads(contenu)
        
        self.image2Scale = pygame.image.load(self.propriete["Img"]).convert_alpha()
        self.meurt = pygame.mixer.Sound(self.propriete["DeathSound"])
        self.vie = 20
        self.vie_bas = 20
        self.vitesse = self.propriete["Speed"]
        self.Height = self.propriete["Height"]
        self.image = pygame.transform.scale(self.image2Scale, (self.Height, self.Height))
        self.Vie_Rect_Arriere = pygame.Surface((self.vie*(60/self.vie), 3))
        self.Vie_Rect_Arriere.fill((255, 0, 0))
        
        for filename in glob.glob(self.propriete["ImgFolder"]):
            Img2Scale = pygame.image.load(filename).convert_alpha()
            Img = pygame.transform.scale(Img2Scale, (self.Height, self.Height))
            self.tab.append(Img)
        
        for filename in glob.glob(self.propriete["ImgFolderRet"]):
            ImgR2Scale = pygame.image.load(filename).convert_alpha()
            ImgR = pygame.transform.scale(ImgR2Scale, (self.Height, self.Height))
            self.tab_ret.append(ImgR)
        
    def pose_ennemi(self, fenetre):
        
        self.posx = random.randrange(1050)
        self.posy = random.randrange(650)
        
        self.PosAbsolue = (self.posx, self.posy)
                
    def vit(self, fenetre):

        self.Vie_Rect = pygame.Surface((self.vie*(60/self.vie_bas), 3))
        self.Vie_Rect.fill((0, 255, 0))
        
        if self.IsAttacked:
            self.Tics += 1
            self.BlitLife = True
            
        if self.Tics == 50:
            self.IsAttacked = False
            self.BlitLife   = False
            self.Tics       = 0
        
        self.PosAbsolue = (self.posx, self.posy)
    
        if sqrt(((self.posx - self.TargetX) ** 2) + ((self.posy - self.TargetY) ** 2)) > self.vitesse*10:
    
            delta_y = self.TargetY - self.posy
            delta_x = self.TargetX - self.posx
            
            if delta_x != 0:
                angle = atan(delta_y/delta_x)
            else:
                if delta_y < 0:
                    angle = -pi/2
                else :
                    angle =  pi/2
            
            if delta_x < 0:
                angle = angle+pi
                self.Returned = True
            
            else:
                self.Returned = False
            
            self.posx_Old = self.posx
            self.posy_Old = self.posy
            
            self.posy = self.posy + sin(angle)*self.vitesse
            self.posx = self.posx + cos(angle)*self.vitesse
            
            self.anim()
            
            fenetre.blit(self.image, (self.posx, self.posy))
            
            if self.BlitLife:
                fenetre.blit(self.Vie_Rect_Arriere, self.PosAbsolue)
                fenetre.blit(self.Vie_Rect,         self.PosAbsolue)
            
        else:
            
            self.TargetX = random.randrange(1050)
            self.TargetY = random.randrange(650)
                
    def enleve_vie(self, viemoins, liste_mech, ennemi, niveau, coin, King):
        
        self.vie -= viemoins
        self.IsAttacked = True
        self.Tics = 0
        
        if self.vie <= 0:
            
            liste_mech.remove(ennemi)
            self.meurt.play()
            if King.capacite1 == True:
                FlyingGold = GoldAnim(self.PosAbsolue[0] + self.Height//2, self.PosAbsolue[1] + self.Height//2, self.vie_bas)
                niveau.GoldTab.append(FlyingGold)
                niveau.gold += self.vie_bas
            else:
                FlyingGold = GoldAnim(self.PosAbsolue[0] + 32, self.PosAbsolue[1] + 32, self.vie_bas//2)
                niveau.GoldTab.append(FlyingGold)
                niveau.gold += self.vie_bas//2
            niveau.Nombre_Ennemis_Tue += 1
            return True

    def anim(self):
        self.i += 1
        if self.i == 12:
            self.i = 0
        if self.Returned:
            self.image = self.tab_ret[self.i//2]
        else:
            self.image = self.tab[self.i//2]