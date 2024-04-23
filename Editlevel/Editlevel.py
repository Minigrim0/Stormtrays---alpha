import pygame
from pygame.locals import *
from constantes import *
from classes import *
import tkinter
from tkinter import filedialog
import os
import time

#init des bibliotheques
pygame.init()
root = tkinter.Tk()
root.withdraw()

fenetre = pygame.display.set_mode((largeur_jeu+100, hauteur_jeu))

rectangle = pygame.Surface((100, hauteur_jeu))
rectangle.fill((189, 83, 64))

lignevert = pygame.Surface((1, hauteur_jeu))
lignevert.fill((0, 0, 0))

lignehor= pygame.Surface((largeur_jeu, 1))
lignehor.fill((0, 0, 0))

rect = {}
rect["c1"] = pygame.Rect((largeur_jeu + 12, 10),  (64  , 64))
rect["t2"] = pygame.Rect((largeur_jeu + 12, 84),  (64  , 64))
rect["t1"] = pygame.Rect((largeur_jeu + 12, 154), (64  , 64))
rect["x1"] = pygame.Rect((largeur_jeu + 12, 228), (64  , 64))
rect["p1"] = pygame.Rect((largeur_jeu + 12, 302), (64  , 64))
rect["k1"] = pygame.Rect((largeur_jeu + 12, 376), (3*64, 64))
rect["v1"] = pygame.Rect((largeur_jeu + 12, 450), (64  , 64))

FondCrect  = pygame.Rect((largeur_jeu +10, hauteur_jeu - 140),    (72, 44))
effacerect = pygame.Rect((largeur_jeu +10, hauteur_jeu -40),      (80, 30))
sauverect  = pygame.Rect((largeur_jeu + 10, hauteur_jeu -90),     (40, 40))
chargerect = pygame.Rect((largeur_jeu +50 + 10, hauteur_jeu -90), (40, 40))

MicroFond = pygame.image.load(Mini_Fond).convert_alpha()
fond      = pygame.image.load(fond     ).convert_alpha()
efface    = pygame.image.load(efface   ).convert_alpha()
sauve     = pygame.image.load(sauve    ).convert_alpha()
ouvre     = pygame.image.load(ouvre    ).convert_alpha()

fenetre.blit(fond, (0, 0))

edit = 1
choix = "  "
rot = 0
niveau = Niveau()

while edit:
    
    pygame.display.flip()
    niveau.afficheE(fenetre, fond)
    for i in range(1, tabx):
        fenetre.blit(lignevert, (i*64, 0))
        fenetre.blit(lignehor, (0, i*64))
    fenetre.blit(rectangle, (largeur_jeu, 0))
    fenetre.blit(efface,    (effacerect.x, effacerect.y))
    fenetre.blit(sauve,     (sauverect.x,   sauverect.y))
    fenetre.blit(ouvre,     (chargerect.x, chargerect.y))
    fenetre.blit(MicroFond, (FondCrect.x,   FondCrect.y))
    
    if choix != "  ":
        fenetre.blit(niveau.imgE[choix, rot], possouris)
    
    for v in rect:
        fenetre.blit(niveau.imgE[v, 0], (rect[v].x, rect[v].y))
        
    for event in pygame.event.get():
        if event.type == QUIT:
            edit = 0
            
        if event.type == MOUSEBUTTONDOWN:
        
            for v in rect:
                if rect[v].collidepoint(event.pos):
                    choix = v
                    rot = 0
            
            if effacerect.collidepoint(event.pos):
                niveau.videtab()
                choix = "  "
                
            if FondCrect.collidepoint(event.pos):
                filename = filedialog.askopenfilename(initialdir="../Img/Fonds", defaultextension=".png")
                if filename:
                    fond_Edit = os.path.relpath(filename)
                    fond = pygame.image.load(fond_Edit).convert_alpha()
                choix = "  "
                
            if chargerect.collidepoint(event.pos):
                filename = filedialog.askopenfilename(initialdir="../level", defaultextension=".txt")
                if filename:
                    niveau.construit(filename)
                choix = "  "
                
            if sauverect.collidepoint(event.pos):
                filename = filedialog.asksaveasfilename(initialdir="../level", defaultextension=".txt")
                if filename:
                    niveau.sauve(filename)
                    niveau.sauveF(filename, fond_Edit)
                    i = 0
                    while i < 25:
                        niveau.affiche(fenetre, fond)
                        pygame.display.flip()
                        i += 1
                    i = 0
                    arect = pygame.Rect(0,0, largeur_jeu, hauteur_jeu)
                    sub = fenetre.subsurface(arect)
                    sub = pygame.transform.scale(sub,(39*5, 22*5))
                    dirname, filename = os.path.split(filename)
                    filename, ext = os.path.splitext(filename)
                    pygame.image.save(sub, os.path.join(dirname,"mininiveau",filename+".png"))
                choix = "  "
                

            if event.button == 1 and choix != "  ":
                for x in range(18):
                    for y in range(11):
                        if pygame.Rect((x*64, y*64), (64, 64)).collidepoint(event.pos):
                            if choix == "p1":
                                niveau.tableau[x,y] = "  ", 0
                            else:
                                niveau.tableau[x,y] = choix, rot
                            
            if event.button == 3 and choix != "  ":
                rot = (rot + 90)%360
                            
        if event.type == MOUSEMOTION:
            possouris = (event.pos[0]-16, event.pos[1]-16)
            if event.buttons[0] == 1 and choix != "  ":
                for x in range(18):
                    for y in range(22):
                        if pygame.Rect((x*64, y*64), (64, 64)).collidepoint(event.pos):
                            if choix == "p1":
                                niveau.tableau[x,y] = "  ", 0
                            else:
                                niveau.tableau[x,y] = choix, rot
