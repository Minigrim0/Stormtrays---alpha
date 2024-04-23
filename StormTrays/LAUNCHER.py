import os
import sys
import time
import pygame
import pygame._view
from os import *
from pygame.locals import *

pygame.init()

Launcher = True
Game     = False
Editor   = False

os.environ['SDL_VIDEO_CENTERED'] = '1'

fenetre = pygame.display.set_mode((750, 305), NOFRAME)

CreditFont = pygame.font.Font("../Police/Viner Hand ITC.ttf",  13)

BackGroundLauncher = pygame.image.load("../Img/FondMenu/Launcher.png").convert_alpha()
PlayLauncher = pygame.image.load("../Img/Boutons/LauncherPlay.png").convert_alpha()
EditorLauncher = pygame.image.load("../Img/Boutons/LauncherEditor.png").convert_alpha()
QuitLauncher = pygame.image.load("../Img/Boutons/LauncherQuit.png").convert_alpha()
Credits = CreditFont.render("Powered by Pygame", 1, (0, 0, 0))

GameRect   = pygame.Rect((450, 150), (300, 40))
EditorRect = pygame.Rect((475, 200), (300, 40))
QuitRect   = pygame.Rect((500, 250), (300, 40))

Music = pygame.mixer.Sound("../musique/Launcher/Theme1.wav")
Music.play()
MusicArray = pygame.sndarray.array(Music)

StartTime = time.clock()
TotTime = 0

while Launcher:
    TimeElapsed = time.clock()-StartTime
    StartTime = time.clock()
    TotTime += TimeElapsed
    Bars = []
    fenetre.blit(BackGroundLauncher, (  0,   0))
    for x in range(4):
        try:
            Bars.append(pygame.Surface((5, abs(MusicArray[(int(TotTime))-x][0])*5)))
            Bars[x].fill((200, 200, 0))
            fenetre.blit(Bars[x], (2+7*x, 305-abs(MusicArray[(int(TotTime))-x][0]*5)))
        except:
            pass
    fenetre.blit(PlayLauncher      , (450, 150))
    fenetre.blit(EditorLauncher    , (475, 200))
    fenetre.blit(QuitLauncher      , (500, 250))
    fenetre.blit(Credits           , (625, 285))
    pygame.display.flip()
    
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if GameRect.collidepoint(event.pos):
                pygame.display.quit()
                system("Stormtrays.py")
                Launcher = False
            if EditorRect.collidepoint(event.pos):
                pygame.display.quit()
                system  ("Editlevel.py")
                Launcher = False
            if QuitRect.collidepoint(event.pos):
                Launcher = False
