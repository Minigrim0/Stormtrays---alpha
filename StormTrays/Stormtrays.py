import sys
sys.path.append("../EditLevel")
import glob
import os
import time
import pygame
import math
import random
from pygame.locals import *
from ennemis import *
from invocation import *
from classes import *
from constantes import *
from TourClasse import *
from Perso import *
from math import *

pygame.init()

pygame.mixer.init()

screen = Screen((1152, 704))

Defeat_Song = "../musique/Defeat.wav"

Tableau_Musique = []
for Muse in glob.glob("../musique/Themes/*.wav"):
    Music = Muse
    Tableau_Musique.append(Music)

#------------------------------------------------------------------

#images
joue                       = pygame.image.load(joue                ).convert_alpha()
credits                    = pygame.image.load(credits             ).convert_alpha()
option                     = pygame.image.load(option              ).convert_alpha()
quit                       = pygame.image.load(quit                ).convert_alpha()
retour                     = pygame.image.load(retour              ).convert_alpha()
Fond_Noir_Semi_Transparent = pygame.image.load(sombre              ).convert_alpha()
FondSombre                 = pygame.image.load(sombre__            ).convert_alpha()
boutontour                 = pygame.image.load(boutonmenutour      ).convert_alpha()
menutour                   = pygame.image.load(mt                  ).convert_alpha()
pause                      = pygame.image.load(pause               ).convert_alpha()
accelere                   = pygame.image.load(accelere            ).convert_alpha()
accelerex                  = pygame.image.load(accelerex           ).convert_alpha()
reprise                    = pygame.image.load(reprise             ).convert_alpha()
quitpaus                   = pygame.image.load(quitpaus            ).convert_alpha()
optionpaus                 = pygame.image.load(optionpaus          ).convert_alpha()
Quadrille                  = pygame.image.load(carrea              ).convert_alpha()
FondHautDroite             = pygame.image.load(FondHautDroite      ).convert_alpha()
Plus                       = pygame.image.load(Plus__              ).convert_alpha()
Moins                      = pygame.image.load(Moins__             ).convert_alpha()
Fond_Menu_Opt              = pygame.image.load(Fond_Menu_Opti      ).convert_alpha()
OptionsTxt                 = pygame.image.load(OptionsTxt__        ).convert_alpha()
PauseTxt                   = pygame.image.load(PauseTxt__          ).convert_alpha()
Credits                    = pygame.image.load(Credits             ).convert_alpha()
ConfirmQuit                = pygame.image.load(ConfirmQuit         ).convert_alpha()
Poubelle                   = pygame.image.load(poubelle            ).convert_alpha()
XpBar                      = pygame.image.load(XpBar               ).convert_alpha()
InvocBar                   = pygame.image.load(Invoc               ).convert_alpha()
TpsRestInvoc               = pygame.image.load(TpsRestInvoc__      ).convert_alpha()
TpsRestInvocSombre         = pygame.image.load(TpsRestInvocSombre__).convert_alpha()
InfoLvl5Img                = pygame.image.load(InfoLvl5Img         ).convert_alpha()
Coin                       = pygame.image.load(Coin                ).convert_alpha()

#------------------------------------------------------------------
          
King1          = pygame.image.load(King_1        ).convert_alpha()
King2          = pygame.image.load(King_2        ).convert_alpha()
King3          = pygame.image.load(King_3        ).convert_alpha()
King4          = pygame.image.load(King_4        ).convert_alpha()
King5          = pygame.image.load(King_5        ).convert_alpha()
King6          = pygame.image.load(King_6        ).convert_alpha()
               
KingAttak      = pygame.image.load(King_Attak    ).convert_alpha()
KingAttak2     = pygame.image.load(King_Attak2   ).convert_alpha()
               
KingRet1       = pygame.image.load(King_1Ret     ).convert_alpha()
KingRet2       = pygame.image.load(King_2Ret     ).convert_alpha()
KingRet3       = pygame.image.load(King_3Ret     ).convert_alpha()
KingRet4       = pygame.image.load(King_4Ret     ).convert_alpha()
KingRet5       = pygame.image.load(King_5Ret     ).convert_alpha()
KingRet6       = pygame.image.load(King_6Ret     ).convert_alpha()
               
KingRetAttak   = pygame.image.load(KingRet_Attak ).convert_alpha()
KingRetAttak2  = pygame.image.load(KingRet_Attak2).convert_alpha()

#------------------------------------------------------------------

Invoque_Anim1  = pygame.image.load(invoque_anim_1 ).convert_alpha()
Invoque_Anim2  = pygame.image.load(invoque_anim_2 ).convert_alpha()
Invoque_Anim3  = pygame.image.load(invoque_anim_3 ).convert_alpha()
Invoque_Anim4  = pygame.image.load(invoque_anim_4 ).convert_alpha()
Invoque_Anim5  = pygame.image.load(invoque_anim_5 ).convert_alpha()
Invoque_Anim6  = pygame.image.load(invoque_anim_6 ).convert_alpha()
Invoque_Anim7  = pygame.image.load(invoque_anim_7 ).convert_alpha()
Invoque_Anim8  = pygame.image.load(invoque_anim_8 ).convert_alpha()
Invoque_Anim9  = pygame.image.load(invoque_anim_9 ).convert_alpha()
Invoque_Anim10 = pygame.image.load(invoque_anim_10).convert_alpha()
Invoque_Anim11 = pygame.image.load(invoque_anim_11).convert_alpha()
Invoque_Anim12 = pygame.image.load(invoque_anim_12).convert_alpha()
Invoque_Anim13 = pygame.image.load(invoque_anim_13).convert_alpha()
Invoque_Anim14 = pygame.image.load(invoque_anim_14).convert_alpha()

#------------------------------------------------------------------

Invocation1    = pygame.image.load(Invocation_1   ).convert_alpha()
Invocation2    = pygame.image.load(Invocation_2   ).convert_alpha()
Invocation3    = pygame.image.load(Invocation_3   ).convert_alpha()
Invocation4    = pygame.image.load(Invocation_4   ).convert_alpha()
Invocation5    = pygame.image.load(Invocation_5   ).convert_alpha()
Invocation6    = pygame.image.load(Invocation_6   ).convert_alpha()

InvocationRet1 = pygame.image.load(Invocation_1Ret).convert_alpha()
InvocationRet2 = pygame.image.load(Invocation_2Ret).convert_alpha()
InvocationRet3 = pygame.image.load(Invocation_3Ret).convert_alpha()
InvocationRet4 = pygame.image.load(Invocation_4Ret).convert_alpha()
InvocationRet5 = pygame.image.load(Invocation_5Ret).convert_alpha()
InvocationRet6 = pygame.image.load(Invocation_6Ret).convert_alpha()

#------------------------------------------------------------------
       
Catapulte1      = pygame.image.load(Catapulte_1).convert_alpha()
Catapulte2      = pygame.image.load(Catapulte_2).convert_alpha()
Catapulte3      = pygame.image.load(Catapulte_3).convert_alpha()
Catapulte4      = pygame.image.load(Catapulte_4).convert_alpha()
Catapulte5      = pygame.image.load(Catapulte_5).convert_alpha()
Catapulte6      = pygame.image.load(Catapulte_6).convert_alpha()

#------------------------------------------------------------------

Tab_AnimLvlUp = {}
Tab_AnimLvlUp[0] = pygame.image.load(AnimLvlUp01).convert_alpha()
Tab_AnimLvlUp[1] = pygame.image.load(AnimLvlUp02).convert_alpha()
Tab_AnimLvlUp[2] = pygame.image.load(AnimLvlUp03).convert_alpha()
Tab_AnimLvlUp[3] = pygame.image.load(AnimLvlUp04).convert_alpha()
Tab_AnimLvlUp[4] = pygame.image.load(AnimLvlUp05).convert_alpha()
Tab_AnimLvlUp[5] = pygame.image.load(AnimLvlUp06).convert_alpha()
Tab_AnimLvlUp[6] = pygame.image.load(AnimLvlUp07).convert_alpha()
Tab_AnimLvlUp[7] = pygame.image.load(AnimLvlUp08).convert_alpha()
Tab_AnimLvlUp[8] = pygame.image.load(AnimLvlUp09).convert_alpha()
Tab_AnimLvlUp[9] = pygame.image.load(AnimLvlUp10).convert_alpha()

#------------------------------------------------------------------

Fond_Menu_Principal = pygame.image.load(fondm).convert_alpha()

#------------------------------------------------------------------

King_1          = pygame.transform.scale(King1        , (96, 96))
King_2          = pygame.transform.scale(King2        , (96, 96))
King_3          = pygame.transform.scale(King3        , (96, 96))
King_4          = pygame.transform.scale(King4        , (96, 96))
King_5          = pygame.transform.scale(King5        , (96, 96))
King_6          = pygame.transform.scale(King6        , (96, 96))
                                                                
King_Attak      = pygame.transform.scale(KingAttak    , (96, 96))
King_Attak2     = pygame.transform.scale(KingAttak2   , (96, 96))
                                                                
King_1_ret      = pygame.transform.scale(KingRet1     , (96, 96))
King_2_ret      = pygame.transform.scale(KingRet2     , (96, 96))
King_3_ret      = pygame.transform.scale(KingRet3     , (96, 96))
King_4_ret      = pygame.transform.scale(KingRet4     , (96, 96))
King_5_ret      = pygame.transform.scale(KingRet5     , (96, 96))
King_6_ret      = pygame.transform.scale(KingRet6     , (96, 96))
                                                                
King_Attak_ret  = pygame.transform.scale(KingRetAttak , (96, 96))
King_Attak2_ret = pygame.transform.scale(KingRetAttak2, (96, 96))

#------------------------------------------------------------------

InvoqueAnim1  = pygame.transform.scale(Invoque_Anim1 , (96, 96))
InvoqueAnim2  = pygame.transform.scale(Invoque_Anim2 , (96, 96))
InvoqueAnim3  = pygame.transform.scale(Invoque_Anim3 , (96, 96))
InvoqueAnim4  = pygame.transform.scale(Invoque_Anim4 , (96, 96))
InvoqueAnim5  = pygame.transform.scale(Invoque_Anim5 , (96, 96))
InvoqueAnim6  = pygame.transform.scale(Invoque_Anim6 , (96, 96))
InvoqueAnim7  = pygame.transform.scale(Invoque_Anim7 , (96, 96))
InvoqueAnim8  = pygame.transform.scale(Invoque_Anim8 , (96, 96))
InvoqueAnim9  = pygame.transform.scale(Invoque_Anim9 , (96, 96))
InvoqueAnim10 = pygame.transform.scale(Invoque_Anim10, (96, 96))
InvoqueAnim11 = pygame.transform.scale(Invoque_Anim11, (96, 96))
InvoqueAnim12 = pygame.transform.scale(Invoque_Anim12, (96, 96))
InvoqueAnim13 = pygame.transform.scale(Invoque_Anim13, (96, 96))
InvoqueAnim14 = pygame.transform.scale(Invoque_Anim14, (96, 96))

#------------------------------------------------------------------

Invocation_1     = pygame.transform.scale(Invocation1   , (96, 96))
Invocation_2     = pygame.transform.scale(Invocation2   , (96, 96))
Invocation_3     = pygame.transform.scale(Invocation3   , (96, 96))
Invocation_4     = pygame.transform.scale(Invocation4   , (96, 96))
Invocation_5     = pygame.transform.scale(Invocation5   , (96, 96))
Invocation_6     = pygame.transform.scale(Invocation6   , (96, 96))
                                                          
Invocation_1_ret = pygame.transform.scale(InvocationRet1, (96, 96))
Invocation_2_ret = pygame.transform.scale(InvocationRet2, (96, 96))
Invocation_3_ret = pygame.transform.scale(InvocationRet3, (96, 96))
Invocation_4_ret = pygame.transform.scale(InvocationRet4, (96, 96))
Invocation_5_ret = pygame.transform.scale(InvocationRet5, (96, 96))
Invocation_6_ret = pygame.transform.scale(InvocationRet6, (96, 96))

#------------------------------------------------------------------
        
Catapulte_1 = pygame.transform.scale(Catapulte1, (64, 64))
Catapulte_2 = pygame.transform.scale(Catapulte2, (64, 64))
Catapulte_3 = pygame.transform.scale(Catapulte3, (64, 64))
Catapulte_4 = pygame.transform.scale(Catapulte4, (64, 64))
Catapulte_5 = pygame.transform.scale(Catapulte5, (64, 64))
Catapulte_6 = pygame.transform.scale(Catapulte6, (64, 64))

#------------------------------------------------------------------

Perso_Tab     = [King_1,     King_2,     King_3,     King_4,     King_5,     King_6    ]
Perso_Tab_ret = [King_1_ret, King_2_ret, King_3_ret, King_4_ret, King_5_ret, King_6_ret]

#------------------------------------------------------------------

Invoc_Tab     = [Invocation_1,     Invocation_2,     Invocation_3,     Invocation_4,     Invocation_5,     Invocation_6    ]
Invoc_Tab_ret = [pygame.transform.flip(c, True, False) for c in Invoc_Tab]

#------------------------------------------------------------------

Catapulte_Tab = [Catapulte_1, Catapulte_2, Catapulte_3, Catapulte_4, Catapulte_5, Catapulte_6]
Catapulte_Tab_Ret = [pygame.transform.flip(c, True, False) for c in Catapulte_Tab]

#------------------------------------------------------------------

#Rectangles
jouerect       = pygame.Rect((1152    - 500, 704    - 240), (500,  50))
credirect      = pygame.Rect((1152    - 450, 704    - 180), (500,  50))
optionrect     = pygame.Rect((1152    - 400, 704    - 120), (500,  50))
quitrect       = pygame.Rect((1152    - 350, 704    -  60), (500,  50))
retourrect     = pygame.Rect((1152    - 500,            0), (500,  50))
pauserect      = pygame.Rect((1152    - 332,            5), ( 40,  40))
accelererect   = pygame.Rect((1152    - 382,            5), ( 40,  40))
boutontourrect = pygame.Rect((32           , 704    -  50), ( 45,  45))
mtrect         = pygame.Rect((975          , 704    -  89), ( 15,  15))
reprendrect    = pygame.Rect((1152//2 - 100, 704//2 -  85), (120,  50))
optionprect    = pygame.Rect((1152//2 - 100, 704//2 -  25), (120,  50))
quitjrect      = pygame.Rect((1152//2 - 100, 704//2 +  35), (120,  50))
quitOrect      = pygame.Rect((1152//2 - 100, 704//2 +  55), (120,  50))
VolMoins       = pygame.Rect((          655,          302), ( 40,  40))
VolPlus        = pygame.Rect((          705,          302), ( 40,  40))
DifMoins       = pygame.Rect((          655,          347), ( 40,  40))
DifPlus        = pygame.Rect((          705,          347), ( 40,  40))
ConfirmReprise = pygame.Rect((1152//2 -  60, 704//2 -  55), (120,  50))
ConfirmQuitter = pygame.Rect((1152//2 -  60, 704//2 +  15), (120,  50))
PoubelleRect   = pygame.Rect((           15,           15), ( 40,  40))
InfoLvl5Rect   = pygame.Rect((            0,            0), (750, 113))

#rectangles niveaux
Tableau_Niveau = []

#definition des miniatures
Compteur = 10
for filename in glob.glob("../level/mininiveau/*.png"):
    dirname, file = os.path.split(filename)
    file, ext = os.path.splitext(file)
    try:
        img = pygame.image.load(filename).convert_alpha()
    except:
        img = pygame.image.load(Vide1E).convert_alpha()
    nivrect = pygame.Rect((1152/2 - 10, Compteur), (500, 110))
    level = Levels(file, img, nivrect)
    Tableau_Niveau.append(level)
    Compteur += 120

myfont  = pygame.font.SysFont("monospace"     ,  25)
myfontt = pygame.font.SysFont("Viner Hand ITC", 100)
myfont2 = pygame.font.SysFont("Viner Hand ITC",  20)
myfont3 = pygame.font.SysFont("Viner Hand ITC",  40)
myfont1 = pygame.font.SysFont("Viner Hand ITC",  10)

#Tableau Liste_Tours
num = 0  
Liste_Tours = []
for filename in glob.glob("../Tours/*.json"):
    Liste_Tours.append(Tours(filename, num, myfont1))
    num += 1
    
#Variables de "session"
niveau          = Niveau()
King            = Perso()
invocation      = None
Programme_Actif = True
Menu_Principal  = True
Menu_Selection  = False
Menu_Options    = False
Credits_Anim    = False
Confirm_Quit    = False
jeu             = False
menu_tour       = False
pausemenu       = False
OptionsMenu     = False
Ecran_Perdu     = False
anim_Perdu      = False
animjouer       = False
animmenu        = False
Anim_King       = False
Anim_King_Ret   = False
AfficheLvlUp    = False
animInvocation  = False

invoque_Boucle  = True
deplace         = False
lvl             = False
affiche_nomTour = False

tps             = 0
TpsInvoc        = 0
TpsLvl          = 0
lvl_Num         = 1
Anim_King_i     = 0
message_argent  = myfont2.render("", 1, (255, 0, 0))
position_souris = (0, 0)

pygame.key.set_repeat(100, 10)

Volume = 5
Difficulte = 5

pygame.mixer.music.set_volume(Volume/10)

fondtps = 0
randomVarTF = True

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Tant que le programme tourne
while Programme_Actif:
    
    i = 0
    
    #Menu_Principal
    while Menu_Principal:
        
        
        
        #Affiche les éléments du menu
        screen.blit(Fond_Menu_Principal, (   0,   0))
        screen.blit(joue               , ( 652, 464))
        screen.blit(credits            , ( 702, 524))
        screen.blit(option             , ( 752, 584))
        screen.blit(quit               , ( 802, 644))
        screen.flip()
            
        #Musique
        if not pygame.mixer.music.get_busy():
            
            #iMusic = random.randrange(len(Tableau_Musique))
            pygame.mixer.music.load(Tableau_Musique[random.randrange(len(Tableau_Musique))])
            pygame.mixer.music.play()
        
        #events
        for event in screen.GetEvent():
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Menu_Principal = False
                    Confirm_Quit = True
                    break
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                
                if quitrect.collidepoint(event.pos):
                    Menu_Principal = False
                    Confirm_Quit   = True
                    break
                    
                if jouerect.collidepoint(event.pos):
                    Menu_Principal = False
                    animjouer = True
                    break
                
                if optionrect.collidepoint(event.pos):
                    Menu_Principal = False
                    Menu_Options = True
                    break
                
                if credirect.collidepoint(event.pos):
                    Menu_Principal = False
                    Credits_Anim = True
                    break

#--------------------------------------------------------------------------------------------------------------------------------------------
    
    
    
    while Confirm_Quit:
        
        
        
        screen.blit(Fond_Menu_Principal, (  0,   0))
        screen.blit(ConfirmQuit        , (376, 152))
        screen.blit(reprise            , (516, 297))
        screen.blit(quitpaus           , (516, 367))
        screen.flip()
        
        #Musique
        if not pygame.mixer.music.get_busy():
            
            pygame.mixer.music.load(Tableau_Musique[random.randrange(len(Tableau_Musique))])
            pygame.mixer.music.play()
        
        for event in screen.GetEvent():
            
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                
                Confirm_Quit = False
                Menu_Principal = True
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                
                if ConfirmReprise.collidepoint(event.pos):
                    
                    Confirm_Quit = False
                    Menu_Principal = True
                
                elif ConfirmQuitter.collidepoint(event.pos):
                    
                    Confirm_Quit = False
                    Programme_Actif = False

#--------------------------------------------------------------------------------------------------------------------------------------------
    
    #Menu_Principal de sélection
    if Menu_Selection:
        i = 60
        Compteur_Lvls = 10
        
    while Menu_Selection:
        
        Compteur_Mini = i
        Compteur_Lvls = i
        
        King.posx = 0
        King.posy = 0
        
        #Affiche les éléments du menu
        screen.blit(Fond_Menu_Principal       , (0, 0))
        screen.blit(Fond_Noir_Semi_Transparent, (0, 0))
        
        for level in Tableau_Niveau:
            Nom_Niveau = myfont.render(level.File, 1, (255, 255, 255))
            screen.blit(level.Img       , (586, Compteur_Lvls     ))
            screen.blit(Nom_Niveau,       (796, Compteur_Lvls + 45))
            
            level.Nivrect =  pygame.Rect(  (586, Compteur_Lvls), (500, 110))
            Compteur_Lvls += 120
            
        screen.blit(retour             , ( 654,   0))
        screen.flip()
        
        #Musique
        if not pygame.mixer.music.get_busy():
            
            pygame.mixer.music.load(Tableau_Musique[random.randrange(len(Tableau_Musique))])
            pygame.mixer.music.play()
            
        for event in screen.GetEvent():
            
            if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    Menu_Selection = False
                    Menu_Principal = True
                
            if event.type == MOUSEBUTTONDOWN: 
                
                if event.button == 1:
                    
                    if retourrect.collidepoint(event.pos):
                        animmenu = True
                        Menu_Selection = False
                        break
            
                    for level in Tableau_Niveau:
                        if level.Nivrect.collidepoint(event.pos):
                            jeu = True
                            lvl = level.File
                            Menu_Selection = False
                            break
                
                elif event.button == 5:
                    
                    if i > -len(Tableau_Niveau)*120 + 704:
                        i -= 50
                
                elif event.button == 4:
                    if i < 60:
                        i += 50
                
#--------------------------------------------------------------------------------------------------------------------------------------------
    
    if Menu_Options:
        screen.blit(FondSombre, (0, 0))
        
    while Menu_Options:
        
        #Affiche les éléments du menu
        screen.blit(Fond_Menu_Principal, (0, 0))
        
        #Musique
        if not pygame.mixer.music.get_busy():
            
            i = random.randrange(len(Tableau_Musique))
            pygame.mixer.music.load(Tableau_Musique[i])
            pygame.mixer.music.play()
        
        pygame.mixer.music.set_volume(Volume/10)
    
        Volumetxt = myfont3.render("Volume : "+str(int(Volume*10)), 1, (255, 50, 20))
        Diffictxt = myfont3.render("Difficulté : "+str(Difficulte), 1, (255, 50, 20))
        
        screen.blit(Fond_Menu_Opt, ( 386, 142))
        screen.blit(OptionsTxt   , ( 386, 132))
        screen.blit(Volumetxt    , ( 410, 302))
        screen.blit(Diffictxt    , ( 410, 347))
        screen.blit(Moins        , ( 655, 302))
        screen.blit(Plus         , ( 705, 302))
        screen.blit(Moins        , ( 655, 347))
        screen.blit(Plus         , ( 705, 347))
        screen.blit(quitpaus     , ( 516, 407))
        screen.flip()
        
        for event in screen.GetEvent():
            
            
        
            if event.type == MOUSEBUTTONDOWN:
                
                #quitter le niveau en cours
                if quitOrect.collidepoint(event.pos):
                    Menu_Principal = True
                    Menu_Options = False
                    break
                    
                if VolPlus.collidepoint(event.pos):
                    if Volume < 10:
                        Volume += 1
                
                if VolMoins.collidepoint(event.pos):
                    if Volume > 0:
                        Volume -= 1
                
                if DifPlus.collidepoint(event.pos):
                    if Difficulte < 10:
                        Difficulte += 1
                
                if DifMoins.collidepoint(event.pos):
                    if Difficulte > 0:
                        Difficulte -= 1

#--------------------------------------------------------------------------------------------------------------------------------------------
    
    while Credits_Anim:
        
        #Musique
        if not pygame.mixer.music.get_busy():
            
            i = random.randrange(len(Tableau_Musique))
            pygame.mixer.music.load(Tableau_Musique[i])
            pygame.mixer.music.play()
    
        i = 0
        while i <= 2900:
            
            
            screen.flip()
            screen.blit(Fond_Menu_Principal, (0, 0    ))
            screen.blit(Credits            , (0, 0 - i))
            i += 2
            
            for event in screen.GetEvent():
                
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    
                    Credits_Anim = False
                    i = 3000
                    
                if event.type == MOUSEBUTTONDOWN:
                    
                    if event.button == 5:
                        i += 40
                    elif event.button == 4:
                        i -= 40
                
        
        Menu_Principal = True
        Credits_Anim = False
        
#--------------------------------------------------------------------------------------------------------------------------------------------
                    
    #Si jeu est actif (action unique)
    if jeu:
        niveau.deffond("../level/"+str(lvl)+".txt")
        niveau.construit("../level/"+str(lvl)+".txt")
        niveau.affichem(screen)
        
        double_invoque = False
        
        count = 0
        Level_Number = 1
        Liste_Mechants = []
        Liste_Tours_IG = []
        Tab_Projectile = []
        CooldownInvoc = 0
        TpsCoolDown = 0
        
        niveau.gold = 500
        niveau.Vie_Chateau = 100
        niveau.Nombre_Ennemis_Tue = 0
        XpToAdd = 0
        King.xp = 0
        King.objectif = 10
        King.Level_Roi = 0
        Degats_Roi = 3
        Vitesse = 5
        TpsLvl = 0
        Icapacite1 = 0
        HaveSeenLvl5Msg = False
        ImgInvoc = True
        Accelerex2 = False
        invocation = None
        Tps_Invoc_affiche  = None
        AfficheStatTour = False
        
        Compteur_Iteration = 0
        Time_50 = myfont2.render("0", 1, (  0,  0,  0))
        
    while jeu:
        
        if niveau.capacite1:
            Icapacite1 += 1
            if Icapacite1 == 160:
                Icapacite1 = 0
                niveau.capacite1 = False
        
        #Musique
        if not pygame.mixer.music.get_busy():
            
            i = random.randrange(len(Tableau_Musique))
            pygame.mixer.music.load(Tableau_Musique[i])
            pygame.mixer.music.play()
        
        if XpToAdd > 0:
            XpToAdd -= 3
            King.xp += 3
        
        LvlUp = King.level_up()
        if CooldownInvoc > 0:
            CooldownInvoc -= 1
        TpsCoolDown = CooldownInvoc//24
        
        #Augmentation du niveau
        if LvlUp:
            
            AfficheLvlUp = True
            
            Degats_Roi = King.Level_Roi*0.5 + 3
            Vitesse    = King.Level_Roi*0.25 + 5
            
        #Mort Chateau
        if niveau.Vie_Chateau <= 0:
            jeu = False
            Ecran_Perdu = True
        
        frappe = 0
        
        #Construction + Affichage + Boutons
        Argent_Possede_Affiche = myfont2.render("Or : "     +str(niveau.gold)               , 1, (  0,   0,   0))
        Vie_Chateau_Affiche    = myfont2.render("Bastion : "+str(niveau.Vie_Chateau) + "pv.", 1, (  0,   0,   0))
        Level_Num_Affiche      = myfont2.render("Niveau "   +str(King.Level_Roi)          , 1, (  0,   0,   0))
        Ennemi_Tue_Affiche     = myfont2.render("Victimes : "+str(niveau.Nombre_Ennemis_Tue), 1, (  0,   0,   0))
        Degats_Roi_Affiche     = myfont2.render("Dégats : " +str(Degats_Roi)                , 1, (  0,   0,   0))
        Vitesse_Roi_Affiche    = myfont2.render("Vitesse : "+str(Vitesse)                   , 1, (  0,   0,   0))
        Obj_Lvl_Txt            = myfont2.render(str(King.xp) + "/" + str(King.objectif) , 1, (  0,   0,   0))
        if TpsCoolDown != 0:
            Tps_Invoc_affiche  = myfont2.render(str(TpsCoolDown), 1, (255, 255, 255))
        else:
            Tps_Invoc_affiche  = None
        
        Current_Xp = pygame.Surface(((King.xp/King.objectif)*255, 18))
        Current_Xp.fill((20, 255, 20))
        
        niveau.affichem(screen)
        DoAttak = King.vit(Perso_Tab, Perso_Tab_ret, Vitesse)
        
        if DoAttak:
            if King.Is_Returned and not Anim_King and not Anim_King_Ret:
                Anim_King_Ret = True
            elif not King.Is_Returned and not Anim_King and not Anim_King_Ret:
                Anim_King = True
        
        #Bouger les ennemis
        for ennemi in Liste_Mechants:
        
            ennemi.bouge(niveau.tableau, screen, niveau, Liste_Mechants, Coin)
            ennemi.meurt.set_volume(Volume/10)
        
        for projectileObj in Tab_Projectile:
            projectileObj.Avance(screen, Liste_Mechants, niveau, Coin, Tab_Projectile)
        
        #Faire attaquer les tours
        for tour in Liste_Tours_IG:
        
            tour.attaque(tour.Position_IG, Liste_Mechants, niveau, Coin, Tab_Projectile)
            tour.affiche_jeu(screen)
            
        if invocation:
            if not invocation.vit(screen, Liste_Mechants, niveau, Coin):
                invocation = None
                
        if Anim_King:
            Anim_King_i += 1
            
            if Anim_King_i == 1:
                King.nanim = King_Attak
                
            elif Anim_King_i == 4:
                King.nanim = King_Attak2
                try:
                    if King.target.enleve_vie(Degats_Roi, Liste_Mechants, King.target, niveau, Coin):
                        XpToAdd += King.target.vie_bas*0.33
                except:
                    King.target = None
                
            elif Anim_King_i == 8:
                King.i = 6
                King.anim(Perso_Tab)
                Anim_King_i = 0
                Anim_King = False
        
        if Anim_King_Ret:
            Anim_King_i += 1
            
            if Anim_King_i == 1:
                King.nanim = King_Attak_ret
                
            elif Anim_King_i == 4:
                King.nanim = King_Attak2_ret
                try:
                    if King.target.enleve_vie(Degats_Roi, Liste_Mechants, King.target, niveau, Coin):
                        XpToAdd += King.target.vie_bas*0.33
                except:
                    King.target = None
                
            elif Anim_King_i == 8:
                King.i = 6
                King.anim_ret(Perso_Tab_ret)
                Anim_King_i = 0
                King.Is_Returned = True
                Anim_King_Ret = False
        
        if Difficulte == 10:
            Difficulty = 0.05
        if Difficulte == 9:
            Difficulty = 0.10
        if Difficulte == 8:
            Difficulty = 0.12
        if Difficulte == 7:
            Difficulty = 0.25
        if Difficulte == 6:
            Difficulty = 0.5
        if Difficulte == 5:
            Difficulty = 0.75
        if Difficulte == 4:
            Difficulty = 1
        if Difficulte == 3:
            Difficulty = 1.25
        if Difficulte == 2:
            Difficulty = 1.5
        if Difficulte == 1:
            Difficulty = 1.75
        if Difficulte == 0:
            Difficulty = 2
        
        if niveau.Nombre_Ennemis_Tue >= 0:
            Level_Difficulty = 110*Difficulty
            lvl_Num = 1
        if niveau.Nombre_Ennemis_Tue >= 10:
            Level_Difficulty = 95*Difficulty
            lvl_Num = 2
        if niveau.Nombre_Ennemis_Tue >= 25:
            Level_Difficulty = 60*Difficulty
            lvl_Num = 3
        if niveau.Nombre_Ennemis_Tue >= 50:
            Level_Difficulty = 50*Difficulty
            lvl_Num = 4
        if niveau.Nombre_Ennemis_Tue >= 100:
            Level_Difficulty = 35*Difficulty
            lvl_Num = 5
        if niveau.Nombre_Ennemis_Tue >= 200:
            Level_Difficulty = 20*Difficulty
            lvl_Num = 6
        if niveau.Nombre_Ennemis_Tue >= 400:
            Level_Difficulty = 16*Difficulty
            lvl_Num = 7
        if niveau.Nombre_Ennemis_Tue >= 750:
            Level_Difficulty = 12*Difficulty
            lvl_Num = 8
        if niveau.Nombre_Ennemis_Tue >= 1000:
            Level_Difficulty = 8*Difficulty
            lvl_Num = 9
        if niveau.Nombre_Ennemis_Tue >= 2500:
            Level_Difficulty = 4*Difficulty
            lvl_Num = 10
        if niveau.Nombre_Ennemis_Tue >= 5000:
            Level_Difficulty = 2*Difficulty
            lvl_Num = 10
            double_invoque = True
            
        Aleatoire = random.random()*Level_Difficulty
            
        #Test random en fonction de Level_Difficulty pour invoquer un ennemi
        if Aleatoire <= 1:
            while invoque_Boucle:
                invoque = random.randrange(10)
                if invoque == 0:
                    ennemi = Ennemi_IG("../Ennemis/Orc.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 1 or invoque == 2:
                    ennemi = Ennemi_IG("../Ennemis/Goblin.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 3:
                    ennemi = Ennemi_IG("../Ennemis/Dwarf.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 4:
                    ennemi = Ennemi_IG("../Ennemis/Knight.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 5:
                    ennemi = Ennemi_IG("../Ennemis/Ghost.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 6:
                    ennemi = Ennemi_IG("../Ennemis/Golem.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 7:
                    invoque = random.randrange(5)
                    if invoque == 0:
                        ennemi = Ennemi_IG("../Ennemis/Dragon.json")
                        ennemi.pose_ennemi(niveau.tableau, screen)
                        Liste_Mechants.append(ennemi)
                elif invoque == 8 or invoque == 9 or invoque == 10:
                    ennemi = Ennemi_IG("../Ennemis/Wolf.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                if double_invoque == True:  
                    double_invoque = False
                    pass
                else:
                    invoque_Boucle = False
                    
            invoque_Boucle = True
            
            
    
        #Si le Menu des tours est actif
        if menu_tour:
        
            num = 0
            screen.blit(Quadrille, (0, 0))
            if not deplace:
            
                screen.blit(menutour, (0, 604))
        
            if deplace:
                
                screen.blit(Poubelle, (15, 15))
                tourSelectionee.bougetoursouris(position_souris, screen)
            
            else:
                for tour in Liste_Tours:
                
                    tour.affichemenu(screen, num)
                    num += 1
                
                    #affiche le nom de la tour
                    if tour.tourrect.collidepoint(position_souris):
                        
                        message = myfont2.render(tour.nom, 1, (0, 0, 0))
                        
                        screen.blit(message, (15,  15))
                        
                        if niveau.gold < tour.prix:
                        
                            message_argent = myfont2.render("Vous n'avez pas assez d'argent !", 1, (255, 0, 0))
                            screen.blit(message_argent, (15,  35))
                            
        screen.blit(King.nanim, (King.posx, King.posy))
        screen.blit(FondHautDroite        , (1152 - 282,  0))
        screen.blit(Argent_Possede_Affiche, (1152 - 280,  5))
        screen.blit(Vie_Chateau_Affiche   , (1152 - 280, 27))
        screen.blit(Vitesse_Roi_Affiche   , (1152 - 280, 54))
        screen.blit(Level_Num_Affiche     , (1152 - 132,  5))
        screen.blit(Ennemi_Tue_Affiche    , (1152 - 132, 27))
        screen.blit(Degats_Roi_Affiche    , (1152 - 132, 54))
        screen.blit(Current_Xp            , (1152 - 270, 86))
        screen.blit(Obj_Lvl_Txt           , (1152 - 155, 80))
        screen.blit(XpBar                 , (1152 - 282, 80))
        screen.blit(pause                 , (       820,  5))
        if Tps_Invoc_affiche and King.Level_Roi >= 5:
            screen.blit(TpsRestInvocSombre, (1152 - 550, 10))
            screen.blit(Tps_Invoc_affiche , (1152 - 535, 25))
        elif King.Level_Roi >= 5:
            screen.blit(TpsRestInvoc      , (1152 - 550, 10))
        
        if AfficheLvlUp:
       
            TpsLvl += 1
            if TpsLvl < 30:
                AnimLvlUpBlit = Tab_AnimLvlUp[TpsLvl//3]
            
            elif TpsLvl < 50:
                AnimLvlUpBlit = Tab_AnimLvlUp[9]
            
            else:
                TpsLvl = 0
                AfficheLvlUp = False
                
            screen.blit(AnimLvlUpBlit  , (426, 277))
        
        if AfficheStatTour:
            
            pygame.draw.circle(screen.fenetre, pygame.Color("red"), (SelectedTower4AfficheStat.Position_IG[0]*64 + 32, SelectedTower4AfficheStat.Position_IG[1]*64 + 32), SelectedTower4AfficheStat.portee*64 + 20, 3)
        
        if animInvocation:
            TpsInvoc += 1
            
            if TpsInvoc%8 == 0:
                ImgInvoc = not ImgInvoc
                
            if ImgInvoc == True and TpsInvoc < 92:
                King.nanim = InvoqueAnim1
            else:
                King.nanim = InvoqueAnim2
            if TpsInvoc >= 96:
                King.nanim = InvoqueAnim3
            if TpsInvoc >= 98:
                King.nanim = InvoqueAnim4
            if TpsInvoc >= 100:
                King.nanim = InvoqueAnim5
            if TpsInvoc >= 102:
                King.nanim = InvoqueAnim6
            if TpsInvoc >= 104:
                King.nanim = InvoqueAnim7
            if TpsInvoc >= 106:
                King.nanim = InvoqueAnim8
            if TpsInvoc >= 108:
                King.nanim = InvoqueAnim9
            if TpsInvoc >= 110:
                King.nanim = InvoqueAnim10
            if TpsInvoc >= 112:
                King.nanim = InvoqueAnim11
            if TpsInvoc >= 114:
                King.nanim = InvoqueAnim12
            if TpsInvoc >= 116:
                King.nanim = InvoqueAnim13
            if TpsInvoc >= 118:
                King.nanim = InvoqueAnim14
            
            if TpsInvoc == 120:
                invocation = Invocation(niveau, Invoc_Tab, Invoc_Tab_ret, King.Level_Roi-5, King)
                TpsInvoc = 0
                King.nanim = King_1
                animInvocation = False
            
            else:
                Invoc_Avancee = pygame.Surface(((TpsInvoc/120)*177, 12))
                Invoc_Avancee.fill((215, 75, 0))
                screen.blit(Invoc_Avancee, (16, 69))
                screen.blit(InvocBar     , (10, 65))
                
        if not menu_tour:
            screen.blit(boutontour     , (  32, 654))
        if Accelerex2:
            screen.blit(accelerex      , ( 770,   5))
        else:                                                  
            screen.blit(accelere       , ( 770,   5))
        
        for Gold in niveau.GoldTab:
            Gold.bouge(screen, Coin, Gold, niveau)
        
        if King.Level_Roi == 5:
            if not HaveSeenLvl5Msg:
                screen.blit(InfoLvl5Img, (0, 0))
                
        #Events du jeu
        for event in screen.GetEvent():
            
            #Si l'on est dans le Menu_Principal des tours
            if menu_tour:
        
                if event.type == MOUSEBUTTONDOWN:
                    
                    if deplace and not mtrect.collidepoint(event.pos) and not PoubelleRect.collidepoint(event.pos):
                        
                        if niveau.tableau[(position_souris[0])//(64), (position_souris[1])//(64)] == ('  ', 0):
                            niveau.gold -= tourSelectionee.prix
                            Liste_Tours_IG.append(tourSelectionee)
                            tourSelectionee.placetour(position_souris, screen, niveau.tableau, Liste_Tours_IG, tourSelectionee, niveau)
                            deplace = False
                            menu_tour = False
                            break
                              
                    #Pour quitter le Menu_Principal des tours
                    if mtrect.collidepoint(event.pos):
                        menu_tour = False
                        deplace = False
                    
                    if PoubelleRect.collidepoint(event.pos):
                        
                        deplace = False
                        
                    for tour in Liste_Tours:
                        
                        #Si l'on selectionne une tour
                        if tour.tourrect.collidepoint(event.pos):
                        
                            if niveau.gold >= tour.prix:
                                deplace = True
                                tourSelectionee = Tours_IG(tour, num, Catapulte_Tab, Catapulte_Tab_Ret)
                                message_argent = myfont2.render("", 1, (255, 0, 0))
                            
            #si on est pas dans Menu_Principal tour
            if not menu_tour:
                
                message_argent = myfont2.render("", 1, (255, 0, 0))
                deplace = False
                
                if event.type == KEYDOWN and not animInvocation:
                    
                    k = pygame.key.get_pressed()
                        
                    if k[K_i]:
                        if King.Level_Roi >= 5 and not invocation and CooldownInvoc == 0:
                            animInvocation = True
                            CooldownInvoc = 2640
                        
                if event.type == MOUSEBUTTONDOWN:
                    
                    #Menu_Principal tour actif
                    if boutontourrect.collidepoint(event.pos):
                        menu_tour = True
                    
                    if event.button == 3:
                        
                        if Liste_Mechants:
                        
                            for ennemi in Liste_Mechants:
                        
                                if ennemi.HitBox.collidepoint(event.pos):
                                    King.target = ennemi
                                    break
                                
                                else:
                                    King.target = None
                                    King.targetCoordx = event.pos[0] - 48
                                    King.targetCoordy = event.pos[1] - 48
                                    
                        else:
                            King.target = None
                            King.targetCoordx = event.pos[0] - 48
                            King.targetCoordy = event.pos[1] - 48
                        
            #Si l'on est dans le Menu_Principal de tour ou pas
            if event.type == MOUSEMOTION:
                
                position_souris = event.pos
            
            #Bouton Pause
            if event.type == MOUSEBUTTONDOWN:
                
                AfficheStatTour = False
                
                if King.Level_Roi == 5 and HaveSeenLvl5Msg == False:
                    if InfoLvl5Rect.collidepoint(event.pos):
                        HaveSeenLvl5Msg = True
                
                if pauserect.collidepoint(event.pos):
                    pausemenu = True
                    
                if accelererect.collidepoint(event.pos):
                    Accelerex2 = not Accelerex2
                    if Accelerex2:
                        screen.delais = 0.05/4
                    else:
                        screen.delais = 0.05
                    
                for Tour in Liste_Tours_IG:
                    if Tour.Rect.collidepoint(event.pos):
                        AfficheStatTour = not AfficheStatTour
                        SelectedTower4AfficheStat = Tour
                
            if event.type == KEYDOWN:
                
                #Bouton "ECHAP"
                if event.key == K_ESCAPE:
                    pausemenu = True
                    menu_tour = False
               
        screen.flip()
        
#-----------------------------------------------------------------------------------------------------------
        
        if pausemenu:
            screen.blit(FondSombre, (0, 0))
        
        #tant que Menu_Principal pause est actif
        while pausemenu:
        
            if not pygame.mixer.music.get_busy():
                
                i = random.randrange(len(Tableau_Musique))
                pygame.mixer.music.load(Tableau_Musique[i])
                pygame.mixer.music.play()
                    
            screen.blit(Fond_Menu_Opt, (1152//2 - 190, 704//2 - 210))
            screen.blit(PauseTxt     , (1152//2 - 190, 704//2 - 210))
            screen.blit(reprise      , (1152//2 - 60 , 704//2 -  85))
            screen.blit(optionpaus   , (1152//2 - 60 , 704//2 -  25))
            screen.blit(quitpaus     , (1152//2 - 60 , 704//2 +  35))
            screen.flip()
            
            for event in screen.GetEvent():
                
                if event.type == KEYDOWN:
                    
                    #quitter pausemenu
                    if event.key == K_ESCAPE:
                        pausemenu = False
                        
                if event.type == MOUSEBUTTONDOWN:
                    
                    
                    
                    #continuer le jeu
                    if reprendrect.collidepoint(event.pos):
                        pausemenu = False
                    
                    #Aller vers OptionsMenu
                    elif optionprect.collidepoint(event.pos):
                        pausemenu = False
                        OptionsMenu = True
                    
                    #quitter le niveau en cours
                    elif quitjrect.collidepoint(event.pos):
                        pausemenu = False
                        jeu = False
                        Menu_Selection = True
        
        #Menu_Principal d'Options dans menu pause
        while OptionsMenu:
        
            if not pygame.mixer.music.get_busy():
                
                i = random.randrange(len(Tableau_Musique))
                pygame.mixer.music.load(Tableau_Musique[i])
                pygame.mixer.music.play()
            
            pygame.mixer.music.set_volume(Volume/10)
            
            appuye = False
            
            Volumetxt = myfont3.render("Volume : "+str(int(Volume*10)), 1, (255, 50, 20))
            Diffictxt = myfont3.render("Difficulté : "+str(Difficulte), 1, (255, 50, 20))
            
            screen.blit(Fond_Menu_Opt, ( 386, 142))
            screen.blit(OptionsTxt   , ( 386, 132))
            screen.blit(Volumetxt    , ( 410, 302))
            screen.blit(Diffictxt    , ( 410, 347))
            screen.blit(Moins        , ( 655, 302))
            screen.blit(Plus         , ( 705, 302))
            screen.blit(Moins        , ( 655, 347))
            screen.blit(Plus         , ( 705, 347))
            screen.blit(quitpaus     , ( 516, 407))
            screen.flip()
            
            for event in screen.GetEvent():
                
                if event.type == MOUSEBUTTONDOWN:
                    
                    #quitter le niveau en cours
                    if quitOrect.collidepoint(event.pos):
                        OptionsMenu = False
                        pausemenu = True
                        
                    if VolPlus.collidepoint(event.pos):
                        if Volume < 10:
                            Volume += 1
                    
                    if VolMoins.collidepoint(event.pos):
                        if Volume > 0:
                            Volume -= 1
                    
                    if DifPlus.collidepoint(event.pos):
                        if Difficulte < 10:
                            Difficulte += 1
                    
                    if DifMoins.collidepoint(event.pos):
                        if Difficulte > 0:
                            Difficulte -= 1
                            
#-------------------------------------------------------------------------------------------------------------------------------------------
    
    if Ecran_Perdu:
    
        i = 0
        anim_Perdu = True
        Perdutxt = pygame.image.load(DefeatTxt).convert_alpha()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(Defeat_Song)
        pygame.mixer.music.play()
    
    while anim_Perdu:
            
        i += 5
        niveau.construit("../level/"+lvl+".txt")
        niveau.affichem(screen)
        
        screen.blit(FondSombre, (0            , 0                 ))
        screen.blit(Fond_Menu_Opt             , (1152//2 - 200, 704//2 - 200      ))
        screen.blit(Perdutxt                  , (1152//2 - 190,            i -  20))
        screen.blit(quitpaus                  , (1152//2 - 60 , 704    -   i - 100))
        screen.flip()
        
        for event in screen.GetEvent():
                pass
                
        if i >= 220:
            anim_Perdu = False
        
    while Ecran_Perdu:
    
        screen.blit(Fond_Menu_Opt, (1152//2 - 200, 704//2 - 200))
        screen.blit(Perdutxt     , (1152//2 - 190, 704//2 - 200))
        screen.blit(quitpaus     , (1152//2 - 60 , 704//2 +  35))
        screen.flip()
    
        for event in screen.GetEvent():
            
            if event.type == MOUSEBUTTONDOWN:
                
                
                
                #quitter le niveau en cours
                if quitjrect.collidepoint(event.pos):
                    Ecran_Perdu = False
                    Menu_Selection = True


#-------------------------------------------------------------------------------------------------------------------------------------------
            
    screen.delais = 0.03
            
    #Animation de Menu_Principal à Menu_Selection
    while animjouer:
        
    
        i = 0
        
        while i<464:
            
            screen.flip()
            screen.blit(Fond_Menu_Principal   , (0             , 0            ))
            screen.blit(joue                  , (1152 - 500    , 704 - 240 - i))
            screen.blit(credits               , (1152 - 450 + i, 704 - 180    ))
            screen.blit(option                , (1152 - 400 + i, 704 - 120    ))
            screen.blit(quit                  , (1152 - 350 + i, 704 -  60    ))
            
            for event in screen.GetEvent():
                pass
            
            i += 5
        
        Menu_Selection = True
        animjouer = False
    
    #animation de Menu_Selection à Menu_Principal
    while animmenu:
        
        i = 0
        
        while i<460:
        
            screen.flip()
            screen.blit(Fond_Menu_Principal, (0             , 0        ))
            screen.blit(joue               , (1152 - 500    , i + 4    ))
            screen.blit(credits            , (1152 + 10  - i, 704 - 180))
            screen.blit(option             , (1152 + 60  - i, 704 - 120))
            screen.blit(quit               , (1152 + 110 - i, 704 -  60))
            
            for event in screen.GetEvent():
                pass
                
            i += 5
            
        Menu_Principal = True
        animmenu = False

    screen.delais = 0.05
    
    LoadScreen = False
    
    while LoadScreen:
        
        pass