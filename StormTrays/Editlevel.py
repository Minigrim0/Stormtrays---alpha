import pygame
import pygame._view
from pygame.locals import *
from ConstantEditor import *
from classes import *
import tkinter
from tkinter import filedialog
import os
import time

#init des bibliotheques
pygame.init()
root = tkinter.Tk()
root.withdraw()

fenetre = pygame.display.set_mode((1352, 704))
niveau = Niveau(MapSizeTuple)
    
while Edit:
    
    pygame.display.set_caption(Titre_Fenetre)
    pygame.display.flip()
    niveau.afficheE(fenetre, fond, MapSizeTuple)
    for i in range(1, MapSizeTuple[0]):
        fenetre.blit(lignevert, (i*(1152/MapSizeTuple[0]), 0))
    for i in range(1, MapSizeTuple[1]):
        fenetre.blit(lignehor,  (0, (i*(704/MapSizeTuple[1]))))
    fenetre.blit(rectangle, (largeur_jeu, 0))
    fenetre.blit(efface,     (effacerect.x,      effacerect.y))
    fenetre.blit(sauve,      (sauverect.x,        sauverect.y))
    fenetre.blit(ouvre,      (chargerect.x,      chargerect.y))
    fenetre.blit(MicroFond,  (FondCrect.x,        FondCrect.y))
    fenetre.blit(MapSizeImg, (largeur_jeu+10, hauteur_jeu-120))
    fenetre.blit(MultiplImg, (largeur_jeu+70, hauteur_jeu-120))
    fenetre.blit(MapSizeImg, (largeur_jeu+85, hauteur_jeu-120))
    fenetre.blit(SizeXImg,   (largeur_jeu+20, hauteur_jeu-120))
    fenetre.blit(SizeYImg,   (largeur_jeu+95, hauteur_jeu-120))
    if QGPos:
        fenetre.blit(QGImg, (QGPos))
    
    if choix != "  ":
        fenetre.blit(niveau.imgE[choix, rot], possouris)
    
    for v in rect:
        fenetre.blit(niveau.imgE[v, 0], (rect[v].x, rect[v].y))
        
    for event in pygame.event.get():
        if event.type == QUIT:
            Edit = 0
            
        if event.type == MOUSEBUTTONDOWN:
        
            for v in rect:
                if rect[v].collidepoint(event.pos):
                    choix = v
                    rot = 0
                    
            if PlusX.collidepoint(event.pos):
                MapSizeTuple = MapSizeTuple[0]+1,MapSizeTuple[1]
                SizeXImg = myfont1.render(str(MapSizeTuple[0]), 1, (0, 0, 0))
                niveau.videtab(MapSizeTuple, True)
            if LessX.collidepoint(event.pos):
                MapSizeTuple = MapSizeTuple[0]-1,MapSizeTuple[1]
                SizeXImg = myfont1.render(str(MapSizeTuple[0]), 1, (0, 0, 0))
                niveau.videtab(MapSizeTuple, True)
            if PlusY.collidepoint(event.pos):
                MapSizeTuple = MapSizeTuple[0],MapSizeTuple[1]+1
                SizeYImg = myfont1.render(str(MapSizeTuple[1]), 1, (0, 0, 0))
                niveau.videtab(MapSizeTuple, True)
            if LessY.collidepoint(event.pos):
                MapSizeTuple = MapSizeTuple[0],MapSizeTuple[1]-1
                SizeYImg = myfont1.render(str(MapSizeTuple[1]), 1, (0, 0, 0))
                niveau.videtab(MapSizeTuple, True)
            
            if effacerect.collidepoint(event.pos):
                niveau.videtab(MapSizeTuple, False)
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
                Path, filename = os.path.split(filename)
                filename, ext = os.path.splitext(filename)
                Titre_Fenetre = "Editeur - "+filename
                
            if sauverect.collidepoint(event.pos):
                filename = filedialog.asksaveasfilename(initialdir="../level", defaultextension=".txt")
                if filename:
                    niveau.sauve(filename)
                    niveau.sauveF(filename, fond_Edit, QGPos)
                    i = 0
                    while i < 25:
                        niveau.affiche(fenetre, fond)
                        pygame.display.flip()
                        i += 1
                    i = 0
                    arect = pygame.Rect(0,0, largeur_jeu, hauteur_jeu)
                    sub = fenetre.subsurface(arect)
                    sub2 = sub
                    sub = pygame.transform.scale(sub,(39*5, 22*5))
                    sub2 = pygame.transform.scale(sub,(24, 14))
                    dirname, filename = os.path.split(filename)
                    filename, ext = os.path.splitext(filename)
                    pygame.image.save(sub, os.path.join(dirname,"mininiveau",filename+".png"))
                    pygame.image.save(sub2, os.path.join(dirname,"TileImage",filename+".png"))
                choix = "  "

            if event.button == 1 and choix != "  ":
                for x in range(MapSizeTuple[0]):
                    for y in range(MapSizeTuple[1]):
                        if pygame.Rect((x*(1152/MapSizeTuple[0]), y*(704/MapSizeTuple[1])), (1152/MapSizeTuple[0],
                                        704/MapSizeTuple[1])).collidepoint(event.pos):
                            if choix == "p1":
                                niveau.tableau[x,y] = "  ", 0
                            elif choix == "QG":
                                QGPos = (x*(1152/MapSizeTuple[0]), y*(704/MapSizeTuple[1]))
                            else:
                                niveau.tableau[x,y] = choix, rot
                            
            if event.button == 3 and choix != "  ":
                rot = (rot + 90)%360
                            
        if event.type == MOUSEMOTION:
            possouris = (event.pos[0]-16, event.pos[1]-16)
            if event.buttons[0] == 1 and choix != "  ":
                for x in range(MapSizeTuple[0]):
                    for y in range(MapSizeTuple[1]):
                        if pygame.Rect((x*(1152/MapSizeTuple[0]), y*(704/MapSizeTuple[1])), (1152/MapSizeTuple[0], 
                                        704/MapSizeTuple[1])).collidepoint(event.pos):
                            if choix == "p1":
                                niveau.tableau[x,y] = "  ", 0
                            else:
                                niveau.tableau[x,y] = choix, rot
