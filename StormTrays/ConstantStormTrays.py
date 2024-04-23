import os
import time
import pygame
from pygame.locals import *

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
fenetre = pygame.display.set_mode((750, 305), NOFRAME)

LoadScreen = pygame.image.load("../Img/FondMenu/LoadingScreen.png").convert_alpha()
fenetre.blit(LoadScreen, (0, 0))
pygame.display.flip()

titre_jeu            = "StormTrays - 0 - Beta 2.0"
IconImg              = "../Img/Icon/Icon.png"

Defeat_Song = "../musique/Defeat.wav"

Tab_AnimLvlUp = {}
Tab_AnimLvlUp[0] = pygame.image.load("../Img/LevelUp/AnimLvlUp01.png").convert_alpha()
Tab_AnimLvlUp[1] = pygame.image.load("../Img/LevelUp/AnimLvlUp02.png").convert_alpha()
Tab_AnimLvlUp[2] = pygame.image.load("../Img/LevelUp/AnimLvlUp03.png").convert_alpha()
Tab_AnimLvlUp[3] = pygame.image.load("../Img/LevelUp/AnimLvlUp04.png").convert_alpha()
Tab_AnimLvlUp[4] = pygame.image.load("../Img/LevelUp/AnimLvlUp05.png").convert_alpha()
Tab_AnimLvlUp[5] = pygame.image.load("../Img/LevelUp/AnimLvlUp06.png").convert_alpha()
Tab_AnimLvlUp[6] = pygame.image.load("../Img/LevelUp/AnimLvlUp07.png").convert_alpha()
Tab_AnimLvlUp[7] = pygame.image.load("../Img/LevelUp/AnimLvlUp08.png").convert_alpha()
Tab_AnimLvlUp[8] = pygame.image.load("../Img/LevelUp/AnimLvlUp09.png").convert_alpha()
Tab_AnimLvlUp[9] = pygame.image.load("../Img/LevelUp/AnimLvlUp10.png").convert_alpha()

king_1         = "../Img/Perso/King/King_1.png"
king_2         = "../Img/Perso/King/King_2.png"
king_3         = "../Img/Perso/King/King_3.png"
king_4         = "../Img/Perso/King/King_4.png"
king_5         = "../Img/Perso/King/King_5.png"
king_6         = "../Img/Perso/King/King_6.png"

king_Attak     = "../Img/Perso/King/King_Attak.png"
king_Attak2    = "../Img/Perso/King/King_Attak2.png"

king_1Ret      = "../Img/Perso/King/KingRet_1.png"
king_2Ret      = "../Img/Perso/King/KingRet_2.png"
king_3Ret      = "../Img/Perso/King/KingRet_3.png"
king_4Ret      = "../Img/Perso/King/KingRet_4.png"
king_5Ret      = "../Img/Perso/King/KingRet_5.png"
king_6Ret      = "../Img/Perso/King/KingRet_6.png"

kingRet_Attak  = "../Img/Perso/King/KingRet_Attak.png"
kingRet_Attak2 = "../Img/Perso/King/KingRet_Attak2.png"

Invocation_Attak     = "../Img/Perso/King/Invocation/King_Attak.png"
Invocation_Attak2    = "../Img/Perso/King/Invocation/King_Attak2.png"

InvocationRet_Attak  = "../Img/Perso/King/Invocation/KingRet_Attak.png"
InvocationRet_Attak2 = "../Img/Perso/King/Invocation/KingRet_Attak2.png"

#images
Coin                       = pygame.image.load("../Img/GoldIcon.png").convert_alpha()
fond                       = pygame.image.load("../Img/Fonds/fond1.png").convert_alpha()

Cursor                     = pygame.image.load("../Img/HUD/RaceButtons/Properties/Cursor.png").convert_alpha()
BackGroundPerso            = pygame.image.load("../Img/HUD/PlayerBackGround.png").convert_alpha()
Fond_Menu_Opt              = pygame.image.load("../Img/HUD/Fond_Options.png").convert_alpha()
Quadrille                  = pygame.image.load("../Img/HUD/Quadrillage.png").convert_alpha()
FondHautDroite             = pygame.image.load("../Img/HUD/Haut_Droite.png").convert_alpha()
ConfirmQuit                = pygame.image.load("../Img/HUD/ConfirmQuit.png").convert_alpha()
TextZoneName               = pygame.image.load("../Img/HUD/BackTxtName.png").convert_alpha()
FondSombre                 = pygame.image.load("../Img/HUD/SombreFull.png").convert_alpha()
menutour                   = pygame.image.load("../Img/HUD/menutours.png").convert_alpha()
Poubelle                   = pygame.image.load("../Img/HUD/poubelle.png").convert_alpha()
Fond_Noir_Semi_Transparent = pygame.image.load("../Img/HUD/sombre.png").convert_alpha()
InvocBar                   = pygame.image.load("../Img/HUD/Invoc.png").convert_alpha()
WomanIcon                  = pygame.image.load("../Img/HUD/Woman.png").convert_alpha()
ManIcon                    = pygame.image.load("../Img/HUD/Man.png").convert_alpha()
XpBar                      = pygame.image.load("../Img/HUD/Xp.png").convert_alpha()

TpsRestInvocSombre         = pygame.image.load("../Img/Perso/King/TpsInvocSomb.png").convert_alpha()
TpsRestInvoc               = pygame.image.load("../Img/Perso/King/TpsInvoc.png").convert_alpha()

InfoLvl5Img                = pygame.image.load("../Img/Textes/Lvl5Info.png").convert_alpha()
Credits                    = pygame.image.load("../Img/Textes/Credits.png").convert_alpha()
OptionsTxt                 = pygame.image.load("../Img/Textes/OPTION.png").convert_alpha()
Moins                      = pygame.image.load("../Img/Textes/Moins.png").convert_alpha()
PauseTxt                   = pygame.image.load("../Img/Textes/PAUSE.png").convert_alpha()
Plus                       = pygame.image.load("../Img/Textes/Plus.png").convert_alpha()

boutontour                 = pygame.image.load("../Img/Boutons/boutonmenutour.png").convert_alpha()
optionpaus                 = pygame.image.load("../Img/Boutons/optionpause.png").convert_alpha()
accelerex                  = pygame.image.load("../Img/Boutons/accelerex.png").convert_alpha()
quitpaus                   = pygame.image.load("../Img/Boutons/quitpaus.png").convert_alpha()
ContinueImg                = pygame.image.load("../Img/Boutons/continue.png").convert_alpha()
accelere                   = pygame.image.load("../Img/Boutons/accelere.png").convert_alpha()
reprise                    = pygame.image.load("../Img/Boutons/reprise.png").convert_alpha()
option                     = pygame.image.load("../Img/Boutons/options.png").convert_alpha()
credits                    = pygame.image.load("../Img/Boutons/credits.png").convert_alpha()
retour                     = pygame.image.load("../Img/Boutons/retour.png").convert_alpha()
launch                     = pygame.image.load("../Img/Boutons/launch.png").convert_alpha()
joue                       = pygame.image.load("../Img/Boutons/jouer.png").convert_alpha()
pause                      = pygame.image.load("../Img/Boutons/pause.png").convert_alpha()
SellButton                 = pygame.image.load("../Img/Boutons/sell.png").convert_alpha()
quit                       = pygame.image.load("../Img/Boutons/quit.png").convert_alpha()
loadImg                    = pygame.image.load("../Img/Boutons/load.png").convert_alpha()
NewImg                     = pygame.image.load("../Img/Boutons/new.png").convert_alpha()

Fond_Menu_Principal        = pygame.image.load("../Img/FondMenu/FondMenuPrincipal.png").convert_alpha()
Loading_Screen_Road2       = pygame.image.load("../Img/FondMenu/LoadLevel.png").convert_alpha()
LoadBarImg                 = pygame.image.load("../Img/FondMenu/LoadBar.png").convert_alpha()

#Cartes Menu de Campagne
HighLighted_Draconnian     = pygame.image.load("../Img/FondMenu/Maps/DraconnianMap.png").convert_alpha()
BackGroundCampaign         = pygame.image.load("../Img/FondMenu/Maps/CampaignMap.png").convert_alpha()
HighLighted_HighELf        = pygame.image.load("../Img/FondMenu/Maps/HighElfMap.png").convert_alpha()
HighLighted_Spirit         = pygame.image.load("../Img/FondMenu/Maps/SpiritMap.png").convert_alpha()
HighLighted_Dwarf          = pygame.image.load("../Img/FondMenu/Maps/DwarfMap.png").convert_alpha()
HighLighted_Human          = pygame.image.load("../Img/FondMenu/Maps/HumanMap.png").convert_alpha()
HighLighted_Gnome          = pygame.image.load("../Img/FondMenu/Maps/GnomeMap.png").convert_alpha()
HighLighted_Ogre           = pygame.image.load("../Img/FondMenu/Maps/OgreMap.png").convert_alpha()
HighLighted_Orc            = pygame.image.load("../Img/FondMenu/Maps/OrcMap.png").convert_alpha()

InvoqueAnim1               = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_1.png").convert_alpha()
InvoqueAnim2               = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_2.png").convert_alpha()
InvoqueAnim3               = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_3.png").convert_alpha()
InvoqueAnim4               = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_4.png").convert_alpha()
InvoqueAnim5               = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_5.png").convert_alpha()
InvoqueAnim6               = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_6.png").convert_alpha()
InvoqueAnim7               = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_7.png").convert_alpha()
InvoqueAnim8               = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_8.png").convert_alpha()
InvoqueAnim9               = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_9.png").convert_alpha()
InvoqueAnim10              = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_10.png").convert_alpha()
InvoqueAnim11              = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_11.png").convert_alpha()
InvoqueAnim12              = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_12.png").convert_alpha()
InvoqueAnim13              = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_13.png").convert_alpha()
InvoqueAnim14              = pygame.image.load("../Img/Perso/King/Invoque/King_Invoc_14.png").convert_alpha()
                        
Invocation_1               = pygame.image.load("../Img/Perso/King/Invocation/King_1.png").convert_alpha()
Invocation_2               = pygame.image.load("../Img/Perso/King/Invocation/King_2.png").convert_alpha()
Invocation_3               = pygame.image.load("../Img/Perso/King/Invocation/King_3.png").convert_alpha()
Invocation_4               = pygame.image.load("../Img/Perso/King/Invocation/King_4.png").convert_alpha()
Invocation_5               = pygame.image.load("../Img/Perso/King/Invocation/King_5.png").convert_alpha()
Invocation_6               = pygame.image.load("../Img/Perso/King/Invocation/King_6.png").convert_alpha()
                        
Invocation_1_ret           = pygame.image.load("../Img/Perso/King/Invocation/KingRet_1.png").convert_alpha()
Invocation_2_ret           = pygame.image.load("../Img/Perso/King/Invocation/KingRet_2.png").convert_alpha()
Invocation_3_ret           = pygame.image.load("../Img/Perso/King/Invocation/KingRet_3.png").convert_alpha()
Invocation_4_ret           = pygame.image.load("../Img/Perso/King/Invocation/KingRet_4.png").convert_alpha()
Invocation_5_ret           = pygame.image.load("../Img/Perso/King/Invocation/KingRet_5.png").convert_alpha()
Invocation_6_ret           = pygame.image.load("../Img/Perso/King/Invocation/KingRet_6.png").convert_alpha()

GoldGained = [1]
GoldGained[0] = 0

DicoTowersBought                          = {}
DicoTowersBought["Archer"]                = 0
DicoTowersBought["Baliste"]               = 0
DicoTowersBought["Catapulte Rapide"]      = 0
DicoTowersBought["Catapulte Basique"]     = 0
DicoTowersBought["Catapulte Precise"]     = 0
DicoTowersBought["Catapulte tres rapide"] = 0

DicoEnnemisKilled                 = {}
DicoEnnemisKilled["Orc"]          = 0
DicoEnnemisKilled["Wolf"]         = 0
DicoEnnemisKilled["Dwarf"]        = 0
DicoEnnemisKilled["Ghost"]        = 0
DicoEnnemisKilled["Golem"]        = 0
DicoEnnemisKilled["Dragon"]       = 0
DicoEnnemisKilled["Goblin"]       = 0
DicoEnnemisKilled["Knight"]       = 0
DicoEnnemisKilled["PukeMonster"]  = 0

#Rectangles
jouerect         = pygame.Rect((1152    - 500, 704    - 240), (500,  50))
credirect        = pygame.Rect((1152    - 450, 704    - 180), (500,  50))
optionrect       = pygame.Rect((1152    - 400, 704    - 120), (500,  50))
quitrect         = pygame.Rect((1152    - 350, 704    -  60), (500,  50))
retourrect       = pygame.Rect((1152    - 500,            0), (500,  50))
pauserect        = pygame.Rect((1152    - 332,            5), ( 40,  40))
accelererect     = pygame.Rect((1152    - 382,            5), ( 40,  40))
boutontourrect   = pygame.Rect((32           , 704    -  50), ( 45,  45))
mtrect           = pygame.Rect((975          , 704    -  89), ( 15,  15))
reprendrect      = pygame.Rect((1152//2 - 100, 704//2 -  85), (120,  50))
optionprect      = pygame.Rect((1152//2 - 100, 704//2 -  25), (120,  50))
quitjrect        = pygame.Rect((1152//2 - 100, 704//2 +  35), (120,  50))
quitOrect        = pygame.Rect((1152//2 - 100, 704//2 +  55), (120,  50))
VolMoins         = pygame.Rect((          655,          302), ( 40,  40))
VolPlus          = pygame.Rect((          705,          302), ( 40,  40))
DifMoins         = pygame.Rect((          655,          347), ( 40,  40))
DifPlus          = pygame.Rect((          705,          347), ( 40,  40))
ConfirmReprise   = pygame.Rect((1152//2 -  60, 704//2 -  55), (120,  50))
ConfirmQuitter   = pygame.Rect((1152//2 -  60, 704//2 +  15), (120,  50))
PoubelleRect     = pygame.Rect((           15,           15), ( 40,  40))
InfoLvl5Rect     = pygame.Rect((            0,            0), (750, 113))
SellRect         = pygame.Rect((1152    - 282, 704    -  30), (120,  24))
LoadGameRect     = pygame.Rect((          912,          324), (240,  30))
NewGameRect      = pygame.Rect((          942,          364), (240,  30))
ContinueGameRect = pygame.Rect((          972,          404), (240,  30))
ManRect          = pygame.Rect((          1000,         105), ( 40,  40))
WomanRect        = pygame.Rect((          1000,          60), ( 40,  40))
TextZoneRect     = pygame.Rect((          765,          410), (220,  40))
LaunchRect       = pygame.Rect((          654,          654), (500,  50))

myfont    = pygame.font.Font("../Police/Viner Hand ITC.ttf",  25)
myfontt   = pygame.font.Font("../Police/Viner Hand ITC.ttf", 100)
myfont2   = pygame.font.Font("../Police/Viner Hand ITC.ttf",  20)
myfont3   = pygame.font.Font("../Police/Viner Hand ITC.ttf",  40)
myfont1   = pygame.font.Font("../Police/Viner Hand ITC.ttf",  13)
TowerFont = pygame.font.Font("../Police/Viner Hand ITC.ttf",  35)

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