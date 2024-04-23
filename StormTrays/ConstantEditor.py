import os
import pygame
import time
from pygame.locals import *

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
fenetre = pygame.display.set_mode((750, 305), NOFRAME)

LoadScreen = pygame.image.load("../Img/FondMenu/LoadingScreen.png").convert_alpha()
fenetre.blit(LoadScreen, (0, 0))
pygame.display.flip()

SizeInit = (18, 11)
largeur_jeu = 64*SizeInit[0]
hauteur_jeu = 64*SizeInit[1]

titre_editeur        = "Editeur - Sans Nom"
IconImg              = "../Img/Icon/Icon.png"

rect = {}
rect["c1"] = pygame.Rect((largeur_jeu +  12,  10), (64  , 64))
rect["t2"] = pygame.Rect((largeur_jeu + 100,  10), (64  , 64))
rect["t1"] = pygame.Rect((largeur_jeu +  12,  84), (64  , 64))
rect["x1"] = pygame.Rect((largeur_jeu + 100,  84), (64  , 64))
rect["p1"] = pygame.Rect((largeur_jeu +  12, 154), (64  , 64))
rect["v1"] = pygame.Rect((largeur_jeu + 100, 154), (64  , 64))
rect["k1"] = pygame.Rect((largeur_jeu +  12, 218), (3*64, 64))
rect["QG"] = pygame.Rect((largeur_jeu +  12, 282), (64  , 64))

FondCrect  = pygame.Rect((largeur_jeu +  10, hauteur_jeu - 100), (72, 44))
effacerect = pygame.Rect((largeur_jeu +  10, hauteur_jeu -  40), (80, 30))
sauverect  = pygame.Rect((largeur_jeu + 100, hauteur_jeu -  40), (40, 40))
chargerect = pygame.Rect((largeur_jeu + 150, hauteur_jeu -  40), (40, 40))

PlusX      = pygame.Rect((largeur_jeu +  62, hauteur_jeu - 120), (9, 15))
PlusY      = pygame.Rect((largeur_jeu + 137, hauteur_jeu - 120), (9, 15))
LessX      = pygame.Rect((largeur_jeu +  10, hauteur_jeu - 120), (9, 15))
LessY      = pygame.Rect((largeur_jeu +  85, hauteur_jeu - 120), (9, 15))

rectangle = pygame.Surface((200, hauteur_jeu))
rectangle.fill((189, 83, 64))

lignevert = pygame.Surface((1, hauteur_jeu))
lignevert.fill((0, 0, 0))

lignehor= pygame.Surface((largeur_jeu, 1))
lignehor.fill((0, 0, 0))

QGImg      = pygame.image.load("../Img/Perso/QuestGiver/QuestGiverF1.png").convert_alpha()
fond       = pygame.image.load("../Img/Fonds/fond1.png").convert_alpha()
efface     = pygame.image.load("../Img/Boutons/efface.png").convert_alpha()
ouvre      = pygame.image.load("../Img/Boutons/ouvrir.png").convert_alpha()
sauve      = pygame.image.load("../Img/Boutons/save.png").convert_alpha()
MicroFond  = pygame.image.load("../Img/HUD/MicroFond.png").convert_alpha()
MapSizeImg = pygame.image.load("../Img/HUD/MapSize.png").convert_alpha()
MultiplImg = pygame.image.load("../Img/HUD/times.png").convert_alpha()

myfont    = pygame.font.SysFont("monospace"     ,  25)
myfontt   = pygame.font.Font("../Police/Viner Hand ITC.ttf", 100)
myfont2   = pygame.font.Font("../Police/Viner Hand ITC.ttf",  20)
myfont3   = pygame.font.Font("../Police/Viner Hand ITC.ttf",  40)
myfont1   = pygame.font.Font("../Police/Viner Hand ITC.ttf",  13)
TowerFont = pygame.font.Font("../Police/Viner Hand ITC.ttf",  35)

Edit = True

Titre_Fenetre = titre_editeur
choix = "  "
QGPos = (0, 0)
rot = 0
MapSizeTuple = (18,11)

SizeXImg = myfont1.render(str(MapSizeTuple[0]), 1, (0, 0, 0))
SizeYImg = myfont1.render(str(MapSizeTuple[1]), 1, (0, 0, 0))

Text = "Arkaniis Entertainment  2015 - 2016 ®"
TextI = ""

for Char in Text:
    TextI += Char
    Textb = myfont3.render(TextI, 1, (255, 255, 255))
    fenetre.blit(Textb, (50, 215))
    pygame.display.flip()
    time.sleep(0.05)
    
time.sleep(0.5)
    
pygame.display.quit()