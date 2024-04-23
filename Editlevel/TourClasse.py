import pygame
from pygame.locals import *
from constantes import *
from math import *
from classes import *
import json

class Tours (object):
    
    def __init__ (self, fichiertour, num, myfont1):
        
        f                    = open(fichiertour)
        contenu              = f.read()
        self.propriete       = json.loads(contenu)
        self.nom             = self.propriete["nom"]
        self.vitesse         = self.propriete["vitesse tir"]
        self.degats          = self.propriete["degats"]
        self.portee          = self.propriete["portee"]
        self.image_menu_load = self.propriete["img"]
        self.prix            = self.propriete["prix"]
        self.image_menu      = pygame.image.load(self.image_menu_load).convert_alpha()
        self.tourrect        = pygame.Rect((18 + (64*num) + (num*10), round((704) - (72))), (64, 64))
        self.prix_affiche    = myfont1.render(str(self.prix), 1, (0, 0, 0))
        
    def affichemenu(self, fenetre, num):
        
        fenetre.blit(self.image_menu,   (18 + (60*num) + (num*10), (704) - (72)))
        fenetre.blit(self.prix_affiche, (18 + (60*num) + (num*10), (704) - (72)))
    
class Tours_IG(object):

    def __init__(self, Type_Tour, num, Tab_Cata, Tab_Cata_Ret):
    
        self.portee = Type_Tour.portee
        self.nom = Type_Tour.nom
        self.vitesse = Type_Tour.vitesse
        self.vitesse_Projectile = 12.5
        self.degats = Type_Tour.degats
        self.prix = Type_Tour.prix
        self.Tab_Image = Tab_Cata
        self.Tab_ImageRet = Tab_Cata_Ret
        self.image = self.Tab_Image[0]
        self.Position_IG = [0, 0]
        self.i = 0
        self.frappe = False
        self.Is_Returned = False
        self.tps = 0
        self.Has_Ennemi2Attack = False
        self.t0 = self.vitesse/6
    
    def bougetoursouris(self, possouris, fenetre):
        
        if possouris[0] <  1152 and possouris[0] >= 0 and possouris[1] <  704 and possouris[1] >= 0:
            fenetre.blit(self.image, (possouris[0]-32, possouris[1]-32))
        
    def placetour(self, position_souris, fenetre, tableau, Liste, toursel, niveau):
        
        self.Position_IG[0] = (position_souris[0])//(64)
        self.Position_IG[1] = (position_souris[1])//(64)
        
        niveau.tableau[self.Position_IG[0], self.Position_IG[1]] = ('v1', 0)
        
        fenetre.blit(self.image, ((self.Position_IG[0]*64) , (self.Position_IG[1]*64)))
        self.Rect = pygame.Rect((self.Position_IG[0]*64, self.Position_IG[1]*64), (64, 64))
        
        self.position_Absolue = [self.Position_IG[0]*64, self.Position_IG[1]*64]
        
    def affiche_jeu(self, fenetre):
        if self.Is_Returned:
            self.image = self.Tab_ImageRet[self.i//(self.vitesse//6)]
            fenetre.blit(self.image, ((self.Position_IG[0]*64) , (self.Position_IG[1]*64) ))
        else:
            self.image = self.Tab_Image[self.i//(self.vitesse//6)]
            fenetre.blit(self.image, ((self.Position_IG[0]*64) , (self.Position_IG[1]*64) ))
        
    def attaque(self, pos_tour, Liste_Mechants, niveau, Coin, Tab_Projectile):
    
        if self.i == self.vitesse - 1:
            self.i = 0
        
        elif self.i > 0:
        
            if self.i == self.t0:
                
                Tab_Projectile.append(self.projectile)
                
            self.i += 1
            
        elif self.i == 0:
            
            for ennemi in Liste_Mechants:
            
                t = self.Time2Impact(ennemi)
                
                if (t-self.t0)*self.vitesse_Projectile <= self.portee*64:
                
                    self.Ennemi2Attack = ennemi
                    self.i = 1
                    self.projectile = Projectile(self.position_Absolue, self.Ennemi2Attack, self.degats, t, self.vitesse_Projectile)
                    
                    if self.projectile.delta_x > 0:
                        self.Is_Returned = True
                    else:
                        self.Is_Returned = False
                        
                    break
    
    def Time2Impact(self, ennemi):
        
        delta_x = (self.position_Absolue[0] - ennemi.PosAbsolue[0])
        delta_y = (self.position_Absolue[1] - ennemi.PosAbsolue[1])
        Dist2 = delta_x**2 + delta_y**2
                
        # Cos Angle Tour|Dir Ennemi
        Cos_Beta = (ennemi.Dir_x * delta_x + ennemi.Dir_y * delta_y)
        
        # Triangle Tour/Ennemi/Impact
        # B^2 = A^2 + C^2 - 2AC cos(Beta)
        # A = Distance Ennemi|Impact = Vitesse Ennemi * temps
        # B = Distance Tour|Impact = Vitesse Projectile * (temps - tempsTir)
        # C = Distance Tour|Ennemi
        # Equation second ° pour T : a * t^2 + b * t + c = 0
        a = (self.vitesse_Projectile**2 - ennemi.vitesse**2)
        b = ((2 * ennemi.vitesse * Cos_Beta)-(2 * self.vitesse_Projectile ** 2 * self.t0))
        c = (self.vitesse_Projectile**2 * self.t0 **2) -Dist2
        
        Ro = b**2 - 4*a*c
        
        t = (-b + sqrt(Ro))/(2*a)
        
        return t
            
class Projectile(object):
    
    def __init__(self, PosTour, ennemi, degats, t, vitesse):
        
        self.vitesse = vitesse

        self.image = pygame.image.load("../Img/Projectile.png").convert_alpha()
        
        NewPosEnnemi_x = ennemi.PosAbsolue[0] + ennemi.vitesse * ennemi.Dir_x * t
        NewPosEnnemi_y = ennemi.PosAbsolue[1] + ennemi.vitesse * ennemi.Dir_y * t
        
        self.delta_x = (NewPosEnnemi_x - PosTour[0])
        self.delta_y = (NewPosEnnemi_y - PosTour[1])
        
        self.Dist = sqrt(self.delta_x**2 + self.delta_y**2)
        
        self.Centre_d_x = (NewPosEnnemi_x + PosTour[0])/2
        self.Centre_d_y = (NewPosEnnemi_y + PosTour[1])/2
        
        self.degats = degats
        
        self.Compteur = -1
        
    def Avance(self, fenetre, ListeEnnemis, niveau, coin, Tab_Projectile):
        
        self.Compteur += 2*self.vitesse/self.Dist
        Has_attacked = False
        
        x0 = self.Centre_d_x + self.Compteur*(self.delta_x/2)
        y0 = self.Centre_d_y + self.Compteur*(self.delta_y/2)
        
        h  = (1 - self.Compteur**2) * 0.5 * self.Dist
        
        x = x0
        y = y0 - h
        
        fenetre.blit(self.image, (x, y))
        
        if self.Compteur >= 1:
            for ennemi in ListeEnnemis:
                if sqrt(((x - ennemi.PosAbsolue[0]) ** 2) + (y - ennemi.PosAbsolue[1]) ** 2) < 64:
                    ennemi.enleve_vie(self.degats, ListeEnnemis, ennemi, niveau, coin)
                    
            Tab_Projectile.remove(self)