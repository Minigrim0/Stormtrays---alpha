import sys
import glob
import os
import time
import pygame
import pygame._view
import math
import random
import json
import codecs

from ConstantStormTrays import *
from pygame.locals import *
from TourClasse import *
from invocation import *
from QuestGiver import *
from RaceClasse import *
from BombClass import *
from ennemis import *
from classes import *
from Perso import *
from math import *

pygame.init()

screen = Screen((1152, 704), titre_jeu, IconImg, True, True)

f          = open("Properties.json")
Content    = f.read()
properties = json.loads(Content)

#------------------------------------------------------------------

Invoc_Tab     = [Invocation_1, Invocation_2, Invocation_3, Invocation_4, Invocation_5, Invocation_6]
Invoc_Tab_ret = [pygame.transform.flip(c, True, False) for c in Invoc_Tab]

#------------------------------------------------------------------

Tableau_Saves = []
Liste_Mechants = []

Compteur = 10
for filename in glob.glob("../Saves/*.json"):
    dirname, file = os.path.split(filename)
    file, ext = os.path.splitext(file)
    try:
        img = pygame.image.load(dirname+"/"+filename+"/SaveShot.png").convert_alpha()
    except:
        img = pygame.image.load("../Img/HUD/VideE.png").convert_alpha()
    nivrect = pygame.Rect((1152/2 - 10, Compteur), (500, 110))
    level = Levels(file, img, nivrect)
    Tableau_Saves.append(level)
    Compteur += 120
    
num = 0  
Liste_Tours = []
for filename in glob.glob("../Tours/*.json"):
    Liste_Tours.append(Tours(filename, num, myfont1))
    num += 1

niveau          = Niveau((18, 11))
King            = Perso()

invocation      = None

Programme_Actif = True
invoque_Boucle  = True
Menu_Principal  = True

affiche_nomTour = False
animInvocation  = False
LoadScreenLvl   = False
Menu_Options    = False
Credits_Anim    = False
Confirm_Quit    = False
MenuCampagne    = False
AfficheLvlUp    = False
OptionsMenu     = False
Ecran_Perdu     = False
anim_Perdu      = False
pausemenu       = False
Menu_Load       = False
animjouer       = False
menu_tour       = False
animmenu        = False
Menu_New        = False
Menu_Jeu        = False
deplace         = False
jeu             = False
lvl             = False

ListMobsInMenu = []
ListBombs      = []

TimeElapsed     = 0
Anim_King_i     = 0
TpsInvoc        = 0
TpsLvl          = 0
tps             = 0
T0              = 0

Difficulte      = properties["Difficulty"]
Volume          = properties["Volume"]

position_souris = (0, 0)

pygame.key.set_repeat(250, 25)
pygame.mixer.music.set_volume(Volume/10)

niveau.PlayMusic()

z = 10

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Tant que le programme tourne
while Programme_Actif:
    
    i = 0
    
    #Menu_Principal
    if Menu_Principal:
        screen.delais = 0
    while Menu_Principal:
        #Affiche les éléments du menu
        screen.blit(Fond_Menu_Principal, (        0,         0))
        screen.blit(joue               , (      652,       464))
        screen.blit(credits            , (      702,       524))
        screen.blit(option             , (      752,       584))
        screen.blit(quit               , (      802,       644))
        
        for x in range(z):
            screen.blit(FondSombre, (0,0))
        
        screen.flip()
        
        if z > 0:
            z -= 1
            
        #Musique
        niveau.PlayMusic()
        
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
                    Menu_Jeu = True
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
    if Menu_Jeu:
        x=0
        STime = time.clock()
        while x<=240:
            ETime = time.clock()-STime
            STime = time.clock()
            screen.blit(Fond_Menu_Principal, (     0,   0))
            screen.blit(loadImg            , (1392-x*2, 324))
            screen.blit(NewImg             , (1182-x, 364))
            screen.blit(ContinueImg        , (1092-x/2, 404))
            screen.blit(joue               , (   652, 464))
            screen.blit(credits            , (   702, 524))
            screen.blit(option             , (   752, 584))
            screen.blit(quit               , (   802, 644))
            screen.flip()
            x += 580*ETime
            
    while Menu_Jeu:

        screen.blit(Fond_Menu_Principal, (        0,         0))
        screen.blit(loadImg            , (      912,       324))
        screen.blit(NewImg             , (      942,       364))
        screen.blit(ContinueImg        , (      972,       404))
        screen.blit(joue               , (      652,       464))
        screen.blit(credits            , (      702,       524))
        screen.blit(option             , (      752,       584))
        screen.blit(quit               , (      802,       644))
        screen.flip()
        
        niveau.PlayMusic()
        
        for event in screen.GetEvent():
            
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                x=240
                STime = time.clock()
                while x>=0:
                    ETime = time.clock()-STime
                    STime = time.clock()
                    screen.blit(Fond_Menu_Principal, (       0,   0))
                    screen.blit(loadImg            , (1392-x*2, 324))
                    screen.blit(NewImg             , (1182-x  , 364))
                    screen.blit(ContinueImg        , (1092-x/2, 404))
                    screen.blit(joue               , (     652, 464))
                    screen.blit(credits            , (     702, 524))
                    screen.blit(option             , (     752, 584))
                    screen.blit(quit               , (     802, 644))
                    screen.flip()
                    x -= 580*ETime
                Menu_Jeu = False
                Menu_Principal = True
                
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
            
                if NewGameRect.collidepoint(event.pos):
                    Menu_Jeu = False
                    Menu_New = True
                    
                if ContinueGameRect.collidepoint(event.pos):
                    pass
                    
                if LoadGameRect.collidepoint(event.pos):
                    Menu_Load = True
                    Menu_Jeu = False
                    
#--------------------------------------------------------------------------------------------------------------------------------------------
    
    while Confirm_Quit:
        
        screen.blit(Fond_Menu_Principal, (  0,   0))
        screen.blit(ConfirmQuit        , (376, 152))
        screen.blit(reprise            , (516, 297))
        screen.blit(quitpaus           , (516, 367))
        screen.flip()
        
        #Musique
        niveau.PlayMusic()
        
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
    if Menu_Load:
        z = 60
        Compteur_Lvls = 10
        
    while Menu_Load:
        
        Compteur_Mini = z
        Compteur_Lvls = z
        
        #Affiche les éléments du menu
        screen.blit(Fond_Menu_Principal       , (        0,         0))
        screen.blit(Fond_Noir_Semi_Transparent, (        0,         0))
        
        for level in Tableau_Saves:
            Nom_Niveau = myfont.render(level.File, 1, (255, 255, 255))
            screen.blit(level.Img       , (586, Compteur_Lvls     ))
            screen.blit(Nom_Niveau,       (796, Compteur_Lvls + 45))
            level.Nivrect =  pygame.Rect(  (586, Compteur_Lvls), (500, 110))
            Compteur_Lvls += 120
            
        if len(Tableau_Saves) == 0:
            screen.blit(TowerFont.render("Aucune sauvegarde !", 1, (255, 255, 255)), (700, 340))
        
        screen.blit(retour             , ( 654,   0))
        screen.flip()
        
        #Musique
        niveau.PlayMusic()
            
        for event in screen.GetEvent():
            
            if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    Menu_Load = False
                    Menu_Principal = True
                
            if event.type == MOUSEBUTTONDOWN: 
                
                if event.button == 1:
                    
                    if retourrect.collidepoint(event.pos):
                        Menu_Principal = True
                        Menu_Load = False
                        break
            
                    for level in Tableau_Saves:
                        if level.Nivrect.collidepoint(event.pos):
                            LoadScreenLvl = True
                            lvl = level
                            Menu_Load = False
                            break
                
                elif event.button == 5:
                    
                    if z > -len(Tableau_Saves)*120 + 704:
                        z -= 50
                
                elif event.button == 4:
                    if z < 60:
                        z += 50

#--------------------------------------------------------------------------------------------------------------------------------------------
    
    if Menu_New:
        TabObjRaces  = []
        Writing = False
        Sex = "Male"
        Name = ""
        x=0
        for filename in glob.glob("../Img/HUD/RaceButtons/*.png"):
            Race = RaceObj(filename, x)
            TabObjRaces.append(Race)
            x+=1
        TabObjRaces[0].SetState(True)
                
    #Menu_Principal de création de partie
    while Menu_New:
        
        #Affiche les éléments du menu
        screen.blit(Fond_Menu_Principal       , (   0,   0))
        screen.blit(Fond_Noir_Semi_Transparent, (   0,   0))
        screen.blit(BackGroundPerso           , ( 755,  51))
        screen.blit(WomanIcon                 , (1000,  60))
        screen.blit(ManIcon                   , (1000, 105))
        screen.blit(TextZoneName              , ( 765, 410))
        for ObjRace in TabObjRaces:
            ObjRace.BlitDescription(screen)
        if Writing:
            screen.blit(Cursor, (755, 423))
        if Sex=="Male":
            screen.blit(Cursor, (990, 118))
        else:
            screen.blit(Cursor, (990, 73))
            
        screen.blit(retour, (654,   0))
        screen.blit(launch, (654, 654))
        screen.flip()
        
        #Musique
        niveau.PlayMusic()
            
        for event in screen.GetEvent():
            
            if event.type == KEYDOWN:
                
                if Writing:
                    if event.unicode.isalpha():
                        Name += event.unicode
                        TextZoneName.blit(myfont2.render(Name, 1, (0, 0, 0)), (5, 5))
                    elif event.key == K_SPACE:
                        Name += " "
                        TextZoneName.blit(myfont2.render(Name, 1, (0, 0, 0)), (5, 5))
                    elif event.key == K_BACKSPACE:
                        Name = Name[:-1]
                        TextZoneName = pygame.image.load("../Img/HUD/BackTxtName.png").convert_alpha()
                        TextZoneName.blit(myfont2.render(Name, 1, (0, 0, 0)), (5, 5))
                    elif event.key == K_RETURN:
                        Writing = False
                
                else:
                    if event.key == K_ESCAPE:
                        Menu_New = False
                        Menu_Principal = True
                
            if event.type == MOUSEBUTTONDOWN: 
                
                if event.button == 1:
                    
                    Writing = False
                    
                    for button in TabObjRaces:
                        button.GetSelected(event.pos, TabObjRaces)
                    
                    if retourrect.collidepoint(event.pos):
                        Menu_Principal = True
                        Menu_New = False
                        break
                        
                    if ManRect.collidepoint(event.pos):
                        Sex = "Male"
                        
                    if WomanRect.collidepoint(event.pos):
                        Sex = "Woman"
                        
                    if TextZoneRect.collidepoint(event.pos):
                        Writing = True
                    
                    if LaunchRect.collidepoint(event.pos):
                        if Name != "":
                            CurrentSave = '../Saves/'+Name+'.json'
                            Player = {}
                            Player["name"] = Name
                            Player["sex"] = Sex
                            Player["level"] = 1
                            for race in TabObjRaces:
                                if race.GotSelected():
                                    Player["race"] = race.GetName()
                            with open(CurrentSave, 'w', encoding='utf-8') as f:
                                json.dump(Player, f, indent=4)
                            Carte = niveau.CreateGame(Player["name"], Player["sex"], Player["race"])
                            Menu_New = False
                            MenuCampagne = True

#---------------------------------------------------------------------------------------------------------------------------
    while MenuCampagne:
        screen.blit(BackGroundCampaign, (0, 0))
        for Zone in Carte:
            Carte[Zone].BlitSelf(screen)
        
        for event in screen.GetEvent():
            if event.type == MOUSEMOTION:
                for Zone in Carte:
                    if Carte[Zone].Collide(event.pos):
                        pass
            if event.type == MOUSEBUTTONDOWN:
                MenuCampagne = False
                Menu_Principal = True
        screen.flip()

#---------------------------------------------------------------------------------------------------------------------------
    
    while Menu_Options:
        
        #Affiche les éléments du menu
        screen.blit(Fond_Menu_Principal, (0, 0))
        screen.blit(FondSombre         , (0, 0))
        
        #Musique
        niveau.PlayMusic()
        
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
                    if Difficulte > 1:
                        Difficulte -= 1

#--------------------------------------------------------------------------------------------------------------------------------------------
    
    while Credits_Anim:
        
        z = 0
        while z <= 2900:
            
            #Musique
            niveau.PlayMusic()
            
            screen.flip()
            screen.blit(Fond_Menu_Principal, (0, 0    ))
            screen.blit(Credits            , (0, 0 - z))
            z += 2
            
            for event in screen.GetEvent():
                
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    
                    Credits_Anim = False
                    z = 3000
                    
                if event.type == MOUSEBUTTONDOWN:
                    
                    if event.button == 5:
                        z += 40
                    elif event.button == 4:
                        z -= 40
                
        
        Menu_Principal = True
        Credits_Anim = False
        
#--------------------------------------------------------------------------------------------------------------------------------------------

    
    while jeu:
        
        niveau.deffond("../level/"+str(lvl.File)+".txt")
        niveau.construit("../level/"+str(lvl.File)+".txt")
        niveau.affichem(screen)
        
        Gandalf = QuestGiver("../level/"+str(lvl.File)+".txt_Pref.txt")
        Gandalf.LoadQuests(str(lvl.File))
        
        DicoEnnemiKilled = {}
        Liste_Mechants = []
        ListBombs      = []
        Liste_Tours_IG = []
        Tab_Projectile = []
        niveau.GoldTab = []
        
        count              = 0
        Level_Number       = 1
        TpsCoolDown        = 0
        TpsLvl             = 0
        Icapacite1         = 0
        Icapacite2         = 0
        Compteur_Iteration = 0
        TimeFromStart      = 0
        
        niveau.Nombre_Ennemis_Tue = 0
        niveau.Vie_Chateau        = 100
        niveau.gold               = 500
        
        King.targetCoordx = 528
        King.targetCoordy = 304
        King.Level_Roi    = 0
        King.objectif     = 10
        King.XpToAdd      = 0
        King.Vitesse      = 5
        King.Degats       = 3
        King.posx         = 0
        King.posy         = 304
        King.xp           = 0
        
        AfficheMessageAtStart = True
        ImgInvoc              = True
        HaveSeenLvl5Msg       = False
        AfficheStatTour       = False
        double_invoque        = False
        Accelerex2            = False
        Tps_Invoc_affiche     = False
        invocation            = None
        
        MessageAtStart = myfont2.render("Les hordes  ennemies arrivent ! Placez des tours pour les arrêter !", 1, (255, 20, 20))
        Time_50        = myfont2.render("0"                              , 1, (  0,  0,  0))
        message_argent = myfont2.render(""                               , 1, (255,  0,  0))
        
        if Accelerex2:
            TimeFromStart += 0.04*3.25
            if TpsCoolDown > 0:
                TpsCoolDown -= 0.04*3.25
        else:
            TimeFromStart += 0.04
            if TpsCoolDown > 0:
                TpsCoolDown -= 0.04
        
        #Musique
        niveau.PlayMusic()
        Gandalf.GiveRecompense(King.XpToAdd)
        
        #Augmentation du niveau
        if King.level_up():
            AfficheLvlUp = True
        
        #Mort Chateau
        if niveau.Vie_Chateau <= 0:
            InParty = False
            Ecran_Perdu = True
        
        #Construction + Affichage + Boutons
        Time = niveau.ConvertToHMS(round(TimeFromStart))
        Argent_Possede_Affiche = myfont2.render("Or : "      +str(niveau.gold)                             , 1, (  0,   0,   0))
        Vie_Chateau_Affiche    = myfont2.render("Bastion : " +str(int(niveau.Vie_Chateau)) + "pv."         , 1, (  0,   0,   0))
        Level_Num_Affiche      = myfont2.render("Niveau "    +str(King.Level_Roi)                          , 1, (  0,   0,   0))
        Degats_Roi_Affiche     = myfont2.render("Dégats : "  +str(King.Degats)                             , 1, (  0,   0,   0))
        Vitesse_Roi_Affiche    = myfont2.render("Vitesse : " +str(King.Vitesse)                            , 1, (  0,   0,   0))
        Temps_Txt              = myfont2.render(str(Time[0]) + "H" + str(Time[1]) + "M" +str(Time[2]) + "S", 1, (  0,   0,   0))
        Obj_Lvl_Txt            = myfont2.render(str(int(King.xp)) + "/" + str(King.objectif)               , 1, (  0,   0,   0))
        if niveau.Nombre_Ennemis_Tue > 1000000:
            Ennemi_Tue_Affiche = myfont2.render("Victimes : "+str(niveau.Nombre_Ennemis_Tue//1000000)+"M"  , 1, (  0,   0,   0))
        elif niveau.Nombre_Ennemis_Tue > 1000:
            Ennemi_Tue_Affiche = myfont2.render("Victimes : "+str(niveau.Nombre_Ennemis_Tue//1000)+"K"     , 1, (  0,   0,   0))
        else:
            Ennemi_Tue_Affiche = myfont2.render("Victimes : "+str(niveau.Nombre_Ennemis_Tue)               , 1, (  0,   0,   0))
        if TpsCoolDown > 0:
            Tps_Invoc_affiche  = myfont2.render(str(round(TpsCoolDown)), 1, (255, 255, 255))
        else:
            Tps_Invoc_affiche  = False
        
        Current_Xp = pygame.Surface(((King.xp/King.objectif)*255, 18))
        Current_Xp.fill((20, 255, 40))
        
        niveau.affichem(screen)
        King.vit(Liste_Mechants, niveau, Coin)
        
        if King.capacite1:
            Icapacite1 += 1
            if Icapacite1 == 160:
                Icapacite1 = 0
                King.capacite1 = False
        if King.capacite2:
            Icapacite2 += 1
            if Icapacite2 == 160:
                Icapacite2 = 0
                King.capacite2 = False
            for ennemi in Liste_Mechants:
                ennemi.BlitInPlace(screen)
        else:
            for ennemi in Liste_Mechants:
                ennemi.bouge(niveau.tableau, screen, niveau, Liste_Mechants, Coin, King)
                ennemi.meurt.set_volume(Volume/10)
        
        for Bomb in ListBombs:
            Bomb.Live(screen, Liste_Mechants, niveau, Coin, King, ListBombs)
        
        for projectileObj in Tab_Projectile:
            projectileObj.Avance(screen, Liste_Mechants, niveau, Coin, Tab_Projectile, King)
        
        #Faire attaquer les tours
        for tour in Liste_Tours_IG:
            tour.attaque(tour.Position_IG, Liste_Mechants, niveau, Coin, Tab_Projectile)
            tour.affiche_jeu(screen)
            
        if invocation:
            if not invocation.vit(screen, Liste_Mechants, niveau, Coin, King):
                King.XpToAdd += invocation.xp
                invocation = None
        
        Level_Difficulty = niveau.Set_Difficulty(Difficulte)
        
        if niveau.Nombre_Ennemis_Tue >= 5000:
            double_invoque = True
        
        while invoque_Boucle:
            DoSummon = random.randrange(Level_Difficulty)
            if DoSummon == 0 and King.Level_Roi > 0:
                AfficheMessageAtStart = False
                invoque = random.randrange(10)
                if invoque == 0 and King.Level_Roi >= 3:
                    ennemi = Ennemi_IG("../Ennemis/Orc.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 1 or invoque == 2 or invoque == 3:
                    ennemi = Ennemi_IG("../Ennemis/Goblin.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 4 and King.Level_Roi >= 4:
                    ennemi = Ennemi_IG("../Ennemis/Knight.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 5 and King.Level_Roi >= 3:
                    ennemi = Ennemi_IG("../Ennemis/Ghost.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 6 and King.Level_Roi >= 2:
                    ennemi = Ennemi_IG("../Ennemis/Golem.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 7:
                    invoque = random.randrange(5)
                    if invoque == 1 and King.Level_Roi >= 5:
                        ennemi = Ennemi_IG("../Ennemis/Dwarf.json")
                        ennemi.pose_ennemi(niveau.tableau, screen)
                        Liste_Mechants.append(ennemi)
                    elif invoque == 0 and King.Level_Roi >= 7:
                        ennemi = Ennemi_IG("../Ennemis/Dragon.json")
                        ennemi.pose_ennemi(niveau.tableau, screen)
                        Liste_Mechants.append(ennemi)
                elif invoque == 8 or invoque == 9:
                    ennemi = Ennemi_IG("../Ennemis/Puke.json")
                    ennemi.pose_ennemi(niveau.tableau, screen)
                    Liste_Mechants.append(ennemi)
                elif invoque == 10:
                    invoque = random.randrange(5)
                    if invoque == 1 and King.Level_Roi >= 4:
                        ennemi = Ennemi_IG("../Ennemis/Puke.json")
                        ennemi.pose_ennemi(niveau.tableau, screen)
                        Liste_Mechants.append(ennemi)
                if double_invoque == True:  
                    double_invoque = False
                    pass
                else:
                    invoque_Boucle = False
                
            invoque_Boucle = False
                    
        invoque_Boucle = True
            
        #Si le Menu des tours est actif
        if menu_tour:
        
            screen.blit(Quadrille, (0, 0))
            if deplace:
                screen.blit(Poubelle, (15, 15))
                tourSelectionee.bougetoursouris(position_souris, screen)
                
            else:
                screen.blit(menutour, (0, 604))
                
                num = 0
                for tour in Liste_Tours:
                    tour.affichemenu(screen, num)
                    num += 1
                
                    #affiche le nom de la tour
                    if tour.tourrect.collidepoint(position_souris):
                        
                        StatTourCurseur = TowerFont.render(tour.nom, 1, (0, 0, 0))
                        screen.blit(StatTourCurseur, (15,  15))
                        NameTower = tour.nom
                        
                        if niveau.gold < tour.prix:
                        
                            message_argent = TowerFont.render("Pas assez d'argent !", 1, (255, 20, 20))
                            screen.blit(message_argent, (15,  50))
                            
        Gandalf.Live(screen)
        screen.blit(King.nanim            , (King.posx , King.posy))
        screen.blit(FondHautDroite        , (1152 - 390,         0))
        screen.blit(FondHautDroite        , (1152 - 282,         0))
        screen.blit(Argent_Possede_Affiche, (1152 - 280,         2))
        screen.blit(Level_Num_Affiche     , (1152 - 132,         2))
        screen.blit(Vie_Chateau_Affiche   , (1152 - 280,        27))
        screen.blit(Ennemi_Tue_Affiche    , (1152 - 132,        27))
        screen.blit(Vitesse_Roi_Affiche   , (1152 - 280,        54))
        screen.blit(Degats_Roi_Affiche    , (1152 - 132,        54))
        screen.blit(Current_Xp            , (1152 - 270,        86))
        screen.blit(XpBar                 , (1152 - 282,        80))
        screen.blit(Obj_Lvl_Txt           , (1152 - 155,        82))
        screen.blit(pause                 , (       820,         5))
        screen.blit(Temps_Txt             , (1152 - 385,        55))
        if Tps_Invoc_affiche and King.Level_Roi >= 5:          
            screen.blit(TpsRestInvocSombre, (1152 - 450,        10))
            screen.blit(Tps_Invoc_affiche , (1152 - 435,        25))
        elif King.Level_Roi >= 5:                              
            screen.blit(TpsRestInvoc      , (1152 - 450,        10))
            if not HaveSeenLvl5Msg:
                screen.blit(InfoLvl5Img   , (         0,         0))
        if AfficheMessageAtStart:
            screen.blit(MessageAtStart, (0, 0))
        if King.capacite1:
            CapaciteTxt1 = myfont2.render("DOUBLE OR !", 1, (255, 20, 20))
            screen.blit(CapaciteTxt1, (0, 10))
        if King.capacite2:
            CapaciteTxt2 = myfont2.render("ENNEMIS COINCES !", 1, (255, 20, 20))
            screen.blit(CapaciteTxt2, (0, 40))
        
        if AfficheLvlUp:
    
            TpsLvl += 1
            if TpsLvl < 30:
                screen.blit(Tab_AnimLvlUp[TpsLvl//3]  , (426, 277))
            elif TpsLvl <= 50:
                screen.blit(Tab_AnimLvlUp[9]  , (426, 277))
            else:
                TpsLvl = 0
                AfficheLvlUp = False
                
        if AfficheStatTour:
            
            NbEnnemiKilled = myfont2.render("Ennemis tués : " + str(SelectedTower4AfficheStat.EnnemiKilled), 1, (0, 0, 0))
            DispensedDamage = myfont2.render("Dégâts dispensés : "     + str(SelectedTower4AfficheStat.TotalDegats) , 1, (0, 0, 0))
            pygame.draw.circle(screen.fenetre, pygame.Color("red"), (SelectedTower4AfficheStat.Position_IG[0]*64 + 32, SelectedTower4AfficheStat.Position_IG[1]*64 + 32), SelectedTower4AfficheStat.portee*64 + 20, 3)
            screen.blit(FondHautDroite , (1152-282, 704-81))
            screen.blit(NbEnnemiKilled , (1152-282, 704-80))
            screen.blit(DispensedDamage, (1152-282, 704-55))
            screen.blit(SellButton     , (1152-272, 704-25))
        
        if animInvocation:
            King.targetCoordx, King.targetCoordy = King.posx, King.posy
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
                King.nanim = King.King_1
                animInvocation = False
                if King.Level_Roi >= 6:
                    King.capacite1 = True
                if King.Level_Roi >= 8:
                    King.capacite2 = True
            else:
                Invoc_Avancee = pygame.Surface(((TpsInvoc/120)*177, 12))
                Invoc_Avancee.fill((215, 75, 0))
                screen.blit(Invoc_Avancee, (1152 - 182, 109))
                screen.blit(InvocBar     , (1152 - 188, 105))
                
        if not menu_tour:
            screen.blit(boutontour     , (  32, 654))
        if Accelerex2:
            screen.blit(accelerex      , ( 770,   5))
        else:                                                  
            screen.blit(accelere       , ( 770,   5))
        
        for Gold in niveau.GoldTab:
            Gold.bouge(screen, Coin, Gold, niveau)
        
        #Events du jeu
        for event in screen.GetEvent():
            
            #Si l'on est dans le Menu des tours
            if menu_tour:
        
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    
                    if deplace and not mtrect.collidepoint(event.pos) and not PoubelleRect.collidepoint(event.pos):
                        
                        if niveau.tableau[(position_souris[0])//(64), (position_souris[1])//(64)] == ('  ', 0):
                            niveau.gold -= tourSelectionee.prix
                            Liste_Tours_IG.append(tourSelectionee)
                            tourSelectionee.placetour(position_souris, screen, niveau.tableau, Liste_Tours_IG, tourSelectionee, niveau)
                            King.XpToAdd += tourSelectionee.prix//10
                            deplace = False
                            menu_tour = False
                            DicoTowersBought[NameTower] += 1
                            break
                            
                    #Pour quitter le Menu des tours
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
                                tourSelectionee = Tours_IG(tour, num, tour.DirImg)
                                message_argent = myfont2.render("", 1, (255, 0, 0))
                            
            #si on est pas dans Menu des tour
            if not menu_tour:
                
                message_argent = myfont2.render("", 1, (255, 0, 0))
                deplace = False
                
                if event.type == KEYDOWN and not animInvocation:
                    
                    k = pygame.key.get_pressed()
                        
                    if k[K_i]:
                        if King.Level_Roi >= 5 and not invocation and TpsCoolDown < 1:
                            animInvocation = True
                            TpsCoolDown = 110
                            
                    if k[K_b]:
                        if niveau.gold >= 25:
                            niveau.gold -= 25
                            Bombe = Bomb(King.posx, King.posy, 5)
                            ListBombs.append(Bombe)
                        
                if event.type == MOUSEBUTTONUP:
                    
                    King.IsMoving = False
                
                if event.type == MOUSEBUTTONDOWN:
                    
                    if AfficheStatTour and event.button == 1:
                        if SellRect.collidepoint(event.pos):
                            Liste_Tours_IG.remove(SelectedTower4AfficheStat)
                            niveau.gold += round(SelectedTower4AfficheStat.prix*0.75)
                            niveau.tableau[SelectedTower4AfficheStat.Position_IG[0], SelectedTower4AfficheStat.Position_IG[1]] = ('  ', 0)
                            AfficheStatTour = False
                            
                    if Gandalf.HitBox.collidepoint(event.pos) and event.button == 1:
                        Gandalf.IsGiving = not Gandalf.IsGiving
                    
                    #Menu_Principal tour actif
                    if boutontourrect.collidepoint(event.pos) and event.button == 1:
                        menu_tour = True
                    
                    if event.button == 3 and not animInvocation:
                        
                        if Liste_Mechants:
                        
                            for ennemi in Liste_Mechants:
                        
                                if ennemi.HitBox.collidepoint(event.pos):
                                    King.target = ennemi
                                    break
                                
                                else:
                                    King.target = None
                                    King.IsMoving = True
                                    King.targetCoordx = event.pos[0] - 48
                                    King.targetCoordy = event.pos[1] - 48
                                    
                        else:
                            King.target = None
                            King.IsMoving = True
                            King.targetCoordx = event.pos[0] - 48
                            King.targetCoordy = event.pos[1] - 48
                        
            #Si l'on est dans le Menu_Principal de tour ou pas
            if event.type == MOUSEMOTION:
                
                position_souris = event.pos
                if King.IsMoving:
                    King.targetCoordx = event.pos[0] - 48
                    King.targetCoordy = event.pos[1] - 48
            
            #Bouton Pause
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                
                AfficheStatTour = False
                
                if King.Level_Roi >= 5 and HaveSeenLvl5Msg == False:
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
                
                if event.key == K_a:
                    Accelerex2 = not Accelerex2
                    if Accelerex2:
                        screen.delais = 0.05/4
                    else:
                        screen.delais = 0.05
                    
        screen.flip()
        
#-----------------------------------------------------------------------------------------------------------
        
        if pausemenu:
            screen.blit(FondSombre, (0, 0))
        
        #tant que Menu_Principal pause est actif
        while pausemenu:
        
            niveau.PlayMusic()
                    
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
        
            niveau.PlayMusic()
            
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
                        if Difficulte > 1:
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

    screen.delais = 0.05
    z = 0