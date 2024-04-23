import sys
sys.path.append("../EditLevel")
import pygame
from pygame.locals import *
from constantes import *
import glob
import os
from math import *
import time
import json

def FindAngle(delta_x, delta_y):
    
    if delta_x != 0:
        angle = atan(delta_y/delta_x)
    else:
        if delta_y < 0:
            angle = -pi/2
        else :
            angle =  pi/2
    
    if delta_x < 0:
        angle = angle+pi
        
    return angle

class Levels(object):
    
    def __init__(self, file, img, nivrect):
        
        self.File = file
        self.Img = img
        self.Nivrect = nivrect
        
#---------------------------------------------------------------------------------------------------------------------
        
class GoldAnim(object):
    
    def __init__(self, x, y, n):
        
        self.posx = x
        self.posy = y
        self.nbrs = n
        self.i = 0
        myfont = pygame.font.SysFont("Viner Hand ITC", 15)
        self.NbrsAffiche = myfont.render(str(self.nbrs), 1, (0, 0, 0))
    
    def bouge(self, fenetre, goldImg, goldObj, niveau):
        
        self.i += 1
        self.posy -= 2
        if self.i == 24:
            niveau.GoldTab.remove(goldObj)
        fenetre.blit(goldImg         , (self.posx - 12 + 3*cos(self.i), self.posy - 6))
        fenetre.blit(self.NbrsAffiche, (self.posx + 3*cos(self.i)     , self.posy - 6))
        
#---------------------------------------------------------------------------------------------------------------------

class Niveau(object):
    
    def __init__(self):
    
        self.img = {}
        self.img["c1", 0] = pygame.image.load(chem1).convert_alpha()
        self.img["t2", 0] = pygame.image.load(tour2).convert_alpha()
        self.img["t1", 0] = pygame.image.load(tour1).convert_alpha()
        self.img["x1", 0] = pygame.image.load(croix1).convert_alpha()
        self.img["p1", 0] = pygame.image.load(poubelle).convert_alpha()
        self.img["k1", 0] = pygame.image.load(fort1).convert_alpha()
        self.img["v1", 0] = pygame.image.load(Vide1).convert_alpha()
        for rot in [90, 180, 270]:
            self.img["c1",rot] = pygame.transform.rotate(self.img["c1",0], rot)
            self.img["t2",rot] = pygame.transform.rotate(self.img["t2",0], rot)
            self.img["t1",rot] = pygame.transform.rotate(self.img["t1",0], rot)
            self.img["x1",rot] = pygame.transform.rotate(self.img["x1",0], rot)
            self.img["p1",rot] = pygame.transform.rotate(self.img["p1",0], rot)
            self.img["k1",rot] = pygame.transform.rotate(self.img["k1",0], rot)
            self.img["v1",rot] = pygame.transform.rotate(self.img["v1",0], rot)
        
        self.imgE = {}
        self.imgE["c1", 0] = pygame.image.load(chem1E).convert_alpha()
        self.imgE["t2", 0] = pygame.image.load(tour2E).convert_alpha()
        self.imgE["t1", 0] = pygame.image.load(tour1E).convert_alpha()
        self.imgE["x1", 0] = pygame.image.load(croix1E).convert_alpha()
        self.imgE["p1", 0] = pygame.image.load(poubelleE).convert_alpha()
        self.imgE["k1", 0] = pygame.image.load(fort1E).convert_alpha()
        self.imgE["v1", 0] = pygame.image.load(Vide1E).convert_alpha()
        for rot in [90, 180, 270]:
            self.imgE["c1",rot] = pygame.transform.rotate(self.imgE["c1",0], rot)
            self.imgE["t2",rot] = pygame.transform.rotate(self.imgE["t2",0], rot)
            self.imgE["t1",rot] = pygame.transform.rotate(self.imgE["t1",0], rot)
            self.imgE["x1",rot] = pygame.transform.rotate(self.imgE["x1",0], rot)
            self.imgE["p1",rot] = pygame.transform.rotate(self.imgE["p1",0], rot)
            self.imgE["k1",rot] = pygame.transform.rotate(self.imgE["k1",0], rot)
            self.imgE["v1",rot] = pygame.transform.rotate(self.imgE["v1",0], rot)
        
        self.videtab()
        
        self.gold = 500
        self.Vie_Chateau = 100
        self.Nombre_Ennemis_Tue = 0
        self.capacite1 = False
        
        self.GoldTab = []
        
    def videtab(self):
        self.tableau = {}
        for y in range(11):
            for x in range(18):
                self.tableau[x,y] = "  ",0
                
    def sauve(self, nomfichier):
        f = open (nomfichier, "w")
        for y in range(11):
            for x in range(18):
                img,rot = self.tableau[x,y]
                f.write("%s%d/" % (img, rot/90))
            f.write("\n")
    
    def sauveF(self, nomfichier, Fond):
        f = open (nomfichier+"_Pref.txt", "w")
        f.write(Fond)
        
    def construit(self, nomfichier):
        f = open(nomfichier)
        self.tableau = {}
        for y, l in enumerate(f):
            for x in range(18):
                img = l[x*4:x*4+2]
                rot = l[x*4+2]
                self.tableau[x, y] = img, int(rot)*90

        self.FondFenetre = pygame.Surface((1152, 704))
        
        fondimgf = pygame.transform.scale(self.fondimg, (int(1152), int(704)))
        self.FondFenetre.blit(fondimgf, (0,0))
        for y in range(11):
            for x in range(18):
                lettre,rot = self.tableau[x,y]
                if lettre != "  " and lettre != "k1":
                    img = pygame.transform.scale(self.img[lettre,rot],(int(65), int(65)))
                    self.FondFenetre.blit(img, (int((x*64)), int((y*64))))
                elif lettre == "k1":
                    img = pygame.transform.scale(self.img[lettre,rot],(int(64), int((3*64))))
                    self.FondFenetre.blit(img, (int((x*64)), int((y*64))))
                    self.pos_Chateau = [x, y+1]
                    
            try:
                self.FondFenetre.blit(self.nanim, (self.posx, self.posy))
            except:
                pass
                
    def deffond(self, nomfichier):
        f = open(nomfichier+"_Pref.txt", "r")
        image = f.read()
        self.fondimg = pygame.image.load(image).convert_alpha()
            
    def affiche(self, fenetre, fond):
        fenetre.blit(fond, (0,0))
        for y in range(11):
            for x in range(18):
                lettre,rot = self.tableau[x,y]
                if lettre != "  ":
                    fenetre.blit(self.img[lettre,rot], (x*64,y*64))
                    
    def afficheE(self, fenetre, fond):
        fenetre.blit(fond, (0,0))
        for y in range(11):
            for x in range(18):
                lettre,rot = self.tableau[x,y]
                if lettre != "  ":
                    fenetre.blit(self.imgE[lettre,rot], (x*64,y*64))
                    
    def affichem(self, fenetre):
        
        fenetre.blit(self.FondFenetre, (0, 0))
        
class Screen(object):
    
    def __init__(self, size):
        
        info = pygame.display.Info()
        
        self.Font = pygame.font.SysFont("Viner Hand ITC", 25)
        
        self.nativeSize = size
        
        self.fullSize = (info.current_w, info.current_h)
        self.fullScreen = True
        self.resize(self.fullSize)
        
        self.ScaleButton = pygame.image.load(ScaleImg).convert_alpha()
        self.ScaleRect      = pygame.Rect((2, self.nativeSize[1] - 22), (20, 20))
        
        self.fenetre = pygame.Surface(self.nativeSize)
        
        self.delais = 0.05
        self.T0 = time.clock()
        self.Tdepart = time.clock()
        
        self.CompteurFrame = 0
        self.FPS = 0
        self.ShowFPS = False
        
    def rescale(self):
    
        if self.fullScreen:
        
            self.fullScreen = False
            self.resize((1152, 704))
            
        else:
        
            self.fullScreen = True
            self.resize(self.fullSize)
    
    def resize(self, size):
        
        if self.fullScreen:
        
            self.fenetreAffiche = pygame.display.set_mode(self.fullSize, FULLSCREEN)
            
        else:
            
            self.fenetreAffiche = pygame.display.set_mode(size, RESIZABLE)
            
        taillex  = size[0]/self.nativeSize[0]
        tailley  = size[1]/self.nativeSize[1]
        self.taille = min(taillex, tailley)
        
        self.posAffiche = (size[0] - int(self.taille*self.nativeSize[0]))//2, (size[1] - int(self.taille*self.nativeSize[1]))//2
        
    def flip(self):
        
        self.Intervalle()
        self.fenetre.blit(self.ScaleButton, self.ScaleRect.topleft)
        self.fenetreAffiche.blit(pygame.transform.smoothscale(self.fenetre, (int(self.nativeSize[0]*self.taille), int(self.nativeSize[1]*self.taille))), self.posAffiche)
        pygame.display.flip()
        
    def blit(self, Surface, Pos):
        
        self.fenetre.blit(Surface, Pos)
        
    def GetEvent(self):
        
        for event in pygame.event.get():
            
            if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN:
        
                event.pos = int((event.pos[0] - self.posAffiche[0])/self.taille), int((event.pos[1] - self.posAffiche[1])/self.taille)
                
                if event.pos[0] < 0 or event.pos[1] < 0 or event.pos[0] >= 1152 or event.pos[1] >= 704:
                    
                    continue
                    
            if event.type == QUIT:
                
                exit()
            
            elif event.type == KEYDOWN:
                
                if event.key == K_F2:
            
                    pygame.image.save(self.fenetre, "screen/"+ time.strftime("%Y_%m_%d_%H_%M_%S") +".bmp")
            
                elif event.key == K_F11:
                    
                    self.rescale()
                
                elif event.key == K_F3:
                    
                    self.ShowFPS = not self.ShowFPS
                
                else:
                    
                    yield event
            
            elif event.type == VIDEORESIZE:
                
                self.resize(event.size)
        
            elif event.type == MOUSEBUTTONDOWN and self.ScaleRect.collidepoint(event.pos):   
            
                self.rescale()
                    
            else:
            
                yield event
    
    
    def Intervalle(self):
        
        self.T0 = self.T0 + self.delais
            
        SleepTime = self.T0 - time.clock()
        if SleepTime < 0:
            self.T0 = self.T0 - SleepTime
            SleepTime = 0
        time.sleep(SleepTime)
        
        self.CompteurFrame += 1
        if self.T0 - self.Tdepart >= 1:
            self.FPS = self.CompteurFrame/(self.T0 - self.Tdepart)
            self.CompteurFrame = 0
            self.Tdepart = self.T0
        
        if self.ShowFPS:
        
            self.fenetre.blit(self.Font.render(str(round(self.FPS)), 1, (0, 0, 0)), (0, 0))