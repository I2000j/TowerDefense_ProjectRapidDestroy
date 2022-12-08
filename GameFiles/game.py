import pygame
import random
import math
import webbrowser
import os
import socket
import time

license = True

if license == False:
    userLogin = os.getlogin()
    userIp = socket.gethostbyname(socket.gethostname()) 
    print('Купите лицензию!!! Я знаю ваш логин: ' + userLogin + ' и еще я знаю ваш IP: ' + userIp)
    file = open("C:/Users/student/Desktop/YouBeenHacked.txt", "w")
    file.write('Купите лицензию на сайте!!! Я знаю ваш логин: ' + userLogin + ' и еще я знаю ваш IP: ' + userIp + ' GG')
    file.close()

pygame.init()

BG_SIZE = (1200,680)
FPS = 60

gameName = 'TowerDefence-Project.Rapid_Destroy'
versionGame = 'V - 0.8.1'

running = True
pygame.mouse.set_visible(False)

antiplag = pygame.sprite.Sprite()
antiplag = pygame.image.load('AntiPlag.png')
antiplag_rect = antiplag.get_rect()
antiplag = pygame.transform.scale(antiplag, BG_SIZE)

screen = pygame.display.set_mode(BG_SIZE)
rtext = random.randint(1,35)
pygame.display.set_icon(pygame.image.load('logoGame.ico'))
screen.blit(antiplag, antiplag_rect)
pygame.display.update()

time.sleep(3)

loading = pygame.sprite.Sprite()
loading = pygame.image.load('loading.jpg')
loading_rect = loading.get_rect()
loading = pygame.transform.scale(loading, BG_SIZE)

screen.blit(loading, loading_rect)
pygame.display.update()
langRus = True
def rtexts():
    if langRus == True:
        if rtext == 1:
            pygame.display.set_caption( gameName + ' | Совет: если вы новичок пройдите обучение.')
        if rtext == 2:
            pygame.display.set_caption( gameName + ' | Совет: на сложном режиме используйте генераторы.')
        if rtext == 3:
            pygame.display.set_caption( gameName + ' | Совет: лучше ставить стены в начале.')
        if rtext == 4:
            pygame.display.set_caption( gameName + ' | Интересный факт: эта игра по мотивам Mindustry.')
        if rtext == 5:
            pygame.display.set_caption( gameName + ' | Совет: Пушка двигается на E/Q')
        if rtext == 6:
            pygame.display.set_caption( gameName + ' | Вопрос: Это вообще хоть кто-то читает?')
        if rtext == 7:
            pygame.display.set_caption( gameName + ' | Больше обновлений не выйдет!(Возможно)')
        if rtext == 8:
            pygame.display.set_caption( gameName + ' | Интересный факт: Тут миллион названий окна.')
        if rtext == 9:
            pygame.display.set_caption( gameName + ' | Интересный факт: Разрабатывалось меньше месяца.')
        if rtext == 10:
            pygame.display.set_caption( gameName + ' | Интересный факт: картинки с GITHUB.')
        if rtext == 11:
            pygame.display.set_caption( gameName + ' | Совет: Если вы не можете пройти игру так, используйте AirDrop.')
        if rtext == 12:
            pygame.display.set_caption( gameName + ' | Совет: Вы можете включить английский язык!')
        if rtext == 13:
            pygame.display.set_caption( gameName + ' | Совет: не играйте слишком много!')
        if rtext == 14:
            pygame.display.set_caption( gameName + ' | Спасибо за игру в игру!')
        if rtext == 15:
            pygame.display.set_caption( gameName + ' | Интересный факт: Это пятнадцатая вариация текста.')
        if rtext == 16:
            pygame.display.set_caption( gameName + ' | Интересный факт: Разработано трудом!')
        if rtext == 17:
            pygame.display.set_caption( gameName + ' | Совет: если вам скучно поиграйте с чит-панелью.')
        if rtext == 18:
            pygame.display.set_caption( gameName + ' | Интересный факт: HardMode не очень сложный!')
        if rtext == 19:
            pygame.display.set_caption( gameName + ' | ...')
        if rtext == 20:
            pygame.display.set_caption( gameName + ' | Сколько времени ушло на это...')
        if rtext == 21:
            pygame.display.set_caption( gameName + ' | Совет: Даже не пытайтесь прочитать все сообщения от автора!')
        if rtext == 22:
            pygame.display.set_caption(gameName)
        if rtext == 23:
            pygame.display.set_caption( gameName + ' | Совет: Also try to play terraria!')
        if rtext == 24:
            pygame.display.set_caption( gameName + ' | Интересный факт: Эти сообщения занимают 69 строчек кода!')
        if rtext == 25:
            pygame.display.set_caption( gameName + ' | Совет: Попробуйте включить DLC.')
        if rtext == 26:
            pygame.display.set_caption( gameName + ' | Интересный факт: тут я научился работать с Python: https://jetcode.org')
        if rtext == 27:
            pygame.display.set_caption( gameName + ' | Совет: Попробуйте ставить пушки на поздних стадиях игры!')
        if rtext == 28:
            pygame.display.set_caption( gameName + ' | Интересный факт: не думайте, что код я позаимствовал с оригинала, ведь он на Java!')
        if rtext == 29:
            pygame.display.set_caption( gameName + ' | Интересный факт: Это расшифрованное название игры.')
        if rtext == 30:
            pygame.display.set_caption('TD-P.RD | Разгадывайте это сами!')
        if rtext == 31:
            pygame.display.set_caption( gameName + ' | Совет: Советую читать файлы: READ ME.txt')
        if rtext == 32:
            pygame.display.set_caption( gameName + ' | Интересный факт: Не все обратят на это внимание...')
        if rtext == 33:
            pygame.display.set_caption( gameName + ' | Интересный факт: Это не Mindustry...')
        if rtext == 34:
            pygame.display.set_caption( gameName + ' | Интересный факт: Это предпоследнее сообщение(А может и нет).')
        if rtext == 35:
            pygame.display.set_caption( gameName + ' | Я надеюсь, что вам понравится эта игра!')
    else:
        if rtext == 1:
            pygame.display.set_caption( gameName + ' | Tip: if you are a beginner, complete the training.')
        if rtext == 2:
            pygame.display.set_caption( gameName + ' | Tip: Use generators in hard mode.')
        if rtext == 3:
            pygame.display.set_caption( gameName + ' | Tip: it is better to put the walls at the beginning.')
        if rtext == 4:
            pygame.display.set_caption( gameName + ' | Interesting fact: This game is based on Mindustry.')
        if rtext == 5:
            pygame.display.set_caption( gameName + ' | Tip: The cannon moves on E/Q')
        if rtext == 6:
            pygame.display.set_caption( gameName + ' | Question: Does anyone read this at all?')
        if rtext == 7:
            pygame.display.set_caption( gameName + ' | No more updates will be released!(Maybe)')
        if rtext == 8:
            pygame.display.set_caption( gameName + ' | Interesting fact: There are a million window names here.')
        if rtext == 9:
            pygame.display.set_caption( gameName + ' | Interesting fact: It was developed for less than a month.')
        if rtext == 10:
            pygame.display.set_caption( gameName + ' | Interesting fact: Pictures from GITHUB.')
        if rtext == 11:
            pygame.display.set_caption( gameName + ' | Tip: If you cant beat the game like this, use AirDrop.')
        if rtext == 12:
            pygame.display.set_caption( gameName + ' | The Council: You can turn on Russian!')
        if rtext == 13:
            pygame.display.set_caption( gameName + ' | Tip: Dont play too much!')
        if rtext == 14:
            pygame.display.set_caption( gameName + ' | Thanks for playing the game!')
        if rtext == 15:
            pygame.display.set_caption( gameName + ' | Interesting fact: This is the fifteenth variation of the text.')
        if rtext == 16:
            pygame.display.set_caption( gameName + ' | Interesting fact: Developed by labor!')
        if rtext == 17:
            pygame.display.set_caption( gameName + ' | Tip: If you are bored, play with the cheat panel.')
        if rtext == 18:
            pygame.display.set_caption( gameName + ' | Interesting fact: HardMode is not very complicated!')
        if rtext == 19:
            pygame.display.set_caption( gameName + ' | ...')
        if rtext == 20:
            pygame.display.set_caption( gameName + ' | How long did it take...')
        if rtext == 21:
            pygame.display.set_caption( gameName + ' | The Council: Dont even try to read all the messages from the author!')
        if rtext == 22:
            pygame.display.set_caption(gameName)
        if rtext == 23:
            pygame.display.set_caption( gameName + ' | Tip: также попробуйте поиграть в террарию!')
        if rtext == 24:
            pygame.display.set_caption( gameName + ' | Interesting fact: These messages take up 69 lines of code!')
        if rtext == 25:
            pygame.display.set_caption( gameName + ' | Tip: Try enabling DLC.')
        if rtext == 26:
            pygame.display.set_caption( gameName + ' | Interesting fact: here I learned how to work with Python: https://jetcode.org')
        if rtext == 27:
            pygame.display.set_caption( gameName + ' | Tip: Try putting guns in the later stages of the game!')
        if rtext == 28:
            pygame.display.set_caption( gameName + ' | Interesting fact: dont think that I borrowed the code from the original, because its in Java!')
        if rtext == 29:
            pygame.display.set_caption( gameName + ' | Interesting fact: This is the decoded name of the game.')
        if rtext == 30:
            pygame.display.set_caption('TD-P.RD | Solve it yourself!')
        if rtext == 31:
            pygame.display.set_caption( gameName + ' | Tip: I advise you to read the files: READ ME.txt')
        if rtext == 32:
            pygame.display.set_caption( gameName + ' | Interesting fact: Not everyone will pay attention to this...')
        if rtext == 33:
            pygame.display.set_caption( gameName + ' | Interesting fact: This is not Mindustry...')
        if rtext == 34:
            pygame.display.set_caption( gameName + ' | Interesting fact: This is the penultimate message (or maybe not).')
        if rtext == 35:
            pygame.display.set_caption( gameName + ' | I hope you enjoy this game!')
rtexts()

bg = pygame.sprite.Sprite()
bg = pygame.image.load('bg.jpg')
bg_rect = bg.get_rect()
bg = pygame.transform.scale(bg, BG_SIZE)

bgM = pygame.sprite.Sprite()
rbg = random.randint(1,7)
if rbg == 1:
    bgM = pygame.image.load('font.png')
if rbg == 2:
    bgM = pygame.image.load('fon.jpg')
if rbg == 3:
    bgM = pygame.image.load('fon2.jpg')
if rbg == 4:
    bgM = pygame.image.load('fon3.jpg')
if rbg == 5:
    bgM = pygame.image.load('fon4.jpg')
if rbg == 6:
    bgM = pygame.image.load('fon5.jpg')
if rbg == 7:
    bgM = pygame.image.load('fon6.jpg')
bgM_rect = bgM.get_rect()
bgM = pygame.transform.scale(bgM, BG_SIZE)

comCenter = pygame.sprite.Sprite()
comCenter = pygame.image.load('spawn.png')
comCenter_rect = comCenter.get_rect()
comCenter = pygame.transform.scale(comCenter, (80,80))
comCenter_rect.x = 560
comCenter_rect.y = 300
comCenterHP = 300

full_0 = pygame.image.load('full-0.png')
full_20 = pygame.image.load('full-20.png')
full_40 = pygame.image.load('full-40.png')
full_60 = pygame.image.load('full-60.png')
full_80 = pygame.image.load('full-80.png')
full_100 = pygame.image.load('full-100.png')
full = pygame.sprite.Sprite()
full = full_0
full_rect = full.get_rect()
full = pygame.transform.scale(full, (80,80))
full_rect.x = 560
full_rect.y = 300

go = pygame.sprite.Sprite()
go = pygame.image.load('gameOver.jpg')
go_rect = go.get_rect()
go = pygame.transform.scale(go, BG_SIZE)

es = pygame.sprite.Sprite()
es = pygame.image.load('escape.jpg')
es_rect = es.get_rect()
es = pygame.transform.scale(es, BG_SIZE)

player = pygame.sprite.Sprite()
player = pygame.image.load('player.png')
player_rect = player.get_rect()
player_rect.x = comCenter_rect.x
player_rect.y = comCenter_rect.y

player2 = pygame.sprite.Sprite()
player2 = pygame.image.load('beta.png')
player2_rect = player2.get_rect()
player2_rect.x = comCenter_rect.x
player2_rect.y = comCenter_rect.y

skin = 0

skin1 = pygame.image.load('atrax.png')
skin2 = pygame.image.load('flare.png')
skin3 = pygame.image.load('gamma.png')
skin4 = pygame.image.load('horizon.png')
skin5 = pygame.image.load('nova.png')
skin6 = pygame.image.load('poly.png')
skin7 = pygame.image.load('pulsar.png')
skin8 = pygame.image.load('retusa.png')
skin9 = pygame.image.load('risso.png')
skin10 = pygame.image.load('spiroct.png')
skin11 = pygame.image.load('player.png')
skin12 = pygame.image.load('beta.png')

def randomSkin():
    global player
    skin = random.randint(1, 12)
    if skin == 1:
        player = skin1
    if skin == 2:
        player = skin2
    if skin == 3:
        player = skin3
    if skin == 4:
        player = skin4
    if skin == 5:
        player = skin5
    if skin == 6:
        player = skin6
    if skin == 7:
        player = skin7
    if skin == 8:
        player = skin8
    if skin == 9:
        player = skin9
    if skin == 10:
        player = skin10
    if skin == 11:
        player = skin11
    if skin == 12:
        player = skin12

def randomSkin2():
    global player2
    skin = random.randint(1, 12)
    if skin == 1:
        player2 = skin1
    if skin == 2:
        player2 = skin2
    if skin == 3:
        player2 = skin3
    if skin == 4:
        player2 = skin4
    if skin == 5:
        player2 = skin5
    if skin == 6:
        player2 = skin6
    if skin == 7:
        player2 = skin7
    if skin == 8:
        player2 = skin8
    if skin == 9:
        player2 = skin9
    if skin == 10:
        player2 = skin10
    if skin == 11:
        player2 = skin11
    if skin == 12:
        player2 = skin12

gun = pygame.sprite.Sprite()
gun = pygame.image.load('gun.png')
gun_rect = gun.get_rect()

gun2 = pygame.sprite.Sprite()
gun2 = pygame.image.load('gun2.png')
gun2_rect = gun2.get_rect()

butPlayO = pygame.sprite.Sprite()
butPlayO = pygame.image.load('playOne.jpg')
butPlayO_rect = butPlayO.get_rect()
butPlayO = pygame.transform.scale(butPlayO, (600,600))
butPlayO_rect.x = 0
butPlayO_rect.y = 0

butPlayC = pygame.sprite.Sprite()
butPlayC = pygame.image.load('playCoop.jpg')
butPlayC_rect = butPlayC.get_rect()
butPlayC = pygame.transform.scale(butPlayC, (600,600))
butPlayC_rect.x = 600
butPlayC_rect.y = 0

settingsB = pygame.sprite.Sprite()
settingsB = pygame.image.load('settings.png')
settingsB_rect = settingsB.get_rect()
settingsB = pygame.transform.scale(settingsB, (80,80))
settingsB_rect.x = 0
settingsB_rect.y = 600

infoB = pygame.sprite.Sprite()
infoB = pygame.image.load('info.png')
infoB_rect = infoB.get_rect()
infoB = pygame.transform.scale(infoB, (80,80))
infoB_rect.x = 80
infoB_rect.y = 600

logo = pygame.sprite.Sprite()
logo = pygame.image.load('Logo.png')
logo_rect = logo.get_rect()
logo = pygame.transform.scale(logo, (540,100))
logo_rect.x = 120
logo_rect.y = 589

contr = pygame.sprite.Sprite()
contr = pygame.image.load('control.png')
contr_rect = contr.get_rect()
contr = pygame.transform.scale(contr, (800,340))
contr_rect.x = 0
contr_rect.y = 0

helpBlocks = pygame.sprite.Sprite()
helpBlocks = pygame.image.load('blocks.png')
helpBlocks_rect = helpBlocks.get_rect()
helpBlocks_rect.x = 800
helpBlocks_rect.y = 30

helpEsc = pygame.sprite.Sprite()
helpEsc = pygame.image.load('escHelp.png')
helpEsc_rect = helpEsc.get_rect()
helpEsc_rect.x = 0
helpEsc_rect.y = 285

cheatHelp = pygame.sprite.Sprite()
cheatHelp = pygame.image.load('cheat.png')
cheatHelp_rect = cheatHelp.get_rect()
cheatHelp_rect.x = 900
cheatHelp_rect.y = 0

costHelp = pygame.sprite.Sprite()
costHelp = pygame.image.load('costHelp.png')
costHelp_rect = costHelp.get_rect()
costHelp = pygame.transform.scale(costHelp, (200,640))
costHelp_rect.x = 700
costHelp_rect.y = 0

costDlcHelp = pygame.sprite.Sprite()
costDlcHelp = pygame.image.load('costDlcHelp.png')
costDlcHelp_rect = costDlcHelp.get_rect()
costDlcHelp = pygame.transform.scale(costDlcHelp, (300,440))
costDlcHelp_rect.x = 900
costDlcHelp_rect.y = 0

helpButton = pygame.sprite.Sprite()
helpButton = pygame.image.load('helpBuild.png')
helpButton_rect = helpButton.get_rect()
helpButton_rect.x = 900
helpButton_rect.y = 380

helpButton2 = pygame.sprite.Sprite()
helpButton2 = pygame.image.load('helpDlcBuild.png')
helpButton2_rect = helpButton2.get_rect()
helpButton2_rect.x = 900
helpButton2_rect.y = 0

speedX = 0
speedY = 0

speedX2 = 0
speedY2 = 0

menuOpen = True
settingsOpen = False
infoOpen = False

settingsTimer = 3
infoTimer = 3

gameMode = 'None'

angle = 0
angle2 = 0
angle3 = 0
angle4 = 0

Mouse_x, Mouse_y = pygame.mouse.get_pos()

inGame = pygame.mixer.Sound('game.wav')
inGame2 = pygame.mixer.Sound('game1.wav')
inGame3 = pygame.mixer.Sound('game5.wav')
inGame4 = pygame.mixer.Sound('game4.wav')
inGame5 = pygame.mixer.Sound('game8.wav')
bang = pygame.mixer.Sound('bang.wav')
bigBang = pygame.mixer.Sound('explosionbig.wav')
click = pygame.mixer.Sound('click.wav')
menu = pygame.mixer.Sound('menu.wav')
place = pygame.mixer.Sound('place.wav')
shoot = pygame.mixer.Sound('shoot.wav')
bigShoot = pygame.mixer.Sound('artillery.wav')

copAsteroid = pygame.sprite.Sprite()
copAsteroid = pygame.image.load('copAsteroid.png')
copAsteroid_rect = copAsteroid.get_rect()
copAsteroid = pygame.transform.scale(copAsteroid, (80,80))
copAsteroid_rect.x = 650
copAsteroid_rect.y = 390

Font1 = pygame.font.SysFont("impact", 50)
Font2 = pygame.font.SysFont("impact", 30)
VersionFont = pygame.font.SysFont("sans-serif", 60)

copper = 10

coper = pygame.sprite.Sprite()
coper = pygame.image.load('item-copper.png')
coper_rect = coper.get_rect()
coper = pygame.transform.scale(coper, (50,50))
coper_rect.x = 0
coper_rect.y = 10

ledAsteroid = pygame.sprite.Sprite()
ledAsteroid = pygame.image.load('leadAsteroid.png')
ledAsteroid_rect = ledAsteroid.get_rect()
ledAsteroid = pygame.transform.scale(ledAsteroid, (80,80))
ledAsteroid_rect.x = 350
ledAsteroid_rect.y = 190

led = 0

lead = pygame.sprite.Sprite()
lead = pygame.image.load('item-lead.png')
lead_rect = lead.get_rect()
lead = pygame.transform.scale(lead, (50,50))
lead_rect.x = 0
lead_rect.y = 60

thoriumAsteroid = pygame.sprite.Sprite()
thoriumAsteroid = pygame.image.load('thoriumAsteroid.png')
thoriumAsteroid_rect = thoriumAsteroid.get_rect()
thoriumAsteroid = pygame.transform.scale(thoriumAsteroid, (80,80))
thoriumAsteroid_rect.x = 150
thoriumAsteroid_rect.y = 600

thorium = 0

thory = pygame.sprite.Sprite()
thory = pygame.image.load('item-thorium.png')
thory_rect = thory.get_rect()
thory = pygame.transform.scale(thory, (50,50))
thory_rect.x = 0
thory_rect.y = 110

graphite = 0

grafite = pygame.sprite.Sprite()
grafite = pygame.image.load('item-graphite.png')
grafite_rect = grafite.get_rect()
grafite = pygame.transform.scale(grafite, (50,50))
grafite_rect.x = 0
grafite_rect.y = 160

hlak = 0

shlak = pygame.sprite.Sprite()
shlak = pygame.image.load('shlak.png')
shlak_rect = shlak.get_rect()
shlak = pygame.transform.scale(shlak, (50,50))
shlak_rect.x = 0
shlak_rect.y = 600

water = 0

vater = pygame.sprite.Sprite()
vater = pygame.image.load('water.png')
vater_rect = vater.get_rect()
vater = pygame.transform.scale(vater, (50,50))
vater_rect.x = 0
vater_rect.y = 550

oil = 0

oils = pygame.sprite.Sprite()
oils = pygame.image.load('oil.png')
oils_rect = oils.get_rect()
oils = pygame.transform.scale(oils, (50,50))
oils_rect.x = 0
oils_rect.y = 500

customM = pygame.sprite.Sprite()
customM = pygame.image.load('cursor.png')
customM_rect = customM.get_rect()

drill = pygame.sprite.Sprite()
drill = pygame.image.load('mechanical-drill.png')
drill = pygame.transform.scale(drill, (80,80))
drill_rect = drill.get_rect()
drill_rect.x = 950
drill_rect.y = 390

rotator = pygame.sprite.Sprite()
rotator = pygame.image.load('mechanical-drill-rotator.png')
rotator_rect = rotator.get_rect()
rotator_rect.x = drill_rect.x + 8
rotator_rect.y = drill_rect.y + 8
rotAngle = 0

createTimer = 10

lastCursor = 1

rubble = pygame.sprite.Group()
towerSpawns = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bigBullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies2 = pygame.sprite.Group()
enemies3 = pygame.sprite.Group()
enemies4 = pygame.sprite.Group()
enemyBullets = pygame.sprite.Group()
enemyBullets2 = pygame.sprite.Group()
healBullets = pygame.sprite.Group()
blocks = pygame.sprite.Group()

Mouse_x, Mouse_y = pygame.mouse.get_pos()

drillTimer = 5

drillSpeed = 30

rotSpeed = 0

attackTimerPlayer1 = 0
attackTimerPlayer2 = 0

destroyedEnemies = 0

file = open("GameStory/Game.txt", "w")
file.write("Концовка еще не получена...")
file.close()   

file = open("GameStory/Money.dat", "r")
b = file.read()
if b.isdigit() == True:
    money = int(b)
else:
    print('FileError 0.1 Пожалуйста используйте цифры в файле money')
    running = False
file.close()   

secretBool = True

file = open("GameStory/doNotChange.dat", "r")
c = file.read()
testC = c
if testC == 'False':
    secretBool = True
if testC == 'True':
    secretBool = False
if not testC == 'True' and not testC == 'False':
    print('FileError 0.2 Пожалуйста не меняйте файл doNotChange, поставьте значение False или True')
    running = False
file.close()   

coin = pygame.sprite.Sprite()
coin = pygame.image.load('coin.png')
coin_rect = coin.get_rect()
coin = pygame.transform.scale(coin, (50,50))
coin_rect.x = 370
coin_rect.y = 190

wave = 0
waveTimer = 160

waweTimerSmall = 0

menu.play()

canEscape = False

hardMode = False
hardModeTimer = 0

hardModeButton = pygame.sprite.Sprite()
if hardMode == False:
    hardModeButton = pygame.image.load('hardModeOff.png')
else:
    hardModeButton = pygame.image.load('hardModeOn.png')
hardModeButton = pygame.transform.scale(hardModeButton, (80,80))
hardModeButton_rect = hardModeButton.get_rect()
hardModeButton_rect.x = 10
hardModeButton_rect.y = 10

unlMode = False
unlModeTimer = 0

unlimitedResButton = pygame.sprite.Sprite()
if unlMode == False:
    unlimitedResButton = pygame.image.load('unlimitedResOff.png')
else:
    unlimitedResButton = pygame.image.load('unlimitedResOn.png')
unlimitedResButton = pygame.transform.scale(unlimitedResButton, (80,80))
unlimitedResButton_rect = unlimitedResButton.get_rect()
unlimitedResButton_rect.x = 10
unlimitedResButton_rect.y = 100

musicPlay = True
musicTimer = 0

musicButton = pygame.sprite.Sprite()
if musicPlay == True:
    musicButton = pygame.image.load('soundOn.png')
else:
    musicButton = pygame.image.load('soundOff.png')
musicButton = pygame.transform.scale(musicButton, (80,80))
musicButton_rect = musicButton.get_rect()
musicButton_rect.x = 10
musicButton_rect.y = 190

nextTimer = 0

nextButton = pygame.sprite.Sprite()
nextButton = pygame.image.load('next.png')
nextButton = pygame.transform.scale(nextButton, (80,80))
nextButton_rect = nextButton.get_rect()
nextButton_rect.x = 100
nextButton_rect.y = 190

nextEquipTimer = 0

nextEquip = pygame.sprite.Sprite()
nextEquip = pygame.image.load('nextEquipment.png')
nextEquip = pygame.transform.scale(nextEquip, (80,80))
nextEquip_rect = nextEquip.get_rect()
nextEquip_rect.x = 280
nextEquip_rect.y = 10

doEnemiesSpawn = True
enemiesSpawnTimer = 0

enemiesSpawn = pygame.sprite.Sprite()
if doEnemiesSpawn == True:
    enemiesSpawn = pygame.image.load('withEnemyOn.png')
else:
    enemiesSpawn = pygame.image.load('withEnemyOff.png')
enemiesSpawn = pygame.transform.scale(enemiesSpawn, (80,80))
enemiesSpawn_rect = enemiesSpawn.get_rect()
enemiesSpawn_rect.x = 100
enemiesSpawn_rect.y = 10

doUnlHp = False
unlHpTimer = 0

unlimitedHpButton = pygame.sprite.Sprite()
if doUnlHp == False:
    unlimitedHpButton = pygame.image.load('unlimitedHpOff.png')
else:
    unlimitedHpButton = pygame.image.load('unlimitedHpOn.png')
unlimitedHpButton = pygame.transform.scale(unlimitedHpButton, (80,80))
unlimitedHpButton_rect = unlimitedHpButton.get_rect()
unlimitedHpButton_rect.x = 100
unlimitedHpButton_rect.y = 100

airdrops = False
airdropTimer = 0

airdropButton = pygame.sprite.Sprite()
if airdrops == False:
    airdropButton = pygame.image.load('airdropsOff.png')
else:
    airdropButton = pygame.image.load('airdropsOn.png')
airdropButton = pygame.transform.scale(airdropButton, (80,80))
airdropButton_rect = airdropButton.get_rect()
airdropButton_rect.x = 190
airdropButton_rect.y = 100

doCheatWork = False
cheatTimer = 0

cheatButton = pygame.sprite.Sprite()
if doCheatWork == False:
    cheatButton = pygame.image.load('cheatModOff.png')
else:
    cheatButton = pygame.image.load('cheatModOn.png')
cheatButton = pygame.transform.scale(cheatButton, (80,80))
cheatButton_rect = cheatButton.get_rect()
cheatButton_rect.x = 190
cheatButton_rect.y = 10

randSkins = False
randTimer = 0

randButton = pygame.sprite.Sprite()
if randSkins == False:  
    randButton = pygame.image.load('randomSkinOff.png')
else:
    randButton = pygame.image.load('randomSkinOn.png')
randButton = pygame.transform.scale(randButton, (80,80))
randButton_rect = randButton.get_rect()
randButton_rect.x = 190
randButton_rect.y = 190

testSee = False
testTimer = 0

testSeeButton = pygame.sprite.Sprite()
if testSee == False:
    testSeeButton = pygame.image.load('testSettingsOff.png')
else:
    testSeeButton = pygame.image.load('testSettingsOn.png')
testSeeButton = pygame.transform.scale(testSeeButton, (200,100))
testSeeButton_rect = testSeeButton.get_rect()
testSeeButton_rect.x = 950
testSeeButton_rect.y = 520

equipSee = pygame.sprite.Sprite()
equipSee = pygame.image.load('equipmentBullet.png')
equipSee = pygame.transform.scale(equipSee, (100,100))
equipSee_rect = equipSee.get_rect()
equipSee_rect.x = 350
equipSee_rect.y = 0

equipSee2 = pygame.sprite.Sprite()
equipSee2 = pygame.image.load('equipmentBullet2.png')
equipSee2 = pygame.transform.scale(equipSee2, (100,100))
equipSee2_rect = equipSee2.get_rect()
equipSee2_rect.x = 450
equipSee2_rect.y = 0

tutorialTimer = 0
tutorialWork = False

tutorialButton = pygame.sprite.Sprite()
if tutorialWork == False:
    tutorialButton = pygame.image.load('tutorialOff.png')
else:
    tutorialButton = pygame.image.load('tutorialOn.png')
tutorialButton = pygame.transform.scale(tutorialButton, (80,80))
tutorialButton_rect = tutorialButton.get_rect()
tutorialButton_rect.x = 600
tutorialButton_rect.y = 600

dlcTimer = 0
dlcWork = False

dlc = pygame.sprite.Sprite()
if dlcWork == False:
    dlc = pygame.image.load('dlcOff.png')
else:
    dlc = pygame.image.load('dlcOn.png')
dlc = pygame.transform.scale(dlc, (80,80))
dlc_rect = dlc.get_rect()
dlc_rect.x = 370
dlc_rect.y = 100

textureTimer = 0

texture = pygame.sprite.Sprite()
texture = pygame.image.load('openTextures.png')
texture = pygame.transform.scale(texture, (80,80))
texture_rect = texture.get_rect()
texture_rect.x = 460
texture_rect.y = 100

fogTimer = 0
fogWork = False

fogButton = pygame.sprite.Sprite()
if fogWork == False:
    fogButton = pygame.image.load('fogOff.png')
else:
    fogButton = pygame.image.load('fogOn.png')
fogButton = pygame.transform.scale(fogButton, (80,80))
fogButton_rect = fogButton.get_rect()
fogButton_rect.x = 280
fogButton_rect.y = 190

langTimer = 0

langButton = pygame.sprite.Sprite()
if langRus == False:
    langButton = pygame.image.load('engLang.png')
else:
    langButton = pygame.image.load('rusLang.png')
langButton = pygame.transform.scale(langButton, (80,80))
langButton_rect = langButton.get_rect()
langButton_rect.x = 550
langButton_rect.y = 100

dialog = pygame.image.load('dialog1.png')
dialog_rect = dialog.get_rect()
dialog_rect.x = 0
dialog_rect.y = 380

shopTimer = 0
storeActivated = False

shop = pygame.sprite.Sprite()
shop = pygame.image.load('shopOff.png')
shop = pygame.transform.scale(shop, (80,80))
shop_rect = shop.get_rect()
shop_rect.x = 960
shop_rect.y = 0

dialogNumber = 1
dialogTimer = 0
dialogWallStay = False

dmgEnemy = 10
dmgEnemy3 = 1
dmgEnemy4 = 1
dmgEnemy5 = 5
dmgDlcEnemy = 1
dmgPlayer = 1
dmgPlayer2 = 0.1

destroyAll = False

equipment = random.randint(1,3)

if equipment == 1:
    equipSee = pygame.image.load('equipmentBullet.png')
    equipSee2 = pygame.image.load('equipmentBigBullet2.png')
if equipment == 2:
    equipSee = pygame.image.load('equipmentHealBullet.png')
    equipSee2 = pygame.image.load('equipmentBullet2.png')
if equipment == 3:
    equipSee = pygame.image.load('equipmentBigBullet.png')
    equipSee2 = pygame.image.load('equipmentHealBullet2.png')

i = 0
haveMoney = False

slot1Timer = 0
slot1 = pygame.sprite.Sprite()
slot1 = pygame.image.load('slotSellCopper.png')
slot1 = pygame.transform.scale(slot1, (96,96))
slot1_rect = slot1.get_rect()
slot1_rect.x = 340
slot1_rect.y = 0

slot2Timer = 0
slot2 = pygame.sprite.Sprite()
slot2 = pygame.image.load('slotSellLead.png')
slot2 = pygame.transform.scale(slot2, (96,96))
slot2_rect = slot2.get_rect()
slot2_rect.x = 446
slot2_rect.y = 0

slot3Timer = 0
slot3 = pygame.sprite.Sprite()
slot3 = pygame.image.load('slotSellThorium.png')
slot3 = pygame.transform.scale(slot3, (96,96))
slot3_rect = slot3.get_rect()
slot3_rect.x = 552
slot3_rect.y = 0

slot4Timer = 0
slot4 = pygame.sprite.Sprite()
slot4 = pygame.image.load('slotSellGraphite.png')
slot4 = pygame.transform.scale(slot4, (96,96))
slot4_rect = slot4.get_rect()
slot4_rect.x = 658
slot4_rect.y = 0

bulletImg = pygame.image.load('bullet.png')

mouseCanClick = False

buttonLose = pygame.sprite.Sprite()
buttonLose = pygame.image.load('buttonLose.png')
buttonLose = pygame.transform.scale(buttonLose, (320,150))
buttonLose_rect = buttonLose.get_rect()
buttonLose_rect.x = 440
buttonLose_rect.y = 100

buttonWin = pygame.sprite.Sprite()
buttonWin = pygame.image.load('buttonWin.png')
buttonWin = pygame.transform.scale(buttonWin, (320,150))
buttonWin_rect = buttonWin.get_rect()
buttonWin_rect.x = 440
buttonWin_rect.y = 100

buttonRestart = pygame.sprite.Sprite()
buttonRestart = pygame.image.load('buttonRestart.png')
buttonRestart = pygame.transform.scale(buttonRestart, (320,150))
buttonRestart_rect = buttonRestart.get_rect()
buttonRestart_rect.x = 440
buttonRestart_rect.y = 260

class Bullet(pygame.sprite.Sprite):
    def __init__ (self, an2, an, spRect):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletImg
        self.rect = self.image.get_rect()
        self.rect.center = spRect.center
        if an2 == 0 or an2 == 180:
            self.rect.x = spRect.x - 7
            self.rect.y = spRect.y
        if an2 == 90 or an2 == -90:
            self.rect.x = spRect.x
            self.rect.y = spRect.y + 8
        self.angle = an + an2
        self.add(bullets)
        shoot.play()
    def update(self):
        self.rect.x -= 8 * math.sin(self.angle * (math.pi / 180))
        self.rect.y -= 8 * math.cos(self.angle * (math.pi / 180))
        if self.rect.x < -60 or self.rect.y < -60 or self.rect.x > 1250 or self.rect.y > 650:
            self.kill()
        if destroyAll == True:
            self.kill()

bulletImg2 = pygame.image.load('bullet2.png')

class Bullet2(pygame.sprite.Sprite):
    def __init__ (self, an2, an, spRect, towr5):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletImg2
        self.rect = self.image.get_rect()
        self.rect.center = spRect.center
        if an2 == 0 or an2 == 180:
            if towr5 == False:
                self.rect.x = spRect.x - 17
                self.rect.y = spRect.y
            else:
                self.rect.x = spRect.x + 36
                self.rect.y = spRect.y
        if an2 == 90 or an2 == -90:
            if towr5 == False:
                self.rect.x = spRect.x
                self.rect.y = spRect.y
        self.angle = an + an2
        self.add(bigBullets)
        bigShoot.play()
        self.randomMove = random.randint(0,10)
    def update(self):
        if self.randomMove == 1:
            self.rect.x -=2
        if self.randomMove == 2:
            self.rect.x +=2
        if self.randomMove == 3:
            self.rect.y +=2
        if self.randomMove == 4:
            self.rect.y -=2
        self.rect.x -= 8 * math.sin(self.angle * (math.pi / 180))
        self.rect.y -= 8 * math.cos(self.angle * (math.pi / 180))
        if self.rect.x < -60 or self.rect.y < -60 or self.rect.x > 1250 or self.rect.y > 650:
            self.kill() 
        if destroyAll == True:
            self.kill()

bulletImg3 = pygame.image.load('healBullet.png')

class HealBullet(pygame.sprite.Sprite):
    def __init__ (self, an2, an, spRect):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletImg3
        self.rect = self.image.get_rect()
        self.rect.center = spRect.center
        if an2 == 0:
            self.rect.x = spRect.x - 13
            self.rect.y = spRect.y - 31
        if an2 == 180:
            self.rect.x = spRect.x - 13
            self.rect.y = spRect.y + 31
        if an2 == 90: 
            self.rect.x = spRect.x - 30
            self.rect.y = spRect.y
        if an2 == -90:
            self.rect.x = spRect.x + 30
            self.rect.y = spRect.y
        self.angle = an + an2
        self.add(healBullets)
        shoot.play()
    def update(self):
        self.rect.x -= 8 * math.sin(self.angle * (math.pi / 180))
        self.rect.y -= 8 * math.cos(self.angle * (math.pi / 180))
        if self.rect.x < -60 or self.rect.y < -60 or self.rect.x > 1250 or self.rect.y > 650:
            self.kill()
        if destroyAll == True:
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__ (self, an2, an, spRect):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletImg
        self.rect = self.image.get_rect()
        self.rect.center = spRect.center
        if an2 == 0 or an2 == 180:
            self.rect.x = spRect.x - 7
            self.rect.y = spRect.y
        if an2 == 90 or an2 == -90:
            self.rect.x = spRect.x
            self.rect.y = spRect.y + 8
        self.angle = an + an2
        self.add(enemyBullets)
        shoot.play()
    def update(self):
        global comCenterHP
        if self.rect.x > 559 and self.rect.x < 641:
            if self.rect.y > 270 and self.rect.y < 380:
                if doUnlHp == False:
                    comCenterHP -= dmgEnemy4
                self.kill()
        self.rect.x -= 8 * math.sin(self.angle * (math.pi / 180))
        self.rect.y -= 8 * math.cos(self.angle * (math.pi / 180))
        if self.rect.x < -60 or self.rect.y < -60 or self.rect.x > 1250 or self.rect.y > 650:
            self.kill()
        if destroyAll == True:
            self.kill()

class EnemyBullet2(pygame.sprite.Sprite):
    def __init__ (self, an2, an, spRect):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletImg2
        self.rect = self.image.get_rect()
        self.rect.center = spRect.center
        if an2 == 0 or an2 == 180:
            self.rect.x = spRect.x + 30
            self.rect.y = spRect.y
        if an2 == 90 or an2 == -90:
            self.rect.x = spRect.x + 30
            self.rect.y = spRect.y
        self.angle = an + an2
        self.add(enemyBullets2)
        bigShoot.play()
    def update(self):
        self.rect.x -= 8 * math.sin(self.angle * (math.pi / 180))
        self.rect.y -= 8 * math.cos(self.angle * (math.pi / 180))
        if self.rect.x < -60 or self.rect.y < -60 or self.rect.x > 1250 or self.rect.y > 650:
            self.kill()
        if destroyAll == True:
            self.kill()

rubble_1_0 = pygame.image.load('rubble-1-0.png')
rubble_1_1 = pygame.image.load('rubble-1-1.png')
rubble_2_0 = pygame.image.load('rubble-2-0.png')
rubble_2_1 = pygame.image.load('rubble-2-1.png')
rubble_3_0 = pygame.image.load('rubble-3-0.png')
rubble_4_0 = pygame.image.load('rubble-4-0.png')
rubble_5_0 = pygame.image.load('rubble-5-0.png')
rubble_6_0 = pygame.image.load('rubble-6-0.png')
rubble_7_0 = pygame.image.load('rubble-7-0.png')
rubble_8_0 = pygame.image.load('rubble-8-0.png')

class Rubble(pygame.sprite.Sprite):
    def __init__ (self, size, placeX, placeY, group):
        pygame.sprite.Sprite.__init__(self)
        if size == 1:
            self.rand = random.randint(1,2)
            if self.rand == 1:
                self.image = rubble_1_0
            if self.rand == 2:
                self.image = rubble_1_1
            self.rect = self.image.get_rect()
            self.rect.center = self.rect.center
            self.cordX = placeX
            self.cordY = placeY
            self.rect.x = self.cordX - 15
            self.rect.y = self.cordY - 15
        if size == 2:
            self.rand = random.randint(1,2)
            if self.rand == 1:
                self.image = rubble_2_0
            if self.rand == 2:
                self.image = rubble_2_1
            self.rect = self.image.get_rect()
            self.rect.center = self.rect.center
            self.cordX = placeX
            self.cordY = placeY
            self.rect.x = self.cordX
            self.rect.y = self.cordY
        if size == 3:
            self.image = rubble_3_0
            self.rect = self.image.get_rect()
            self.rect.center = self.rect.center
            self.cordX = placeX
            self.cordY = placeY
            self.rect.x = self.cordX
            self.rect.y = self.cordY
        if size == 4:
            self.image = rubble_4_0
            self.rect = self.image.get_rect()
            self.rect.center = self.rect.center
            self.cordX = placeX
            self.cordY = placeY
            self.rect.x = self.cordX
            self.rect.y = self.cordY
        if size == 5:
            self.image = rubble_5_0
            self.rect = self.image.get_rect()
            self.rect.center = self.rect.center
            self.cordX = placeX
            self.cordY = placeY
            self.rect.x = self.cordX
            self.rect.y = self.cordY
        if size == 6:
            self.image = rubble_6_0
            self.rect = self.image.get_rect()
            self.rect.center = self.rect.center
            self.cordX = placeX
            self.cordY = placeY
            self.rect.x = self.cordX
            self.rect.y = self.cordY
        if size == 7:
            self.image = rubble_7_0
            self.rect = self.image.get_rect()
            self.rect.center = self.rect.center
            self.cordX = placeX
            self.cordY = placeY
            self.rect.x = self.cordX
            self.rect.y = self.cordY
        if size == 8:
            self.image = rubble_8_0
            self.rect = self.image.get_rect()
            self.rect.center = self.rect.center
            self.cordX = placeX
            self.cordY = placeY
            self.rect.x = self.cordX
            self.rect.y = self.cordY
        self.timer = 1000
        self.add(group)       
    def update(self):
        self.timer -= 0.1
        if self.timer < 1:
            self.kill()
        if destroyAll == True:
            self.kill()

imgWallDmg = pygame.image.load('wall.png')
imgWallDmg2 = pygame.image.load('wall2.png')
imgWallDmg3 = pygame.image.load('wall3.png')

class Walls(pygame.sprite.Sprite):
    def __init__ (self, group):
        global dialogWallStay
        dialogWallStay = True
        pygame.sprite.Sprite.__init__(self)
        self.image = imgWallDmg
        self.hp = 30
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.cordX = Mouse_x
        self.cordY = Mouse_y
        self.rect.x = self.cordX
        self.rect.y = self.cordY
        self.add(group)       
        place.play()
    def update(self):
        if self.hp > 20:
            self.image = imgWallDmg
        if self.hp > 10 and self.hp < 21:
            self.image = imgWallDmg2
        if self.hp < 11:
            self.image = imgWallDmg3
        if pygame.sprite.spritecollide(self, enemies, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 30:
                self.hp += 1
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(1, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

mineImg = pygame.image.load('shock-mine.png')

class Mine(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = mineImg
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.hp = 1
        self.cordX = Mouse_x
        self.cordY = Mouse_y
        self.rect.x = self.cordX
        self.rect.y = self.cordY
        self.add(group)       
        place.play()
    def update(self):
        if pygame.sprite.spritecollide(self, enemies, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, enemies2, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, enemies4, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy
            bang.play()
        if self.hp < 1:
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

randomFog = random.randint(1,3)
fog = pygame.sprite.Sprite()
if randomFog == 1:
    fog = pygame.image.load('noiseAlpha.png')
if randomFog == 2:
    fog = pygame.image.load('clouds.png')
if randomFog == 3:
    fog = pygame.image.load('fog.png')
fog = pygame.transform.scale(fog, (1200,680))
fog_rect = fog.get_rect()
fog_rect.x = 1200
fog_rect.y = 0    

fog2 = pygame.sprite.Sprite()
if randomFog == 1:
    fog2 = pygame.image.load('noiseAlpha.png')
if randomFog == 2:
    fog2 = pygame.image.load('clouds.png')
if randomFog == 3:
    fog2 = pygame.image.load('fog.png')
fog2 = pygame.transform.scale(fog2, (1200,680))
fog2_rect = fog2.get_rect()
fog2_rect.x = 2400
fog2_rect.y = 0   

imgbigWallDmg = pygame.image.load('wall-large.png')
imgbigWallDmg2 = pygame.image.load('wall-large2.png')
imgbigWallDmg3 = pygame.image.load('wall-large3.png')

class BigWalls(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = imgbigWallDmg
        self.hp = 60
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)       
        place.play()
    def update(self):
        if self.hp > 40:
            self.image = imgbigWallDmg
        if self.hp > 20 and self.hp < 41:
            self.image = imgbigWallDmg2
        if self.hp < 21:
            self.image = imgbigWallDmg3
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 60:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(2, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

imgForceProjectorDmg = pygame.image.load('force-projector.png')
imgForceProjectorDmg2 = pygame.image.load('force-projector2.png')
imgForceProjectorDmg3 = pygame.image.load('force-projector3.png')

class ForceProjector(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = imgForceProjectorDmg
        self.hp = 60
        self.timer = 1000
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)       
        place.play()
    def update(self):
        if self.timer < 1:
            self.hp += 1
            self.timer = 300
        self.timer -= 1
        if self.hp > 40:
            self.image = imgForceProjectorDmg
        if self.hp > 20 and self.hp < 41:
            self.image = imgForceProjectorDmg2
        if self.hp < 21:
            self.image = imgForceProjectorDmg3
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 60:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(3, self.rect.x + 100, self.rect.y + 100, rubble)
        if destroyAll == True:
            self.kill()

imgPressDmg = pygame.image.load('graphite-press.png')
imgPressDmg2 = pygame.image.load('graphite-press2.png')
imgPressDmg3 = pygame.image.load('graphite-press3.png')

class Press(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = imgPressDmg
        self.hp = 30
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.timer = 10
        self.add(group)       
        place.play()
    def update(self):
        global clicked
        global copper
        global led
        global thorium
        global graphite
        if self.hp > 20:
            self.image = imgPressDmg
        if self.hp > 10 and self.hp < 21:
            self.image = imgPressDmg2
        if self.hp < 11:
            self.image = imgPressDmg3
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, True):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 30:
                self.hp += 1
        self.timer -= 1
        if Mouse_x > self.rect.x and Mouse_x < self.rect.x + 60:
            if Mouse_y > self.rect.y and Mouse_y < self.rect.y + 60:
                if mouseClick == True and clicked == 1 and self.timer < 1: 
                    if hardMode == True:
                        if copper > 20 or copper == 20:
                            if led > 20 or led == 20:
                                if thorium > 20 or thorium == 20:
                                    graphite += 1
                                    copper -= 20
                                    thorium -= 20
                                    led -= 20
                                    self.timer = 10
                    else:
                        if copper > 10 or copper == 10:
                            if led > 10 or led == 10:
                                graphite += 1
                                copper -= 10
                                led -= 10
                                self.timer = 10
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(2, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

cheatWallImg = pygame.image.load('thruster.png')

class cheatWalls(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = cheatWallImg
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)       
        place.play()
    def update(self):
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
        if pygame.sprite.spritecollide(self, enemies3, False):
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            bang.play()
        if destroyAll == True:
            self.kill()

dmgBigToriumWallImg = pygame.image.load('thorium-wall-large.png')
dmgBigToriumWallImg2 = pygame.image.load('thorium-wall-large2.png')
dmgBigToriumWallImg3 = pygame.image.load('thorium-wall-large3.png')

class BigTorium(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = dmgBigToriumWallImg
        self.hp = 120
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)       
        place.play()
    def update(self):
        if self.hp > 80:
            self.image = dmgBigToriumWallImg
        if self.hp > 40 and self.hp < 81:
            self.image = dmgBigToriumWallImg2
        if self.hp < 41:
            self.image = dmgBigToriumWallImg3
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 120:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(2, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

ExtraDrillimgDmg = pygame.image.load('thermal-generator.png')
ExtraDrillimgDmg2 = pygame.image.load('thermal-generator2.png')
ExtraDrillimgDmg3 = pygame.image.load('thermal-generator3.png')

class ExtraDrill(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = ExtraDrillimgDmg
        self.hp = 60
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.timer = 0
        self.add(group)       
        place.play()
    def update(self):
        global copper
        global led
        global thorium
        global hlak
        global water
        if self.timer == 0:
            if dlcWork == True:
                if copper < 99999:
                    copper += 0.1 * water
                if led < 99999:
                    led += 0.1 * water
                if thorium < 99999:
                    thorium += 0.1 * water
                if hlak < 999:
                    hlak += 1 * water
                if water < 100:
                    water += 0.001
            else:
                if copper < 99999:
                    copper += 0.1
                if led < 99999:
                    led += 0.1
                if thorium < 99999:
                    thorium += 0.1
            self.timer = 15
        if self.timer > 0:
            self.timer -= 1
        else:
            self.timer = 0
        if self.hp > 40:
            self.image = ExtraDrillimgDmg
        if self.hp > 20 and self.hp < 41:
            self.image = ExtraDrillimgDmg2
        if self.hp < 21:
            self.image = ExtraDrillimgDmg3
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 60:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(2, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

resGeneratorimageDmg = pygame.image.load('resourse-generator.png')
resGeneratorimageDmg2 = pygame.image.load('resourse-generator2.png')
resGeneratorimageDmg3 = pygame.image.load('resourse-generator3.png')

class ResGenerator(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = resGeneratorimageDmg
        self.hp = 60
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.timer = 0
        self.add(group)       
        place.play()
    def update(self):
        global copper
        global led
        global thorium
        global hlak
        global water
        if self.timer == 0:
            if copper < 99999:
                copper += 1 * water
            if led < 99999:
                led += 1 * water
            if thorium < 99999:
                thorium += 1 * water
            if hlak < 999:
                hlak += 2 * water
            if water < 100:
                water += 0.01
            self.timer = 10
        if self.timer > 0:
            self.timer -= 1
        else:
            self.timer = 0
        if self.hp > 40:
            self.image = resGeneratorimageDmg
        if self.hp > 20 and self.hp < 41:
            self.image = resGeneratorimageDmg2
        if self.hp < 21:
            self.image = resGeneratorimageDmg3
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 60:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(8, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

extractorDmgImg = pygame.image.load('oil-extractor.png')
extractorDmgImg2 = pygame.image.load('oil-extractor2.png')
extractorDmgImg3 = pygame.image.load('oil-extractor3.png')

class Extractor(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = extractorDmgImg
        self.hp = 30
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.timer = 0
        self.add(group)       
        place.play()
    def update(self):
        global oil
        global water
        if water > 0.010 and self.timer < 1:
            if oil < 9999:
                oil += 0.1
                water -= 0.010
            self.timer = 15
        if self.timer > 0:
            self.timer -= 1
        else:
            self.timer = 0
        if self.hp > 20:
            self.image = extractorDmgImg
        if self.hp > 10 and self.hp < 21:
            self.image = extractorDmgImg2
        if self.hp < 11:
            self.image = extractorDmgImg3
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 30:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(3, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

waterExtractorDmgImg = pygame.image.load('water-extractor.png')
waterExtractorDmgImg2 = pygame.image.load('water-extractor2.png')

class WaterExtractor(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = waterExtractorDmgImg
        self.hp = 10
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.timer = 0
        self.add(group)       
        place.play()
    def update(self):
        global water
        if self.timer < 1:
            if water < 99.9:
                water += 0.1
            self.timer = 15
        if self.timer > 0:
            self.timer -= 1
        else:
            self.timer = 0
        if self.hp > 5:
            self.image = waterExtractorDmgImg
        if self.hp < 6:
            self.image = waterExtractorDmgImg2
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 30:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(2, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

mixerDmgImg = pygame.image.load('blast-mixer.png')
mixerDmgImg2 = pygame.image.load('blast-mixer2.png')

class Mixer(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = mixerDmgImg
        self.hp = 10
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.timer = 0
        self.add(group)       
        place.play()
    def update(self):
        global hlak
        if self.timer < 1:
            if hlak < 999:
                hlak += 0.1
            self.timer = 15
        if self.timer > 0:
            self.timer -= 1
        else:
            self.timer = 0
        if self.hp > 5:
            self.image = mixerDmgImg
        if self.hp < 6:
            self.image = mixerDmgImg2
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 30:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(2, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

enemyImg = pygame.image.load('crawler.png')

class Enemy(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemyImg
        self.hp = 20
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.angle = 0
        self.spawn = random.randint(1,2)   
        if self.spawn == 1:
            self.rect.x = 570
            self.rect.y = 0
            self.angle = 180
        if self.spawn == 2:
            self.rect.x = 570
            self.rect.y = 640
            self.angle = 0
        self.add(group)
    def update(self):
        global destroyedEnemies
        global comCenterHP
        self.rect.x -= 1 * math.sin(self.angle * (math.pi / 180))
        self.rect.y -= 1 * math.cos(self.angle * (math.pi / 180))
        if pygame.sprite.spritecollide(self, bullets, True):
            self.hp -= dmgPlayer
        if pygame.sprite.spritecollide(self, bigBullets, False):
            self.hp -= dmgPlayer2
        if self.rect.x > 559 and self.rect.x < 641:
            if self.rect.y > 270 and self.rect.y < 380:
                if doUnlHp == False:
                    comCenterHP -= 10
                bang.play()
                self.kill()
        if self.hp < 1:
            destroyedEnemies += 1
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

enemyImg2 = pygame.image.load('mace.png')

class Enemy2(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemyImg2
        if hardMode == False:
            self.hp = 5
        else:
            self.hp = 10
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.spawn = random.randint(1,2)   
        if self.spawn == 1:
            self.rect.x = 0
            self.rect.y = 300
            self.angle = 90
        if self.spawn == 2:
            self.rect.x = 1100
            self.rect.y = 300
            self.angle = -90
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.add(group)
    def update(self):
        global destroyedEnemies
        global comCenterHP
        self.rect.x += 1 * math.sin(self.angle * (math.pi / 180))
        self.rect.y += 1 * math.cos(self.angle * (math.pi / 180))
        if pygame.sprite.spritecollide(self, bullets, True):
            self.hp -= dmgPlayer
        if pygame.sprite.spritecollide(self, bigBullets, False):
            self.hp -= dmgPlayer2
        if self.rect.x > 509 and self.rect.x < 641:
            if self.rect.y > 270 and self.rect.y < 380:
                if doUnlHp == False:
                    if hardMode == False:
                        comCenterHP -= 50
                    else:
                        comCenterHP -= 100
                bang.play()
                self.kill()
        if self.hp < 1:
            destroyedEnemies += 1
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

enemyImg3 = pygame.image.load('zenith.png')

class Enemy3(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        global dmgEnemy3
        self.image = enemyImg3
        if hardMode == False:
            dmgEnemy3 = 1
        else:
            dmgEnemy3 = 5
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.spawn = random.randint(1,2)  
        if hardMode == False: 
            self.hp = 3
        else:
            self.hp = 10
        if self.spawn == 1:
            self.rect.x = 0
            self.rect.y = 300
            self.angle = -90
        if self.spawn == 2:
            self.rect.x = 1100
            self.rect.y = 300
            self.angle = 90
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.add(group)
    def update(self):
        global destroyedEnemies
        self.rect.x -= 1 * math.sin(self.angle * (math.pi / 180))
        self.rect.y -= 1 * math.cos(self.angle * (math.pi / 180))
        if pygame.sprite.spritecollide(self, bullets, True):
            self.hp -= dmgPlayer
        if pygame.sprite.spritecollide(self, bigBullets, False):
            self.hp -= dmgPlayer2
        if self.rect.x > 1400 or self.rect.x < -200:
            bang.play()
            self.kill()
        if self.hp < 1:
            destroyedEnemies += 1
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

enemyImg4 = pygame.image.load('alpha.png')

class Enemy4(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        global dmgEnemy4
        self.image = enemyImg4
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.spawn = random.randint(1,2)   
        if hardMode == True:
            self.hp = 10
        else:
            self.hp = 3
        self.timer = 0
        if self.spawn == 1:
            self.rect.x = 600
            self.rect.y = 30
            self.angle = 180
        if self.spawn == 2:
            self.rect.x = 600
            self.rect.y = 590
            self.angle = 0
        if hardMode == True:
            dmgEnemy4 = 5
        else:
            dmgEnemy4 = 1
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.add(group)
    def update(self):
        global destroyedEnemies
        if pygame.sprite.spritecollide(self, bullets, True):
            self.hp -= dmgPlayer
        if pygame.sprite.spritecollide(self, bigBullets, False):
            self.hp -= dmgPlayer2
        if self.timer > 0:
            self.timer -= 1
        else:
            self.timer = 0
        if self.timer == 0:
            EnemyBullet(self.angle, 0, self.rect)
            self.timer = 50
        if self.hp < 1:
            destroyedEnemies += 1
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

ExclusiveEnemyImg1 = pygame.image.load('quad.png')
ExclusiveEnemyImg2 = pygame.image.load('aegires.png')
ExclusiveEnemyImg3 = pygame.image.load('antumbra.png')
ExclusiveEnemyImg4 = pygame.image.load('eclipse.png')
ExclusiveEnemyImg5 = pygame.image.load('navanax.png')
ExclusiveEnemyImg6 = pygame.image.load('omura.png')
ExclusiveEnemyImg7 = pygame.image.load('sei.png')

class ExclusiveEnemy(pygame.sprite.Sprite):
    def __init__ (self, group):
        global dmgEnemy5
        pygame.sprite.Sprite.__init__(self)
        self.randomImgBoss = random.randint(1,7)
        if self.randomImgBoss == 1:
            self.image = ExclusiveEnemyImg1
        if self.randomImgBoss == 2:
            self.image = ExclusiveEnemyImg2
        if self.randomImgBoss == 3:
            self.image = ExclusiveEnemyImg3
        if self.randomImgBoss == 4:
            self.image = ExclusiveEnemyImg4
        if self.randomImgBoss == 5:
            self.image = ExclusiveEnemyImg5
        if self.randomImgBoss == 6:
            self.image = ExclusiveEnemyImg6
        if self.randomImgBoss == 7:
            self.image = ExclusiveEnemyImg7
        self.image = pygame.transform.scale(self.image,(200,200))
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.spawn = random.randint(1,2)   
        self.timer = 0
        if hardMode == True:
            self.hp = 20
        else:
            self.hp = 30
        self.timer = 0
        if self.spawn == 1:
            self.rect.x = 500
            self.rect.y = -100
            self.angle = 180
        if self.spawn == 2:
            self.rect.x = 500
            self.rect.y = 690
            self.angle = 0
        if hardMode == True:
            dmgEnemy5 = 20
        else:
            dmgEnemy5 = 10
        self.move = False
        self.rot = False
        self.rand = 0
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.add(group)
    def update(self):
        global destroyedEnemies
        if self.rect.y == 250 and self.move == False:
            self.rect.x += 1
            self.move = True
            self.rand = random.randint(1,2)
            if self.rand == 1 and self.rot == False:
                self.angle = -90
            if self.rand == 2 and self.rot == False:
                self.angle = 90
            if self.rot == False:
                self.rot = True
                if self.rand == 1:
                    self.angle = -90
                if self.rand == 2:
                    self.angle = 90
                self.rotated = pygame.transform.rotate(self.image, self.angle)
                self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
                self.image = self.rotated
        if self.move == False:
            self.rect.x -= 1 * math.sin(self.angle * (math.pi / 180))
        else:
            self.rect.x -= 1 * math.sin(self.angle * (math.pi / 180))
        if self.move == False:
            self.rect.y -= 1 * math.cos(self.angle * (math.pi / 180))
        if pygame.sprite.spritecollide(self, bullets, True):
            self.hp -= dmgPlayer
        if pygame.sprite.spritecollide(self, bigBullets, False):
            self.hp -= dmgPlayer2
        if self.timer > 0:
            self.timer -=1
        else:
            self.timer = 0
        if self.timer == 0:
            self.timer = 50
        if self.rect.x > 1600 or self.rect.x < -400:
            bang.play()
            self.kill()
        if self.hp < 1:
            destroyedEnemies += 1
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

dlcEnemyImg = pygame.image.load('dlcEnemy.png')

class EnemyDlc(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = dlcEnemyImg
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.spawn = random.randint(1,2)   
        if hardMode == True:
            self.hp = 15
        else:
            self.hp = 5
        self.timer = 0
        if self.spawn == 1:
            self.rect.x = 540
            self.rect.y = 30
            self.angle = 180
        if self.spawn == 2:
            self.rect.x = 540
            self.rect.y = 590
            self.angle = 0
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.add(group)
    def update(self):
        global destroyedEnemies
        if pygame.sprite.spritecollide(self, bullets, True):
            self.hp -= dmgPlayer
        if pygame.sprite.spritecollide(self, bigBullets, False):
            self.hp -= dmgPlayer2
        if self.timer > 0:
            self.timer -=1
        else:
            self.timer = 0
        if self.timer == 0:
            EnemyBullet2(self.angle, 0, self.rect)
            self.timer = 150
        if self.hp < 1:
            destroyedEnemies += 1
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

towerSpawnImgDmg = pygame.image.load('tower-spawn.png')
towerSpawnImgDmg2 = pygame.image.load('tower-spawn2.png')
towerSpawnImgDmg3 = pygame.image.load('tower-spawn3.png')

class TowerSpawn(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = towerSpawnImgDmg
        self.hp = 50
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(blocks)
        self.add(group)
        place.play()
    def update(self):
        if self.hp > 30:
            self.image = towerSpawnImgDmg
        if self.hp > 20 and self.hp < 31:
            self.image = towerSpawnImgDmg2
        if self.hp < 21:
            self.image = towerSpawnImgDmg3
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 50:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(2, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

tower1ImgDmg1 = pygame.image.load('parallax.png')
tower1ImgDmg2 = pygame.image.load('arc.png')
tower1ImgDmg3 = pygame.image.load('duo.png')
tower1ImgDmg4 = pygame.image.load('hail.png')
tower1ImgDmg5 = pygame.image.load('scorch.png')

class Tower(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.rand = random.randint(1,5)
        if self.rand == 1:
            self.image = tower1ImgDmg1
        if self.rand == 2:
            self.image = tower1ImgDmg2
        if self.rand == 3:
            self.image = tower1ImgDmg3
        if self.rand == 4:
            self.image = tower1ImgDmg4
        if self.rand == 5:
            self.image = tower1ImgDmg5
        self.hp = 10
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rotated = pygame.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.a = angle
        self.rechare = 0
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)
        place.play()
    def update(self):
        global hlak
        if self.rechare > 1:
            self.rechare -= 1
        else:
            self.rechare = 0
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 10:
                self.hp += 1
        if pygame.sprite.spritecollide(self, towerSpawns, False):
            if dlcWork == True:
                if hardMode == True:
                    if self.rechare == 0 and hlak > 9.9:
                        Bullet(self.a, 0, self.rect)
                        self.rechare = 100
                        hlak -= 10
                else:
                    if self.rechare == 0 and hlak > 0.9:
                        Bullet(self.a, 0, self.rect)
                        self.rechare = 100
                        hlak -= 1
            else:
                if self.rechare == 0:
                    Bullet(self.a, 0, self.rect)
                    self.rechare = 100
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if self.hp < 1:
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

tower2ImgDmg1 = pygame.image.load('segment.png')
tower2ImgDmg2 = pygame.image.load('lancer.png')
tower2ImgDmg3 = pygame.image.load('salvo.png')
tower2ImgDmg4 = pygame.image.load('scatter.png')
tower2ImgDmg5 = pygame.image.load('wave.png')
tower2ImgDmg6 = pygame.image.load('swarmer.png')

class Tower2(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.rand = random.randint(1,6)
        if self.rand == 1:
            self.image = tower2ImgDmg1
        if self.rand == 2:
            self.image = tower2ImgDmg2
        if self.rand == 3:
            self.image = tower2ImgDmg3
        if self.rand == 4:
            self.image = tower2ImgDmg4
        if self.rand == 5:
            self.image = tower2ImgDmg5
        if self.rand == 6:
            self.image = tower2ImgDmg6
        self.hp = 10
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rotated = pygame.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.a = angle
        self.rechare = 0
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)
        place.play()
    def update(self):
        global hlak
        if self.rechare > 1:
            self.rechare -= 1
        else:
            self.rechare = 0
        if pygame.sprite.spritecollide(self, towerSpawns, False):
            if dlcWork == True:
                if hardMode == True:
                    if self.rechare == 0 and hlak > 9.9:
                        Bullet2(self.a, 0, self.rect, False)
                        self.rechare = 300
                        hlak -= 10
                else:
                    if self.rechare == 0 and hlak > 0.9:
                        Bullet2(self.a, 0, self.rect, False)
                        self.rechare = 300
                        hlak -= 1
            else:
                if self.rechare == 0:
                    Bullet2(self.a, 0, self.rect, False)
                    self.rechare = 300
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 10:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

tower3Img1 = pygame.image.load('cyclone.png')
tower3Img2 = pygame.image.load('ripple.png')
tower3Img3 = pygame.image.load('foreshadow.png')
tower3Img4 = pygame.image.load('spectre.png')
tower3Img5 = pygame.image.load('tsunami.png')
tower3Img6 = pygame.image.load('meltdown.png')

class Tower3(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.rand = random.randint(1,6)
        if self.rand == 1:
            self.image = tower3Img1
        if self.rand == 2:
            self.image = tower3Img2
        if self.rand == 3:
            self.image = tower3Img3
        if self.rand == 4:
            self.image = tower3Img4
        if self.rand == 5:
            self.image = tower3Img5
        if self.rand == 6:
            self.image = tower3Img6
        self.hp = 1
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rotated = pygame.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.a = angle
        self.rechare = 0
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)
        place.play()
    def update(self):
        global hlak
        if self.rechare > 1:
            self.rechare -= 1
        else:
            self.rechare = 0
        if pygame.sprite.spritecollide(self, towerSpawns, False):
            if dlcWork == True:
                if hardMode == True:
                    if self.rechare == 0 and hlak > 9.9:
                        Bullet2(self.a, 0, self.rect, False)
                        Bullet2(self.a, 0, self.rect, False)
                        self.rechare = 150
                        hlak -= 10
                else:
                    if self.rechare == 0 and hlak > 0.9:
                        Bullet2(self.a, 0, self.rect, False)
                        Bullet2(self.a, 0, self.rect, False)
                        self.rechare = 150
                        hlak -= 1
            else:
                if self.rechare == 0:
                    Bullet2(self.a, 0, self.rect, False)
                    Bullet2(self.a, 0, self.rect, False)
                    self.rechare = 150
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 1:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

tower4Img = pygame.image.load('fuse.png')

class Tower4(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = tower4Img
        self.hp = 1
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rotated = pygame.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.a = angle
        self.rechare = 0
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)
        place.play()
    def update(self):
        global hlak
        if self.rechare > 1:
            self.rechare -= 1
        else:
            self.rechare = 0
        if pygame.sprite.spritecollide(self, towerSpawns, False):
            if hardMode == True:
                if self.rechare == 0 and hlak > 9.9:
                    Bullet2(self.a, 0, self.rect, False)
                    Bullet(self.a, 0, self.rect)
                    Bullet2(self.a, 0, self.rect, False)
                    Bullet(self.a, 0, self.rect)
                    self.rechare = 150
                    hlak -= 10
            else:
                if self.rechare == 0 and hlak > 9.9:
                    Bullet2(self.a, 0, self.rect, False)
                    Bullet(self.a, 0, self.rect)
                    Bullet2(self.a, 0, self.rect, False)
                    Bullet(self.a, 0, self.rect)
                    self.rechare = 150
                    hlak -= 10
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 1:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

limitTower = False
tower5Img = pygame.image.load('warning-tower.png')

class Tower5(pygame.sprite.Sprite):
    def __init__ (self, group):
        global limitTower
        limitTower = True
        pygame.sprite.Sprite.__init__(self)
        self.image = tower5Img
        self.hp = 100
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rotated = pygame.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.a = angle
        self.rechare = 0
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)
        place.play()
        self.timer = 0
    def update(self):
        global hlak
        global limitTower
        self.timer -= 1
        if self.timer < 1:
            Bullet2(self.a, 0, self.rect, True)
            self.timer = 10
        hlak -= 0.1
        if hlak < 0.1:
            self.hp -= 1
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 1:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.hp = 0
            Rubble(4, self.rect.x, self.rect.y, rubble)
            self.kill()
            limitTower = False
        if destroyAll == True:
            self.hp = 0
            self.kill()
            limitTower = False

tower6Img = pygame.image.load('repair-turret.png')

class Tower6(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = tower6Img
        self.hp = 1
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rotated = pygame.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.a = angle
        self.rechare = 0
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)
        place.play()
    def update(self):
        global hlak
        if self.rechare > 1:
            self.rechare -= 1
        else:
            self.rechare = 0
        if pygame.sprite.spritecollide(self, towerSpawns, False):
            if dlcWork == True:
                if hardMode == True:
                    if self.rechare == 0 and hlak > 9.9:
                        HealBullet(self.a, 0, self.rect)
                        self.rechare = 30
                        hlak -= 10
                else:
                    if self.rechare == 0 and hlak > 0.9:
                        HealBullet(self.a, 0, self.rect)
                        self.rechare = 30
                        hlak -= 1
            else:
                if self.rechare == 0:
                    HealBullet(self.a, 0, self.rect)
                    self.rechare = 30
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if self.hp < 1:
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

tower6Img1 = pygame.image.load('artillery.png')
tower6Img2 = pygame.image.load('artillery-mount.png')
tower6Img3 = pygame.image.load('beam-weapon.png')
tower6Img4 = pygame.image.load('eruption.png')
tower6Img5 = pygame.image.load('flamethrower.png')
tower6Img6 = pygame.image.load('heal-shotgun-weapon.png')
tower6Img7 = pygame.image.load('large-bullet-mount.png')

class HelpTower(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.rand = random.randint(1,7)
        if self.rand == 1:
            self.image = tower6Img1
        if self.rand == 2:
            self.image = tower6Img2
        if self.rand == 3:
            self.image = tower6Img3
        if self.rand == 4:
            self.image = tower6Img4
        if self.rand == 5:
            self.image = tower6Img5
        if self.rand == 6:
            self.image = tower6Img6
        if self.rand == 7:
            self.image = tower6Img7
        self.hp = 1
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rotated = pygame.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated.get_rect(center=self.rect.center)
        self.image = self.rotated
        self.a = angle
        self.rechare = 0
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)
        place.play()
    def update(self):
        if self.rechare > 1:
            self.rechare -= 1
        else:
            self.rechare = 0
        if self.rect.x > 559 and self.rect.x < 641:
            if self.rect.y > 270 and self.rect.y < 380:
                if self.rechare == 0:
                    Bullet(self.a, 0, self.rect)
                    self.rechare = 10
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if self.hp < 1:
            bang.play()
            self.kill()
        if destroyAll == True:
            self.kill()

escapeImgDmg = pygame.image.load('launch-pad.png')
escapeImgDmg2 = pygame.image.load('launch-pad2.png')
escapeImgDmg3 = pygame.image.load('launch-pad3.png')

class Escape(pygame.sprite.Sprite):
    def __init__ (self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = escapeImgDmg
        self.hp = 50
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.x = Mouse_x
        self.rect.y = Mouse_y
        self.add(group)
        place.play()
    def update(self):
        global canEscape
        if self.hp > 30:
            self.image = escapeImgDmg
        if self.hp > 20 and self.hp < 31:
            self.image = escapeImgDmg2
        if self.hp < 21:
            self.image = escapeImgDmg3
        if Mouse_x > self.rect.x and Mouse_x < self.rect.x + 160 and Mouse_y > self.rect.y and Mouse_y < self.rect.y + 160:
            if mouseClick == True and clicked == 1:
                if copper > 1500 or copper == 1500:
                    if led > 1000 or led == 1000:
                        canEscape = True
        if pygame.sprite.spritecollide(self, enemies, True):
            bang.play()
            if doUnlHp == False:
                self.hp -= dmgEnemy
        if pygame.sprite.spritecollide(self, enemies3, False):
            if doUnlHp == False:
                self.hp -= dmgEnemy3
            bigBang.play()
        if pygame.sprite.spritecollide(self, enemyBullets, True):
            if doUnlHp == False:
                self.hp -= dmgEnemy4
            bang.play()
        if pygame.sprite.spritecollide(self, enemyBullets2, False):
            if doUnlHp == False:
                self.hp -= dmgDlcEnemy
            bang.play()
        if pygame.sprite.spritecollide(self, healBullets, True):
            if self.hp < 50:
                self.hp += 1
        if self.hp < 1:
            bang.play()
            self.kill()
            Rubble(5, self.rect.x, self.rect.y, rubble)
        if destroyAll == True:
            self.kill()

gameTimer = 0
destroyTimer = 0

selectedPlanet = 0

if dlcWork == True:
    selectedPlanet = random.randint(1,5)
if dlcWork == False:
    selectedPlanet = random.randint(1,4)

planetRealm = pygame.image.load('planetRealm.jpg')
planetRealmEng = pygame.image.load('planetRealmEng.jpg')
bg1 = pygame.image.load('bg.jpg')
blackHole = pygame.image.load('blackHole.jpg')
blackHoleEng = pygame.image.load('blackHoleEng.jpg')
bg2 = pygame.image.load('bg2.jpg')
planetEarth = pygame.image.load('planetEarth.jpg')
planetEarthEng = pygame.image.load('planetEarthEng.jpg')
bg3 = pygame.image.load('bg3.jpg')
planetLuck = pygame.image.load('planetLuck.jpg')
planetLuckEng = pygame.image.load('planetLuckEng.jpg')
bg4 = pygame.image.load('bg4.jpg')
planetUranius = pygame.image.load('planetUranius.jpg')
planetUraniusEng = pygame.image.load('planetUraniusEng.jpg')
bg5 = pygame.image.load('bg5.jpg')

map = pygame.sprite.Sprite()
map = pygame.image.load('planetRealm.jpg')
if selectedPlanet == 1:
    map = pygame.image.load('planetRealm.jpg')
    bg = pygame.image.load('bg.jpg')
if selectedPlanet == 2:
    map = pygame.image.load('blackHole.jpg')
    bg = pygame.image.load('bg2.jpg')
if selectedPlanet == 3:
    map = pygame.image.load('planetEarth.jpg')
    bg = pygame.image.load('bg3.jpg')
if selectedPlanet == 4:
    map = pygame.image.load('planetLuck.jpg')
    bg = pygame.image.load('bg4.jpg')
if dlcWork == True:
    if selectedPlanet == 5:
        map = pygame.image.load('planetUranius.jpg')
        bg = pygame.image.load('bg5.jpg')
map_rect = map.get_rect()
map = pygame.transform.scale(map, (450,300))
map_rect.x = 10
map_rect.y = 300

helpShip = pygame.sprite.Sprite()
helpShip = pygame.image.load('bryde.png')
helpShip_rect = helpShip.get_rect()
helpShip_rect.x = 535
helpShip_rect.y = 660

whiteTree = pygame.sprite.Sprite()
whiteTree = pygame.image.load('white-tree.png')
whiteTree_rect = whiteTree.get_rect()
whiteTree_rect.x = 75
whiteTree_rect.y = 100

whiteTreeDead = pygame.sprite.Sprite()
whiteTreeDead = pygame.image.load('white-tree-dead.png')
whiteTreeDead_rect = whiteTreeDead.get_rect()
whiteTreeDead_rect.x = 775
whiteTreeDead_rect.y = 570

basaltStone = pygame.sprite.Sprite()
basaltStone = pygame.image.load('basalt-boulder1.png')
basaltStone_rect = basaltStone.get_rect()
basaltStone_rect.x = 475
basaltStone_rect.y = 364

shipHelpTimer = 1000
reloadPhotoMode = 15
photoMode = False

reward = 0

def timerDown(timer, number):
    if timer > 0:
        timer -= number
    else:
        timer = 0
    return timer

def classesUpdate():
    rubble.update()
    enemies.update()
    enemies2.update()
    enemies3.update()
    enemies4.update()
    towerSpawns.update()
    bullets.update()
    bigBullets.update()
    healBullets.update()
    enemyBullets.update()
    enemyBullets2.update()
    enemies.update()
    enemies2.update()
    enemies3.update()
    enemies4.update()
    blocks.update()

def gameBlit():
    global shipHelpTimer
    global led
    global thorium
    global copper
    screen.blit(bg, bg_rect)
    if selectedPlanet == 2:
        screen.blit(basaltStone, basaltStone_rect)
    screen.blit(comCenter, comCenter_rect)
    screen.blit(full, full_rect)
    if photoMode == False:
        screen.blit(copAsteroid, copAsteroid_rect)
        screen.blit(ledAsteroid, ledAsteroid_rect)
        rubble.draw(screen)
        if hardMode == True:
            screen.blit(thoriumAsteroid, thoriumAsteroid_rect)
    if photoMode == False:
        screen.blit(helpButton, helpButton_rect)
        if dlcWork == True:
            screen.blit(helpButton2, helpButton2_rect)
    if photoMode == False:
        screen.blit(drill, drill_rect)
        screen.blit(rotator_rotated, rotator_rotated_rect)   
    towerSpawns.draw(screen)
    blocks.draw(screen)
    enemies.draw(screen)
    enemies2.draw(screen)
    enemies3.draw(screen)
    enemies4.draw(screen)
    if selectedPlanet == 1:
        screen.blit(whiteTree, whiteTree_rect)
    if selectedPlanet == 3:
        screen.blit(whiteTreeDead, whiteTreeDead_rect)      
    if airdrops == True:
        if shipHelpTimer == 0:
            screen.blit(helpShip, helpShip_rect)
            helpShip_rect.y -= 1
            if helpShip_rect.y == 320:
                copper += random.randint(10, 300)
                led += random.randint(0, 100)
                if hardMode == True:
                    thorium += random.randint(0, 50)
            if helpShip_rect.y < -200:
                shipHelpTimer = random.randint(1000,5000)
                helpShip_rect.y = 669
    if photoMode == False:
        screen.blit(player_rotated, player_rotated_rect)
        screen.blit(gun_rotated, gun_rotated_rect)
        if gameMode == 'Coop':
            screen.blit(player2_rotated, player2_rotated_rect)
            screen.blit(gun2_rotated, gun2_rotated_rect)
    if photoMode == False:
        bullets.draw(screen)
        bigBullets.draw(screen)
        healBullets.draw(screen)
        enemyBullets.draw(screen)
        enemyBullets2.draw(screen)
    if photoMode == False:
        if fogWork == True:
            screen.blit(fog, fog_rect)
            screen.blit(fog2, fog2_rect)
        screen.blit(text, (57, 7))
        screen.blit(coper, coper_rect)
        screen.blit(text2, (57, 57))
        screen.blit(lead, lead_rect)
        if dlcWork == True:
            screen.blit(text7, (57, 157))
            screen.blit(grafite, grafite_rect)
            screen.blit(text6, (57, 500))
            screen.blit(oils, oils_rect)
            screen.blit(text4, (57, 600))
            screen.blit(shlak, shlak_rect)
            screen.blit(text5, (57, 550))
            screen.blit(vater, vater_rect)
        if hardMode == True:
            screen.blit(text3, (57, 107))
            screen.blit(thory, thory_rect)
        if storeActivated == True:
            text8 = Font1.render(str(money), True, (255, 255, 255))
            screen.blit(text8, (420, 100))
            screen.blit(coin, coin_rect)
            coin_rect.y = 100
            screen.blit(slot1, slot1_rect)
            screen.blit(slot2, slot2_rect)
            if hardMode == True:
                screen.blit(slot3, slot3_rect)
            if dlcWork == True:
                screen.blit(slot4, slot4_rect)
        screen.blit(shop, shop_rect)
        if dialogNumber == 3:
            screen.blit(copAsteroidHelp, copAsteroidHelp_rect)
        if photoMode == False:
            if tutorialWork == True:
                screen.blit(dialog, dialog_rect)
    if textForPrintTimer > 0:
        screen.blit(textPrint, (0, 620))
    if console == True:
        screen.blit(textButton, textButton_rect)
        screen.blit(textComSee, (20, 600))

textVersion = VersionFont.render(versionGame, True, (0, 250, 255))

def settingsBlit():
    screen.blit(collectionCard, collectionCard_rect)
    screen.blit(hardModeButton, hardModeButton_rect)
    screen.blit(musicButton, musicButton_rect)
    if testSee == True:
        screen.blit(unlimitedResButton, unlimitedResButton_rect)
        screen.blit(enemiesSpawn, enemiesSpawn_rect)
        screen.blit(unlimitedHpButton, unlimitedHpButton_rect)
        screen.blit(cheatButton, cheatButton_rect)
        screen.blit(nextButton, nextButton_rect)
        screen.blit(nextEquip, nextEquip_rect)
        screen.blit(airdropButton, airdropButton_rect)
        screen.blit(randButton, randButton_rect)
        screen.blit(cheatHelp, cheatHelp_rect)
        screen.blit(fogButton, fogButton_rect)
    text8 = Font1.render(str(money), True, (255, 255, 255))
    coin_rect.y = 190
    screen.blit(langButton, langButton_rect)
    screen.blit(text8, (420, 190))
    screen.blit(coin, coin_rect)
    screen.blit(dlc, dlc_rect)
    screen.blit(equipSee, equipSee_rect)
    screen.blit(equipSee2, equipSee2_rect)
    screen.blit(costHelp, costHelp_rect)
    screen.blit(testSeeButton, testSeeButton_rect)
    screen.blit(texture, texture_rect)
    screen.blit(map, map_rect)
    screen.blit(textVersion, (1030, 640))

def infoBlit():
    screen.blit(helpBlocks, helpBlocks_rect)
    screen.blit(contr, contr_rect)
    screen.blit(helpEsc, helpEsc_rect)
    screen.blit(textVersion, (1030, 640))

def building(time, timeH, needC, needL, needG, needO, needHC, needHL, needHT, needHG, needHO, funct, group):
    global hardMode, mouseClick, clicked, copper, led, thorium, graphite, oil, createTimer
    if mouseClick == True and clicked == 1:
        if createTimer < 1:
            if hardMode == True:
                if copper > needHC or copper == needHC or 0 == needHC:
                    if led > needHL or led == needHL or 0 == needHL:
                        if thorium > needHT or thorium == needHT or 0 == needHT:
                            if oil > needHO or oil == needHO or 0 == needHO:
                                if graphite > needHG or graphite == needHG or 0 == needHG:
                                    copper -= needHC
                                    led -= needHL
                                    thorium -= needHT
                                    oil -= needHO
                                    graphite -= needHG
                                    funct(group)
                                    createTimer = timeH
            else:
                if copper > needC or copper == needC:
                    if led > needL or led == needL:
                        if oil > needO or oil == needO:
                            if graphite > needG or graphite == needG:
                                copper -= needC
                                led -= needL
                                oil -= needO
                                graphite -= needG
                                funct(group)
                                createTimer = time
    
comCenterImg1 = pygame.image.load('spawn.png')
comCenterImg2 = pygame.image.load('spawn2.png')
comCenterImg3 = pygame.image.load('spawn3.png')
comCenterImg4 = pygame.image.load('spawn4.png')
comCenterImg5 = pygame.image.load('spawn5.png')
comCenterImg6 = pygame.image.load('spawn6.png')

cursorImg = pygame.image.load('cursor.png')
cursorHand = pygame.image.load('hand.png')
cursorH = pygame.image.load('cursorH.png')
cursorH2 = pygame.image.load('cursorH2.png')
cursorDrill = pygame.image.load('drill.png')

dialog1 = pygame.image.load('dialog1.png')
dialog2 = pygame.image.load('dialog2.png')
dialog3 = pygame.image.load('dialog3.png')
dialog4 = pygame.image.load('dialog4.png')
dialog5 = pygame.image.load('dialog5.png')
dialog6 = pygame.image.load('dialog6.png')

dialog1E = pygame.image.load('dialog1Eng.png')
dialog2E = pygame.image.load('dialog2Eng.png')
dialog3E = pygame.image.load('dialog3Eng.png')
dialog4E = pygame.image.load('dialog4Eng.png')
dialog5E = pygame.image.load('dialog5Eng.png')
dialog6E = pygame.image.load('dialog6Eng.png')

shopOn = pygame.image.load('shopOn.png')
shopOff = pygame.image.load('shopOff.png')

hardModeOn = pygame.image.load('hardModeOn.png')
hardModeOff = pygame.image.load('hardModeOff.png')

soundOn = pygame.image.load('soundOn.png')
soundOff = pygame.image.load('soundOff.png')

airdropOn = pygame.image.load('airdropsOn.png')
airdropOff = pygame.image.load('airdropsOff.png')

cheatOn = pygame.image.load('cheatModOn.png')
cheatOff = pygame.image.load('cheatModOff.png')

dlcOn = pygame.image.load('dlcOn.png')
dlcOff = pygame.image.load('dlcOff.png')

fogOn = pygame.image.load('fogOn.png')
fogOff = pygame.image.load('fogOff.png')

randomSkinOn = pygame.image.load('randomSkinOn.png')
randomSkinOff = pygame.image.load('randomSkinOff.png')

tutorialOn = pygame.image.load('tutorialOn.png')
tutorialOff = pygame.image.load('tutorialOff.png')

unlimitedHpOn = pygame.image.load('unlimitedHpOn.png')
unlimitedHpOff = pygame.image.load('unlimitedHpOff.png')

unlimitedResOn = pygame.image.load('unlimitedResOn.png')
unlimitedResOff = pygame.image.load('unlimitedResOff.png')

withEnemyOn = pygame.image.load('withEnemyOn.png')
withEnemyOff = pygame.image.load('withEnemyOff.png')

cheatModOn = pygame.image.load('cheatModOn.png')
cheatModOff = pygame.image.load('cheatModOff.png')

testSettingsOn = pygame.image.load('testSettingsOn.png')
testSettingsOff = pygame.image.load('testSettingsOff.png')

testSettingsOnE = pygame.image.load('testSettingsOnEng.png')
testSettingsOffE = pygame.image.load('testSettingsOffEng.png')

textButtonOn = pygame.image.load('textButtonOn.png')
textButtonOff = pygame.image.load('textButtonOff.png')

langRu = pygame.image.load('rusLang.png')
langEng = pygame.image.load('engLang.png')

equipmentBullet = pygame.image.load('equipmentBullet.png')
equipmentBullet2 = pygame.image.load('equipmentBullet2.png')
equipmentBigBullet = pygame.image.load('equipmentBigBullet.png')
equipmentBigBullet2 = pygame.image.load('equipmentBigBullet2.png')
equipmentHealBullet = pygame.image.load('equipmentHealBullet.png')
equipmentHealBullet2 = pygame.image.load('equipmentHealBullet2.png')

helpCheat = pygame.image.load('cheat.png')
helpCheatE = pygame.image.load('cheatEng.png')

escHelpT = pygame.image.load('escHelp.png')
escHelpTE = pygame.image.load('escHelpEng.png')

buttonL= pygame.image.load('buttonLose.png')
buttonW = pygame.image.load('buttonWin.png')
buttonR = pygame.image.load('buttonRestart.png')
buttonLE= pygame.image.load('buttonLoseEng.png')
buttonWE = pygame.image.load('buttonWinEng.png')
buttonRE = pygame.image.load('buttonRestartEng.png')

load = pygame.image.load('loading.jpg')
loadE = pygame.image.load('loadingEng.png')

control = pygame.image.load('control.png')
controlEng = pygame.image.load('controlEng.png')

costHelpIM = pygame.image.load('costHelp.png')
costHelpIMEng = pygame.image.load('costHelpEng.png')

timerForRestart = 0

def maxSpeed(spdX, spdY, maxSpeedX, maxSpeedY):
    if spdX < -maxSpeedX:
        spdX = -maxSpeedX
    if spdX > maxSpeedX:
        spdX = maxSpeedX
    if spdY < -maxSpeedY:
        spdY = -maxSpeedY
    if spdY > maxSpeedY:
        spdY = maxSpeedY
    return spdX, spdY

def ButtonOn(button, buttonOn, timerBut, butBool, width, height):
    button = buttonOn
    button = pygame.transform.scale(button, (width, height))
    timerBut = 15
    butBool = True
    click.play()
    return button, timerBut, butBool

def ButtonOff(button, buttonOff, timerBut, butBool, width, height):
    button = buttonOff
    button = pygame.transform.scale(button, (width, height))
    timerBut = 15
    butBool = False
    click.play()
    return button, timerBut, butBool

def restart():
    global dialogNumber, cardSkin, collectionCard, doEnemiesSpawn, dialog, waveTimer, dmgEnemy, dmgPlayer, dmgPlayer2, copper, led, thorium , hlak, water, graphite, oil, wave, photoMode, menuOpen, canEscape, comCenterHP, shipHelpTimer, comCenterHP, destroyAll, timerForRestart, rotSpeed, drillSpeed, drillTimer
    z = 0
    if maxCards == 0:        
        maxZ = random.randint(0,maxCards)
    else:
        maxZ = random.randint(1,maxCards)
    textZ = ''
    cardSkin = ''
    while z < maxZ + 1:
        if maxZ == z:
            textZ = z
        z += 1   
    i = 0
    while i < maxZ + 1:
        if textZ == i:
            collectionCard = allCards[i]
        i += 1
    canEscape = False
    rotSpeed = 0
    drillSpeed = 5
    drillTimer = 5
    pygame.mixer.stop()
    timerForRestart = 35
    destroyAll = True
    comCenterHP = 300
    shipHelpTimer = 1000
    canEscape = False
    wave = 0
    if doEnemiesSpawn2 == True:
        doEnemiesSpawn = True
    else:
        doEnemiesSpawn = False
    photoMode = False
    menuOpen = True
    dialogNumber = 1
    dialog = dialog1
    if hardMode == True:
        waveTimer = 50
        dmgEnemy = 30
        dmgPlayer = 0.1
        dmgPlayer2 = 1
        if unlMode == False:
            copper = -100
            led = -100    
            thorium = -50
            hlak = -100
            water = -10
            graphite = -100
            oil = -30
        else:
            copper = 99999
            led = 99999
            thorium = 99999
            hlak = 99999
            water = 99999
            graphite = 99999
            oil = 99999
    else:
        dmgEnemy = 10
        dmgPlayer = 1
        dmgPlayer2 = 0.1
        waveTimer = 160 
        if unlMode == False:
            copper = 10
            led = 0    
            hlak = 0
            water = 0
            oil = 0
            graphite = 0
            thorium = 0
    if unlMode == True:
        copper = 99999
        led = 99999
        thorium = 99999
        hlak = 99999
        water = 99999
        oil = 99999
        graphite = 99999
    else:
        if hardMode == False:
            copper = 10
            led = 0
            hlak = 0
            water = 0
            oil = 0
            thorium = 0
            graphite = 0
        else:
            copper = -100
            led = -100        
            thorium = -50  
            hlak = -100
            water = -10
            oil = -30
            graphite = -100
    classesUpdate()
    pygame.mixer.stop()
    menu.play()
    destroyAll = False
    canEscape = False
    
def soundChange(volume):
    inGame.set_volume(volume)
    inGame2.set_volume(volume)
    inGame3.set_volume(volume)
    inGame4.set_volume(volume)
    inGame5.set_volume(volume)
    bang.set_volume(volume)
    bigBang.set_volume(volume)
    click.set_volume(volume)
    menu.set_volume(volume)
    place.set_volume(volume)
    shoot.set_volume(volume)
    bigShoot.set_volume(volume) 

def resourseChange(C, L, T, H, W, O, G):
    copper = C
    led = L
    thorium = T
    hlak = H
    water = W
    oil = O
    graphite = G
    return copper, led, thorium, hlak, water, oil, graphite

otherTimer = 15

res = copper + led + thorium + graphite + water + oil + hlak

maxFull = 411094

oneProcent = maxFull / 100

procentFull = res / oneProcent

console = False
reloadEscMode = 0
command = ''

card0 = pygame.image.load('CardsNew\cardNotOpened.png')
card1 = pygame.image.load('CardsNew\Animal_Pen.png')
card2 = pygame.image.load('CardsNew\Apple.png')
card3 = pygame.image.load('CardsNew\Apple_Tree.png')
card4 = pygame.image.load('CardsNew\Baby.png')
card5 = pygame.image.load('CardsNew\Bear.png')
card6 = pygame.image.load('CardsNew\Berry.png')
card7 = pygame.image.load('CardsNew\Berry_Bush.png')
card8 = pygame.image.load('CardsNew\Bone.png')
card9 = pygame.image.load('CardsNew\Brick.png')
card10 = pygame.image.load('CardsNew\Brickyard.png')
card11 = pygame.image.load('CardsNew\Campfire.png')
card12 = pygame.image.load('CardsNew\Carrot.png')
card13 = pygame.image.load('CardsNew\Catacombs.png')
card14 = pygame.image.load('CardsNew\Chicken.png')
card15 = pygame.image.load('CardsNew\Coin.png')
card16 = pygame.image.load('CardsNew\Coin_Chest.png')
card17 = pygame.image.load('CardsNew\Cooked_Meat.png')
card18 = pygame.image.load('CardsNew\Corpse.png')
card19 = pygame.image.load('CardsNew\Cow.png')
card20 = pygame.image.load('CardsNew\Demon.png')
card21 = pygame.image.load('CardsNew\Dog.png')
card22 = pygame.image.load('CardsNew\Egg.png')
card23 = pygame.image.load('CardsNew\Explorer.png')
card24 = pygame.image.load('CardsNew\Farm.png')
card25 = pygame.image.load('CardsNew\Flint.png')
card26 = pygame.image.load('CardsNew\Forest.png')
card27 = pygame.image.load('CardsNew\Frittata.png')
card28 = pygame.image.load('CardsNew\Fruit_Salad.png')
card29 = pygame.image.load('CardsNew\Garden.png')
card30 = pygame.image.load('CardsNew\Giant_Rat.png')
card31 = pygame.image.load('CardsNew\Goblin.png')
card32 = pygame.image.load('CardsNew\Golden_Goblet.png')
card33 = pygame.image.load('CardsNew\Graveyard.png')
card34 = pygame.image.load('CardsNew\House.png')
card35 = pygame.image.load('CardsNew\Idea_-_Animal_Pen.png')
card36 = pygame.image.load('CardsNew\Idea_-_Bricks.png')
card37 = pygame.image.load('CardsNew\Idea_-_Brickyard.png')
card38 = pygame.image.load('CardsNew\Idea_-_Campfire.png')
card39 = pygame.image.load('CardsNew\Idea_-_Chicken.png')
card40 = pygame.image.load('CardsNew\Idea_-_Coin_Chest.png')
card41 = pygame.image.load('CardsNew\Idea_-_Cooked_Meat.png')
card42 = pygame.image.load('CardsNew\Idea_-_Farm.png')
card43 = pygame.image.load('CardsNew\Idea_-_Frittata.png')
card44 = pygame.image.load('CardsNew\Idea_-_Fruit_Salad.png')
card45 = pygame.image.load('CardsNew\Idea_-_Garden.png')
card46 = pygame.image.load('CardsNew\Idea_-_Growth.png')
card47 = pygame.image.load('CardsNew\Idea_-_House.png')
card48 = pygame.image.load('CardsNew\Idea_-_Lumber_Camp.png')
card49 = pygame.image.load('CardsNew\Idea_-_Market.png')
card50 = pygame.image.load('CardsNew\Idea_-_Milkshake.png')
card51 = pygame.image.load('CardsNew\Idea_-_Mine.png')
card52 = pygame.image.load('CardsNew\Idea_-_Offspring.png')
card53 = pygame.image.load('CardsNew\Idea_-_Omelette.png')
card54 = pygame.image.load('CardsNew\Idea_-_Planks.png')
card55 = pygame.image.load('CardsNew\Idea_-_Quarry.png')
card56 = pygame.image.load('CardsNew\Idea_-_Sawmill.png')
card57 = pygame.image.load('CardsNew\Idea_-_Shed.png')
card58 = pygame.image.load('CardsNew\Idea_-_Smelter.png')
card59 = pygame.image.load('CardsNew\Idea_-_Spear.png')
card60 = pygame.image.load('CardsNew\Idea_-_Stew.png')
card61 = pygame.image.load('CardsNew\Idea_-_Stick.png')
card62 = pygame.image.load('CardsNew\Idea_-_Stove.png')
card63 = pygame.image.load('CardsNew\Idea_-_Sword.png')
card64 = pygame.image.load('CardsNew\Idea_-_Temple.png')
card65 = pygame.image.load('CardsNew\Idea_-_Warehouse.png')
card66 = pygame.image.load('CardsNew\Iron_Bar.png')
card67 = pygame.image.load('CardsNew\Iron_Deposit.png')
card68 = pygame.image.load('CardsNew\Iron_Ore.png')
card69 = pygame.image.load('CardsNew\Key.png')
card70 = pygame.image.load('CardsNew\Lumber_Camp.png')
card71 = pygame.image.load('CardsNew\Map.png')
card72 = pygame.image.load('CardsNew\Market.png')
card73 = pygame.image.load('CardsNew\Militia.png')
card74 = pygame.image.load('CardsNew\Milk.png')
card75 = pygame.image.load('CardsNew\Milkshake.png')
card76 = pygame.image.load('CardsNew\Mine.png')
card77 = pygame.image.load('CardsNew\Mountain.png')
card78 = pygame.image.load('CardsNew\Mushroom.png')
card79 = pygame.image.load('CardsNew\Old_Tome.png')
card80 = pygame.image.load('CardsNew\Old_Village.png')
card81 = pygame.image.load('CardsNew\Omelette.png')
card82 = pygame.image.load('CardsNew\Onion.png')
card83 = pygame.image.load('CardsNew\Plains.png')
card84 = pygame.image.load('CardsNew\Plank.png')
card85 = pygame.image.load('CardsNew\Poop.png')
card86 = pygame.image.load('CardsNew\Potato.png')
card87 = pygame.image.load('CardsNew\Quarry.png')
card88 = pygame.image.load('CardsNew\Rabbit.png')
card89 = pygame.image.load('CardsNew\Rat.png')
card90 = pygame.image.load('CardsNew\Raw_Meat.png')
card91 = pygame.image.load('CardsNew\Rock.png')
card92 = pygame.image.load('CardsNew\Sawmill.png')
card93 = pygame.image.load('CardsNew\Shed.png')
card94 = pygame.image.load('CardsNew\Skeleton.png')
card95 = pygame.image.load('CardsNew\Slime.png')
card96 = pygame.image.load('CardsNew\Small_Slime.png')
card97 = pygame.image.load('CardsNew\Smelter.png')
card98 = pygame.image.load('CardsNew\Soil.png')
card99 = pygame.image.load('CardsNew\Spear.png')
card100 = pygame.image.load('CardsNew\Stew.png')
card101 = pygame.image.load('CardsNew\Stick.png')
card102 = pygame.image.load('CardsNew\Stone.png')
card103 = pygame.image.load('CardsNew\Stove.png')
card104 = pygame.image.load('CardsNew\Strange_Portal.png')
card105 = pygame.image.load('CardsNew\Sword.png')
card106 = pygame.image.load('CardsNew\Swordsman.png')
card107 = pygame.image.load('CardsNew\Temple.png')
card108 = pygame.image.load('CardsNew\Travelling_Cart.png')
card109 = pygame.image.load('CardsNew\Treasure_Chest.png')
card110 = pygame.image.load('CardsNew\Tree.png')
card111 = pygame.image.load('CardsNew\Villager.png')
card112 = pygame.image.load('CardsNew\Warehouse.png')
card113 = pygame.image.load('CardsNew\Wolf.png')
card114 = pygame.image.load('CardsNew\Wood.png')

file = open("GameStory/Cards.dat", "r")
g = file.read()
if g.isdigit() == True:
    maxCards = int(g)
    if maxCards > 114:
        maxCards = 114
else:
    print('FileError 0.3 Пожалуйста используйте цифры в файле cards')
    running = False
file.close()   


collectionCard = pygame.sprite.Sprite() 

z = 0
if maxCards == 0:        
    maxZ = random.randint(0,maxCards)
else:
    maxZ = random.randint(1,maxCards)
textZ = ''
cardSkin = ''

while z < maxZ + 1:
    if maxZ == z:
        textZ = z
    z += 1   
allCards = [card0, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30, card31, card32, card33, card34, card35, card36, card37, card38, card39, card40, card41, card42, card43, card44, card45, card46, card47, card48, card49, card50, card51, card52, card53, card54, card55, card56, card57, card58, card59, card60, card61, card62, card63, card64, card65, card66, card67, card68, card69, card70, card71, card72, card73, card74, card75, card76, card77, card78, card79, card80, card81, card82, card83, card84, card85, card86, card87, card88, card89, card90, card91, card92, card93, card94, card95, card96, card97, card98, card99, card100, card101, card102, card103, card104, card105, card106, card107, card108, card109, card110, card111, card112, card113, card114]
i = 0
while i < maxZ + 1:
    if textZ == i:
        collectionCard = allCards[i]
    i += 1

collectionCard_rect = collectionCard.get_rect()
collectionCard_rect.x = 460
collectionCard_rect.y = 300

copAsteroidHelp = pygame.sprite.Sprite()
copAsteroidHelp = pygame.image.load('copperHelp.png')
copAsteroidHelp_rect = copAsteroidHelp.get_rect()
copAsteroidHelp = pygame.transform.scale(copAsteroidHelp, (150,150))
copAsteroidHelp_rect.x = 650
copAsteroidHelp_rect.y = 390

doEnemiesSpawn2 = True

textWork = False

textButton = pygame.sprite.Sprite()
textButton = pygame.image.load('textButtonOff.png')
textButton_rect = textButton.get_rect()
textButton = pygame.transform.scale(textButton, (1200,100))
textButton_rect.x = 0
textButton_rect.y = 580

textCom = ''
textForPrint = 'Hello World!'
textForPrintTimer = 0
commandEntered = False

clock = pygame.time.Clock()
while running:
    events = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            if haveMoney == False:
                file = open("GameStory/Money.dat", "w") 
                file.write(str(money))
                file.close()
            running = False
        if menuOpen == False:
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_RETURN]:
                    commandEntered = True
                    textWork = False
                if keys[pygame.K_BACKSPACE]:
                    l = len(textCom)
                    textCom = textCom[:l-1]
                if not keys[pygame.K_ESCAPE]:
                    if not keys[pygame.K_BACKSPACE]:
                        if not keys[pygame.K_RETURN]:
                            if textWork == True and commandEntered == False:
                                textCom += event.unicode
    gameTimer += 0.01
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseClick = True
        clicked = event.button
    else:
        mouseClick = False
    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    if menuOpen == False:
        keys = pygame.key.get_pressed()
        surface = pygame.display.get_surface()
        x,y = size = surface.get_width(), surface.get_height()
        new_Bg_Size = (x,y)
        bg = pygame.transform.scale(bg, new_Bg_Size)
        if textWork == False:
            if keys[pygame.K_w]:
                angle = 0
                speedY -= 1
                if player_rect.y < -50:
                    player_rect.y = y
            if keys[pygame.K_s]:
                angle = 180
                speedY += 1
                if player_rect.y > y:
                    player_rect.y = -50
            if keys[pygame.K_a]:
                angle = 90
                speedX -= 1
                if player_rect.x < -50:
                    player_rect.x = x
            if keys[pygame.K_d]:
                angle = -90
                speedX += 1
                if player_rect.x > x:
                    player_rect.x = -50
            if keys[pygame.K_q]:
                angle2 += 3
            if keys[pygame.K_e]:
                angle2 -= 3
            if keys[pygame.K_LCTRL]:
                lastCursor = 1
            if keys[pygame.K_LSHIFT]:
                lastCursor = 2
            if keys[pygame.K_CAPSLOCK]:
                lastCursor = 3
            if keys[pygame.K_SPACE]:
                if attackTimerPlayer1 < 1:
                    if equipment == 1:
                        Bullet(angle, angle2, gun_rect)
                        attackTimerPlayer1 = 15
                    if equipment == 2:
                        HealBullet(angle, angle2, gun_rect)
                        attackTimerPlayer1 = 25
                    if equipment == 3:
                        Bullet2(angle, angle2, gun_rect, False)
                        attackTimerPlayer1 = 65
            if keys[pygame.K_p] and reloadPhotoMode < 1:
                    reloadPhotoMode = 15
                    if photoMode == False:
                        photoMode = True
                    else:
                        photoMode = False
            if doCheatWork == True:
                if keys[pygame.K_z]:
                    copper += 100
                if keys[pygame.K_x]:
                    led += 100
                if keys[pygame.K_c]:
                    waveTimer = 0
                if keys[pygame.K_v]:
                    if destroyTimer < 1:
                        if destroyAll == False:
                            destroyAll = True
                            destroyTimer = 15
                        else:
                            destroyAll = False
                            destroyTimer = 15
                if keys[pygame.K_b]:
                    shipHelpTimer = 0
                if keys[pygame.K_n]:
                    thorium += 100
                if keys[pygame.K_m]:
                    if createTimer < 1:
                        cheatWalls(blocks)
                        createTimer = 15
                if keys[pygame.K_F1]:
                    building(30, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, HelpTower, blocks)
            if keys[pygame.K_ESCAPE] and reloadEscMode < 1:
                reloadEscMode = 15
                if console == False:
                    console = True
                else:
                    console = False
        
        reloadEscMode -= 1
        
        if console == True and commandEntered == True:
            if textCom == '/quit':
                running = False
                if langRus == True:
                    textForPrint = 'Удачи!'
                else:
                    textForPrint = 'Good Luck!'
            else:
                if textCom == '/back':
                    reloadEscMode = 15
                    console = False
                    textComEntered = False
                    if langRus == True:
                        textForPrint = 'Вы вышли из функции!'
                    else:
                        textForPrint = 'You have exited the function!'
                else:
                    if textCom == '/cheatOff':
                        doCheatWork = False
                        if langRus == True:
                            textForPrint = 'Читы отключены!'
                        else:
                            textForPrint = 'Cheat off!'
                    else:
                        if textCom == '/clearResourses':
                            copper = 0
                            led = 0
                            thorium = 0
                            hlak = 0
                            water = 0
                            oil = 0
                            graphite = 0
                            if langRus == True:
                                textForPrint = 'Ресурсы очищены!'
                            else:
                                textForPrint = 'Resourses cleared!'
                        else:
                            if textCom == '/reloadTextures':
                                planetRealm = pygame.image.load('planetRealm.jpg')
                                bg1 = pygame.image.load('bg.jpg')
                                blackHole = pygame.image.load('blackHole.jpg')
                                bg2 = pygame.image.load('bg2.jpg')
                                planetEarth = pygame.image.load('planetEarth.jpg')
                                bg3 = pygame.image.load('bg3.jpg')
                                planetLuck = pygame.image.load('planetLuck.jpg')
                                bg4 = pygame.image.load('bg4.jpg')
                                planetUranius = pygame.image.load('planetUranius.jpg')
                                bg5 = pygame.image.load('bg5.jpg')
                                bulletImg2 = pygame.image.load('bullet2.png')
                                bulletImg3 = pygame.image.load('healBullet.png')
                                rubble_1_0 = pygame.image.load('rubble-1-0.png')
                                rubble_1_1 = pygame.image.load('rubble-1-1.png')
                                rubble_2_0 = pygame.image.load('rubble-2-0.png')
                                rubble_2_1 = pygame.image.load('rubble-2-1.png')
                                rubble_3_0 = pygame.image.load('rubble-3-0.png')
                                rubble_4_0 = pygame.image.load('rubble-4-0.png')
                                rubble_5_0 = pygame.image.load('rubble-5-0.png')
                                rubble_6_0 = pygame.image.load('rubble-6-0.png')
                                rubble_7_0 = pygame.image.load('rubble-7-0.png')
                                rubble_8_0 = pygame.image.load('rubble-8-0.png')
                                imgWallDmg = pygame.image.load('wall.png')
                                imgWallDmg2 = pygame.image.load('wall2.png')
                                imgWallDmg3 = pygame.image.load('wall3.png')
                                comCenterImg1 = pygame.image.load('spawn.png')
                                comCenterImg2 = pygame.image.load('spawn2.png')
                                comCenterImg3 = pygame.image.load('spawn3.png')
                                comCenterImg4 = pygame.image.load('spawn4.png')
                                comCenterImg5 = pygame.image.load('spawn5.png')
                                comCenterImg6 = pygame.image.load('spawn6.png')
                                cursorImg = pygame.image.load('cursor.png')
                                cursorHand = pygame.image.load('hand.png')
                                cursorH = pygame.image.load('cursorH.png')
                                cursorH2 = pygame.image.load('cursorH2.png')
                                cursorDrill = pygame.image.load('drill.png')
                                dialog1 = pygame.image.load('dialog1.png')
                                dialog2 = pygame.image.load('dialog2.png')
                                dialog3 = pygame.image.load('dialog3.png')
                                dialog4 = pygame.image.load('dialog4.png')
                                dialog5 = pygame.image.load('dialog5.png')
                                dialog6 = pygame.image.load('dialog6.png')
                                dialog1E = pygame.image.load('dialog1Eng.png')
                                dialog2E = pygame.image.load('dialog2Eng.png')
                                dialog3E = pygame.image.load('dialog3Eng.png')
                                dialog4E = pygame.image.load('dialog4Eng.png')
                                dialog5E = pygame.image.load('dialog5Eng.png')
                                dialog6E = pygame.image.load('dialog6Eng.png')
                                shopOn = pygame.image.load('shopOn.png')
                                shopOff = pygame.image.load('shopOff.png')
                                hardModeOn = pygame.image.load('hardModeOn.png')
                                hardModeOff = pygame.image.load('hardModeOff.png')
                                soundOn = pygame.image.load('soundOn.png')
                                soundOff = pygame.image.load('soundOff.png')
                                airdropOn = pygame.image.load('airdropsOn.png')
                                airdropOff = pygame.image.load('airdropsOff.png')
                                cheatOn = pygame.image.load('cheatModOn.png')
                                cheatOff = pygame.image.load('cheatModOff.png')
                                dlcOn = pygame.image.load('dlcOn.png')
                                dlcOff = pygame.image.load('dlcOff.png')
                                fogOn = pygame.image.load('fogOn.png')
                                fogOff = pygame.image.load('fogOff.png')
                                randomSkinOn = pygame.image.load('randomSkinOn.png')
                                randomSkinOff = pygame.image.load('randomSkinOff.png')
                                tutorialOn = pygame.image.load('tutorialOn.png')
                                tutorialOff = pygame.image.load('tutorialOff.png')
                                unlimitedHpOn = pygame.image.load('unlimitedHpOn.png')
                                unlimitedHpOff = pygame.image.load('unlimitedHpOff.png')
                                unlimitedResOn = pygame.image.load('unlimitedResOn.png')
                                unlimitedResOff = pygame.image.load('unlimitedResOff.png')
                                withEnemyOn = pygame.image.load('withEnemyOn.png')
                                withEnemyOff = pygame.image.load('withEnemyOff.png')
                                cheatModOn = pygame.image.load('cheatModOn.png')
                                cheatModOff = pygame.image.load('cheatModOff.png')
                                testSettingsOn = pygame.image.load('testSettingsOn.png')
                                testSettingsOff = pygame.image.load('testSettingsOff.png')
                                testSettingsOnE = pygame.image.load('testSettingsOnEng.png')
                                testSettingsOffE = pygame.image.load('testSettingsOffEng.png')
                                langRu = pygame.image.load('rusLang.png')
                                langEng = pygame.image.load('engLang.png')
                                equipmentBullet = pygame.image.load('equipmentBullet.png')
                                equipmentBullet2 = pygame.image.load('equipmentBullet2.png')
                                equipmentBigBullet = pygame.image.load('equipmentBigBullet.png')
                                equipmentBigBullet2 = pygame.image.load('equipmentBigBullet2.png')
                                equipmentHealBullet = pygame.image.load('equipmentHealBullet.png')
                                equipmentHealBullet2 = pygame.image.load('equipmentHealBullet2.png')
                                helpCheat = pygame.image.load('cheat.png')
                                helpCheatE = pygame.image.load('cheatEng.png')
                                escHelpT = pygame.image.load('escHelp.png')
                                escHelpTE = pygame.image.load('escHelpEng.png')
                                buttonL= pygame.image.load('buttonLose.png')
                                buttonW = pygame.image.load('buttonWin.png')
                                buttonR = pygame.image.load('buttonRestart.png')
                                buttonLE= pygame.image.load('buttonLoseEng.png')
                                buttonWE = pygame.image.load('buttonWinEng.png')
                                buttonRE = pygame.image.load('buttonRestartEng.png')
                                load = pygame.image.load('loading.jpg')
                                loadE = pygame.image.load('loadingEng.png')
                                if langRus == True:
                                    textForPrint = 'Текстуры обновлены!'
                                else:
                                    textForPrint = 'Texstures updated!'
                            else:
                                if textCom == '/returnToBaze':
                                    file = open("GameStory/Cards.dat", "w") 
                                    file.write(str(0))
                                    file.close()
                                    file = open("GameStory/Money.dat", "w") 
                                    file.write(str(0))
                                    file.close()
                                    file = open("GameStory/doNotChange.dat", "w") 
                                    file.write('False')
                                    file.close()
                                    reloadEscMode = 15
                                    money = 0
                                    reward = 0
                                    maxCards = 0
                                    secretBool = False
                                    running = False
                                    if langRus == True:
                                        textForPrint = 'Всё возвращено к базовым настройкам!'
                                    else:
                                        textForPrint = 'All back to baze settings!'
                                else:
                                    if textCom == '/help':
                                        if langRus == True:
                                            textForPrint = 'Помощь предоставлена!'
                                        else:
                                            textForPrint = 'Heelp provided!'
                                        os.system("Commands.txt")
                                    else:
                                        if langRus == True:
                                            textForPrint = 'Неизвестная команда! Попробуйте почитать Commands.txt'
                                        else:
                                            textForPrint = 'Unknown command! Try to read Commands.txt'
            textForPrintTimer = 30
            reloadEscMode = 15
            console = False
            commandEntered = False   
            textWork = False   
            textButton = textButtonOff     
            textButton = pygame.transform.scale(textButton, (1200, 100))
            textCom = ''

        if dlcWork == True:
            if hardMode == True:
                res = copper + led + thorium + graphite + water + oil + hlak
                maxFull = 411094
                oneProcent = maxFull / 100
                procentFull = res / oneProcent
            else:
                res = copper + led + graphite + water + oil + hlak
                maxFull = 311095
                oneProcent = maxFull / 100
                procentFull = res / oneProcent
        else:
            if hardMode == True:
                res = copper + led + thorium 
                maxFull = 299997
                oneProcent = maxFull / 100
                procentFull = res / oneProcent
            else:
                res = copper + led
                maxFull = 199998
                oneProcent = maxFull / 100
                procentFull = res / oneProcent

        if round(procentFull, 1) > 99.9:
            full = full_100
        if round(procentFull, 1) > 79.9 and round(procentFull, 1) < 100:
            full = full_80
        if round(procentFull, 1) > 59.9 and round(procentFull, 1) < 80:
            full = full_60
        if round(procentFull, 1) > 39.9 and round(procentFull, 1) < 60:
            full = full_40
        if round(procentFull, 1) > 19.9 and round(procentFull, 1) < 40:
            full = full_20
        if round(procentFull, 1) < 20:
            full = full_0

        reloadPhotoMode = timerDown(reloadPhotoMode,1)

        if tutorialWork == True:
            dialogTimer = timerDown(dialogTimer,1)
            if dialogNumber == 1:
                if langRus == True:
                    dialog = dialog1
                else:
                    dialog = dialog1E
                doEnemiesSpawn = False
                if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
                    if dialogTimer < 1:
                        dialogTimer = 30
                        dialogNumber += 1
            if dialogNumber == 2:
                if langRus == True:
                    dialog = dialog2
                else:
                    dialog = dialog2E
                doEnemiesSpawn = False
                if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
                    if dialogTimer < 1:
                        dialogTimer = 30
                        dialogNumber += 1
            if dialogNumber == 3:
                if langRus == True:
                    dialog = dialog3
                else:
                    dialog = dialog3E
                doEnemiesSpawn = False
                screen.blit(copAsteroidHelp, copAsteroidHelp_rect)
                if copper > 99.9:
                    dialogTimer = 30
                    dialogNumber += 1
            if dialogNumber == 4:
                if langRus == True:
                    dialog = dialog4
                else:
                    dialog = dialog4E
                doEnemiesSpawn = False
                if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
                    if dialogTimer < 1 and dialogWallStay == True:
                        dialogTimer = 30
                        dialogNumber += 1
            if dialogNumber == 5:
                if langRus == True:
                    dialog = dialog5
                else:
                    dialog = dialog5E
                doEnemiesSpawn = True
                waveTimer = 0
                if wave == 1:
                    dialogTimer = 30
                    dialogNumber += 1
                    copper += 99999
                    led += 99999
                    thorium += 99999
            if dialogNumber == 6:
                if langRus == True:
                    dialog = dialog6
                else:
                    dialog = dialog6E
                doEnemiesSpawn = False
                if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
                    if dialogTimer < 1:
                        dialogTimer = 30
                        dialogNumber += 1
            
        destroyTimer = timerDown(destroyTimer,1)

        if selectedPlanet == 5 and dlcWork == False:
            selectedPlanet = 3
            map = planetEarth
            bg = bg3

        if waveTimer < 0.1:
            if doEnemiesSpawn == True:
                if secretBool == True:
                    if wave == 50 + i:
                        ExclusiveEnemy(enemies3)
                        i += 50
                    if selectedPlanet == 1:
                        Enemy(enemies)  
                    if selectedPlanet == 2:
                        Enemy(enemies) 
                        Enemy2(enemies2)  
                        if dlcWork == True:
                            randomChanse = random.randint(0,100)
                            if randomChanse == 1:
                                EnemyDlc(enemies4)
                    if selectedPlanet == 3:
                        Enemy(enemies) 
                        Enemy3(enemies3)  
                    if selectedPlanet == 4:
                        randomEnemy = random.randint(0,4)
                        randomEnemy2 = random.randint(0,4)
                        if dlcWork == True:
                            randomChanse = random.randint(0,100)
                            if randomChanse == 1:
                                EnemyDlc(enemies4)
                        if hardMode == False:
                            if randomEnemy == 1:
                                Enemy(enemies) 
                            if randomEnemy == 2:
                                Enemy2(enemies2) 
                            if randomEnemy == 3:
                                Enemy3(enemies3)  
                            if randomEnemy == 4:
                                Enemy4(enemies4)
                            if randomEnemy2 == 1:
                                Enemy(enemies) 
                            if randomEnemy2 == 2:
                                Enemy2(enemies2) 
                            if randomEnemy2 == 3:
                                Enemy3(enemies3)  
                            if randomEnemy2 == 4:
                                Enemy4(enemies4)  
                        else:
                            Enemy(enemies) 
                            Enemy2(enemies2) 
                            Enemy3(enemies3)  
                            Enemy4(enemies4)
                    if selectedPlanet == 5:
                        randomChanse = random.randint(0,50)
                        if randomChanse == 1:
                            EnemyDlc(enemies4)
                        Enemy(enemies) 
                        Enemy2(enemies2) 
                        Enemy3(enemies3)  
                        Enemy4(enemies4)
                else:
                    if dlcWork == True:
                        randomChanse = random.randint(0,10)
                        if randomChanse == 1:
                            EnemyDlc(enemies4)
                    if hardMode == True:
                        randomChanse = random.randint(0,10)
                        if randomChanse == 1:
                            ExclusiveEnemy(enemies3)
                    Enemy(enemies) 
                    Enemy2(enemies2) 
                    Enemy3(enemies3)  
                    Enemy4(enemies4)
            waweTimerSmall = wave / 2
            if hardMode == False:
                if waweTimerSmall > 80:
                    waweTimerSmall = 80
            else:
                if waweTimerSmall > 50:
                    waweTimerSmall = 50
            if hardMode == False:
                waveTimer = 100 - waweTimerSmall
            if hardMode == True:
                waveTimer = 50 - waweTimerSmall
            if tutorialWork == False:
                wave += 1
            if tutorialWork == True and dialogWallStay == True and dialogNumber == 5 and wave == 0:
                wave += 1

        if comCenterHP > 250:
            comCenter = comCenterImg1
            comCenter = pygame.transform.scale(comCenter, (80,80))
        if comCenterHP > 200 and comCenterHP < 251:
            comCenter = comCenterImg2
            comCenter = pygame.transform.scale(comCenter, (80,80))
        if comCenterHP > 150 and comCenterHP < 201:
            comCenter = comCenterImg3
            comCenter = pygame.transform.scale(comCenter, (80,80))
        if comCenterHP > 100 and comCenterHP < 151:
            comCenter = comCenterImg4
            comCenter = pygame.transform.scale(comCenter, (80,80))
        if comCenterHP > 50 and comCenterHP < 101:
            comCenter = comCenterImg5
            comCenter = pygame.transform.scale(comCenter, (80,80))
        if comCenterHP < 51:
            comCenter = comCenterImg6
            comCenter = pygame.transform.scale(comCenter, (80,80))

        shipHelpTimer = timerDown(shipHelpTimer,1)
        waveTimer = timerDown(waveTimer,0.1)
        attackTimerPlayer1 = timerDown(attackTimerPlayer1,1)
        attackTimerPlayer2 = timerDown(attackTimerPlayer2,1)

        if Mouse_x > 650 and Mouse_x < 730 and Mouse_y > 390 and Mouse_y < 470:
            if  mouseClick == True and clicked == 1:
                copper += 0.1
        if Mouse_x > 350 and Mouse_x < 430 and Mouse_y > 190 and Mouse_y < 270:
            if mouseClick == True and clicked == 1:
                led += 0.1

        if comCenterHP > 0:
            if Mouse_x > 350 and Mouse_x < 430 and Mouse_y > 190 and Mouse_y < 270 or Mouse_x > 650 and Mouse_x < 730 and Mouse_y > 390 and Mouse_y < 470:
                customM = cursorDrill
            else:
                if lastCursor == 1:
                    customM = cursorImg
                if lastCursor == 2:
                    customM = cursorH
                if lastCursor == 3:
                    customM = cursorH2          
        else:
            customM = cursorImg

        customM_rect.x = Mouse_x
        customM_rect.y = Mouse_y

        pygame.mouse.set_visible(False)

        rotator_rotated = pygame.transform.rotate(rotator, rotAngle)
        rotator_rotated_rect = rotator_rotated.get_rect(center=drill_rect.center)

        if keys[pygame.K_1]:
            building(15, 30, 10, 0, 0, 0, 20, 0, 0, 0, 0, Walls, blocks)
        if keys[pygame.K_2]:
            building(35, 70, 50, 20, 0, 0, 100, 40, 50, 0, 0, TowerSpawn, towerSpawns)
        if keys[pygame.K_3]:
            if mouseClick == True and clicked == 1:
                drill_rect.x = Mouse_x
                drill_rect.y = Mouse_y
        if keys[pygame.K_4]:
            building(24, 48, 100, 50, 0, 0, 200, 100, 50, 0, 0, Tower, blocks)
        if keys[pygame.K_5]:
            building(45, 90, 300, 250, 0, 0, 600, 500, 0, 0, 0, Escape, blocks)
        if keys[pygame.K_6]:
            building(24, 48, 215, 215, 0, 0, 430, 430, 50, 0, 0, Tower2, blocks)
        if keys[pygame.K_7]:
            building(25, 50, 20, 0, 0, 0, 40, 0, 0, 0, 0, BigWalls, blocks)
        if hardMode == True:
            if keys[pygame.K_8]:
                building(0, 50, 0, 0, 0, 0, 0, 0, 40, 0, 0, BigTorium, blocks)
        if hardMode == True:
            if keys[pygame.K_9]:
                building(0, 48, 0, 0, 0, 0, 300, 300, 100, 0, 0, ExtraDrill, blocks)
        if hardMode == True:
            if keys[pygame.K_0]:
                building(0, 48, 0, 0, 0, 0, 800, 800, 300, 0, 0, Tower3, blocks)
        if dlcWork == True:
            if keys[pygame.K_KP_0]:
                building(24, 48, 50, 50, 0, 0, 100, 100, 50, 0, 0, Extractor, blocks)
            if keys[pygame.K_KP_1]:
                building(10, 15, 25, 25, 0, 5, 50, 50, 25, 0, 10, Mine, blocks)
            if keys[pygame.K_KP_2]:
                building(10, 15, 50, 50, 0, 10, 100, 100, 50, 0, 20, Press, blocks)
            if keys[pygame.K_KP_3]:
                building(10, 15, 50, 50, 0, 5, 100, 100, 50, 0, 10, WaterExtractor, blocks)
            if keys[pygame.K_KP_4]:
                building(10, 15, 250, 250, 0, 50, 500, 500, 250, 0, 100, Tower4, blocks)
            if keys[pygame.K_KP_5]:
                building(10, 15, 50, 50, 0, 15, 100, 100, 50, 0, 30, Mixer, blocks)
            if keys[pygame.K_KP_6]:
                if limitTower == False:
                    building(105, 75, 1000, 1000, 50, 300, 2000, 2000, 1000, 100, 600, Tower5, blocks)
            if keys[pygame.K_KP_7]:
                building(30, 60, 75, 75, 25, 5, 150, 150, 25, 50, 10, ForceProjector, blocks)
            if keys[pygame.K_KP_8]:
                building(30, 60, 500, 500, 25, 25, 1000, 1000, 500, 50, 50, ResGenerator, blocks)
            if keys[pygame.K_KP_9]:
                building(30, 60, 300, 300, 25, 25, 300, 300, 150, 50, 50, Tower6, blocks)

        rotator_rect.y = drill_rect.y + 8
        rotator_rect.x = drill_rect.x + 8

        rotAngle += rotSpeed
        rotAngle = rotAngle % 360
        if rotSpeed > 0:
            drillSpeed / rotSpeed

        if drillTimer < 1:
            if drill_rect.colliderect(copAsteroid_rect):
                if copper < 99999:
                    if dlc == True:
                        copper += 0.1 * water * rotSpeed / 2
                    else:
                        copper += 0.1 * rotSpeed / 2
                drillTimer = drillSpeed
            if drill_rect.colliderect(ledAsteroid_rect):
                if led < 99999:
                    if dlc == True:
                        led += 0.1 * water * rotSpeed / 2
                    else:
                        led += 0.1 * rotSpeed / 2
                drillTimer = drillSpeed
            if hardMode == True:
                if drill_rect.colliderect(thoriumAsteroid_rect):
                    if thorium < 99999:
                        if dlc == True:
                            thorium += 0.1 * water * rotSpeed / 2
                        else:
                            thorium += 0.1 * rotSpeed / 2
                    drillTimer = drillSpeed
            if drill_rect.colliderect(copAsteroid_rect) or drill_rect.colliderect(ledAsteroid_rect) or drill_rect.colliderect(thoriumAsteroid_rect):
                rotSpeed += 0.1
            else:
                rotSpeed -= 0.1

        if rotSpeed > 5:
            rotSpeed = 5
        if rotSpeed < 0:
            rotSpeed = 0

        createTimer = timerDown(createTimer,1)
        drillTimer = timerDown(drillTimer,1)

        if gameMode == 'Coop' and textWork == False:
            if keys[pygame.K_i]:
                angle3 = 0
                speedY2 -= 1
                if player2_rect.y < -50:
                    player2_rect.y = y
            if keys[pygame.K_k]:
                angle3 = 180
                speedY2 += 1
                if player2_rect.y > y:
                    player2_rect.y = -50
            if keys[pygame.K_j]:
                angle3 = 90
                speedX2 -= 1
                if player2_rect.x < -50:
                    player2_rect.x = x
            if keys[pygame.K_l]:
                angle3 = -90
                speedX2 += 1
                if player2_rect.x > x:
                    player2_rect.x = -50
            if keys[pygame.K_u]:
                angle4 += 3
            if keys[pygame.K_o]:
                angle4 -= 3
            if keys[pygame.K_RALT]:
                if attackTimerPlayer2 < 1:
                    if equipment == 1:
                        attackTimerPlayer2 = 65
                        Bullet2(angle3, angle4, gun2_rect, False)
                    if equipment == 2:
                        attackTimerPlayer2 = 25
                        Bullet(angle3, angle4, gun2_rect)
                    if equipment == 3:
                        attackTimerPlayer2 = 15   
                        HealBullet(angle3, angle4, gun2_rect)   

        if speedX < -0:
            speedX += 0.2
        if speedX > 0.2:
            speedX -= 0.2
        if speedY < 0:
            speedY += 0.2
        if speedY > 0.2:
            speedY -= 0.2 

        speedX, speedY = maxSpeed(speedX, speedY, 5, 5)

        if speedX2 < -0:
            speedX2 += 0.2
        if speedX2 > 0.2:
            speedX2 -= 0.2
        if speedY2 < 0:
            speedY2 += 0.2
        if speedY2 > 0.2:
            speedY2 -= 0.2 

        speedX2, speedY2 = maxSpeed(speedX2, speedY2, 5, 5)

        copper = round(copper, 1)
        led = round(led, 1)
        thorium = round(thorium, 1)
        hlak = round(hlak, 1)
        water = round(water, 3)
        oil = round(oil, 3)
        graphite = round(graphite, 1)
        text = Font1.render(str(copper), True, (255, 255, 255))
        text2 = Font1.render(str(led), True, (255, 255, 255))
        text3 = Font1.render(str(thorium), True, (255, 255, 255))
        text4 = Font1.render(str(hlak), True, (255, 255, 255))
        text5 = Font1.render(str(water), True, (255, 255, 255))
        text6 = Font1.render(str(oil), True, (255, 255, 255))
        text7 = Font1.render(str(graphite), True, (255, 255, 255))
        textComSee = Font1.render(str(textCom), True, (255, 255, 255))
        if langRus == True:
            textPrint = Font2.render('Отчёт: ' + str(textForPrint), True, (255, 255, 255))
        else:
            textPrint = Font2.render('Report: ' + str(textForPrint), True, (255, 255, 255))

        player_rect.x += speedX
        player_rect.y += speedY
        player2_rect.x += speedX2
        player2_rect.y += speedY2

        gun_rect.x = player_rect.x + 16
        gun_rect.y = player_rect.y - 5
        gun2_rect.x = player2_rect.x + 16
        gun2_rect.y = player2_rect.y - 5

        player_rotated = pygame.transform.rotate(player, angle)
        player_rotated_rect = player_rotated.get_rect(center=player_rect.center)

        angle2 = angle2 % 360 

        gun_rotated = pygame.transform.rotate(gun, angle2 + angle)
        gun_rotated_rect = gun_rotated.get_rect(center=player_rect.center)

        player2_rotated = pygame.transform.rotate(player2, angle3)
        player2_rotated_rect = player2_rotated.get_rect(center=player2_rect.center)

        angle3 = angle3 % 360 

        gun2_rotated = pygame.transform.rotate(gun2, angle4 + angle3)
        gun2_rotated_rect = gun2_rotated.get_rect(center=player2_rect.center)

        bullets.draw(screen)
        bigBullets.draw(screen)

        if not textForPrint == 'Hello World!':
            textForPrintTimer -= 0.1
        if dlcWork == True:
            hlak += 0.25
            water += 0.001

        if fogWork == True:
            if selectedPlanet == 4:
                fog_rect.x -= 1
                if fog_rect.x < -1200:
                    fog_rect.x = 1198
                fog2_rect.x -= 1
                if fog2_rect.x < -1200:
                    fog2_rect.x = 1198

        if copper > 99999:
            copper = 99999
        if led > 99999:
            led = 99999
        if thorium > 99999:
            thorium = 99999
        if dlcWork == True:
            if water > 100:
                water = 100
            if hlak > 999:
                hlak = 999
            if oil > 9999:
                oil = 9999
            if graphite > 99999:
                graphite = 99999

        if comCenterHP < 1:
            pygame.mixer.stop()
            bang.play()
            screen.blit(go, go_rect)
            screen.blit(buttonLose, buttonLose_rect)
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 100 and Mouse_y < 250:
                customM = cursorHand
            screen.blit(buttonRestart, buttonRestart_rect)
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 260 and Mouse_y < 410:
                customM = cursorHand
            screen.blit(customM, customM_rect)
            file = open("GameStory/Game.txt", "w")
            gameTimer = round(gameTimer)
            file.write("Спасибо за игру! Вы получили плохую концовку. Ваша база была полностью уничтожена! Врагов уничтожено: " + str(destroyedEnemies) + ". Пережито волн: " + str(wave) + ". Проведено секунд в космосе: " + str(gameTimer))
            file.close()    
            otherTimer -= 1
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 100 and Mouse_y < 250:
                customM = cursorHand
                if mouseClick == True and clicked == 1 and otherTimer < 1:
                    running = False
                    click.play()
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 260 and Mouse_y < 410:
                customM = cursorHand
                if mouseClick == True and clicked == 1 and otherTimer < 1:
                    restart()
                    click.play()
        if canEscape == True and secretBool == True:
            storeActivated == False
            pygame.mixer.stop()
            screen.blit(es, es_rect)
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 100 and Mouse_y < 250:
                customM = cursorHand
            screen.blit(buttonRestart, buttonRestart_rect)
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 260 and Mouse_y < 410:
                customM = cursorHand
            screen.blit(customM, customM_rect)
            screen.blit(buttonWin, buttonWin_rect)
            file = open("GameStory/Game.txt", "w")
            gameTimer = round(gameTimer)
            file.write("Спасибо за игру! Вы получили хорошую концовку. Вы победили! Врагов уничтожено: " + str(destroyedEnemies) + ". Пережито волн: " + str(wave) + ". Проведено секунд в космосе: " + str(gameTimer))
            file.close() 
            otherTimer -= 1 
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 260 and Mouse_y < 410:
                customM = cursorHand
                if mouseClick == True and clicked == 1 and otherTimer < 1:
                    restart()
                    file = open("GameStory/Cards.dat", "w") 
                    file.write(str(maxCards + 1))
                    maxCards += 1
                    file.close()
                    click.play()
            file = open("GameStory/Money.dat", "w") 
            if haveMoney == False:
                reward += 0
                if doCheatWork == False and unlMode == False and doUnlHp == False:
                    if tutorialWork == False:
                        if hardMode == True:
                            if dlcWork == True:
                                reward += 200
                            else:
                                reward += 155
                        else:
                            if dlcWork == True:
                                reward += 100
                            else:
                                reward += 50
                    else:
                        reward += 5
            yourCoins = money + reward
            file.write(str(yourCoins))
            file.close()
            haveMoney = True
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 100 and Mouse_y < 250:
                customM = cursorHand
                if mouseClick == True and clicked == 1 and otherTimer < 1:
                    if doCheatWork == False and unlMode == False and doUnlHp == False:
                        file = open("GameStory/Cards.dat", "w") 
                        file.write(str(maxCards + 1))
                        maxCards += 1
                        file.close()
                    running = False
                    click.play()
        if canEscape == True and secretBool == False:
            storeActivated == False
            pygame.mixer.stop()
            screen.blit(es, es_rect)
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 100 and Mouse_y < 250:
                customM = cursorHand
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 260 and Mouse_y < 410:
                customM = cursorHand
            screen.blit(customM, customM_rect)
            screen.blit(buttonWin, buttonWin_rect)
            screen.blit(buttonRestart, buttonRestart_rect)
            file = open("GameStory/Game.txt", "w")
            gameTimer = round(gameTimer)
            file.write("Спасибо за игру! Вы получили секретную концовку!!! Не знаю как у вас это получилось, но это круто! Врагов уничтожено: " + str(destroyedEnemies) + ". Пережито волн: " + str(wave) + ". Проведено секунд в космосе: " + str(gameTimer))
            file.close()  
            otherTimer -= 1
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 260 and Mouse_y < 410:
                customM = cursorHand
                if mouseClick == True and clicked == 1 and otherTimer < 1:
                    restart()
                    click.play()
                    file = open("GameStory/Cards.dat", "w") 
                    file.write(str(maxCards + 1))
                    maxCards += 1
                    file.close()
            file = open("GameStory/Money.dat", "w") 
            if haveMoney == False:
                reward += 0
                if doCheatWork == False and unlMode == False and doUnlHp == False:
                    if tutorialWork == False:
                        if hardMode == True:
                            if dlcWork == True:
                                reward += 200
                            else:
                                reward += 155
                        else:
                            if dlcWork == True:
                                reward += 100
                            else:
                                reward += 50
                        reward += 100
                    else:
                        reward += 5
            yourCoins = money + reward
            file.write(str(yourCoins))
            file.close()
            haveMoney = True
            if Mouse_x > 440 and Mouse_x < 760 and Mouse_y > 100 and Mouse_y < 250:
                customM = cursorHand
                if mouseClick == True and clicked == 1:
                    if doCheatWork == False and unlMode == False and doUnlHp == False:
                        file = open("GameStory/Cards.dat", "w") 
                        file.write(str(maxCards + 1))
                        maxCards += 1
                        file.close()
                    running = False
                    click.play()

        if Mouse_x > 960 and Mouse_x < 1040 and Mouse_y > 0 and Mouse_y < 80:
            customM = cursorHand
            if mouseClick == True and clicked == 1:
                if shopTimer < 1:
                    if storeActivated == False:
                        shop, shopTimer, storeActivated = ButtonOn(shop, shopOn, 15, storeActivated, 80, 80)
                    else:
                        shop, shopTimer, storeActivated = ButtonOff(shop, shopOff, 15, storeActivated, 80, 80)

        if not canEscape == True and not comCenterHP < 1:
            gameBlit()
            if photoMode == False:
                classesUpdate()
                if copper > 99999:
                    copper = 99999
                if led > 99999:
                    led = 99999
                if thorium > 99999:
                    thorium = 99999
                if dlcWork == True:
                    if water > 100:
                        water = 100
                    if hlak > 999:
                        hlak = 999
                    if oil > 9999:
                        oil = 9999
                    if graphite > 99999:
                        graphite = 99999

            if storeActivated == True and canEscape == False:
                if Mouse_x > 340 and Mouse_x < 436 and Mouse_y > 0 and Mouse_y < 96:
                    customM = cursorHand
                    if mouseClick == True and clicked == 1:
                        if slot1Timer < 1 and money > 14:
                            slot1Timer = 15
                            money -= 15
                            copper += 100
                if Mouse_x > 446 and Mouse_x < 542 and Mouse_y > 0 and Mouse_y < 96:
                    customM = cursorHand
                    if mouseClick == True and clicked == 1:
                        if slot2Timer < 1 and money > 14:
                            slot2Timer = 15
                            money -= 15
                            led += 100
                if hardMode == True:
                    if Mouse_x > 552 and Mouse_x < 648 and Mouse_y > 0 and Mouse_y < 96:
                        customM = cursorHand
                        if mouseClick == True and clicked == 1:
                            if slot3Timer < 1 and money > 39:
                                slot3Timer = 15
                                money -= 40
                                thorium += 100
                if dlcWork == True:
                    if Mouse_x > 658 and Mouse_x < 754 and Mouse_y > 0 and Mouse_y < 96:
                        customM = cursorHand
                        if mouseClick == True and clicked == 1:
                            if slot4Timer < 1 and money > 89:
                                slot4Timer = 15
                                money -= 90
                                graphite += 100
            if Mouse_x > 0 and Mouse_x < 1200 and Mouse_y > 580 and Mouse_y < 680 and console == True and textWork == False:
                customM = cursorHand
                if mouseClick == True and clicked == 1:
                    textWork = True
                    textButton = textButtonOn
                    textButton = pygame.transform.scale(textButton, (1200, 100))
                    commandEntered = False

            
            shopTimer = timerDown(shopTimer,1)
            slot1Timer = timerDown(slot1Timer,1)
            slot2Timer = timerDown(slot2Timer,1)
            slot3Timer = timerDown(slot3Timer,1)
            slot4Timer = timerDown(slot4Timer,1)

        if langRus == True:
            buttonRestart = buttonR
            buttonWin = buttonW
            buttonLose = buttonL
        else:
            buttonRestart = buttonRE
            buttonWin = buttonWE
            buttonLose = buttonLE

        buttonLose = pygame.transform.scale(buttonLose, (320,150))
        buttonRestart = pygame.transform.scale(buttonRestart, (320,150))
        buttonWin = pygame.transform.scale(buttonWin, (320,150))

        if photoMode == False:
            screen.blit(customM, customM_rect)
    else:
        screen.blit(bgM, bgM_rect)
        screen.blit(settingsB, settingsB_rect)
        if settingsOpen == False and infoOpen == False:
            screen.blit(tutorialButton, tutorialButton_rect)
            tutorialButton_rect.x = 600
            tutorialButton_rect.y = 600
        if settingsOpen == True:
            screen.blit(tutorialButton, tutorialButton_rect)
            tutorialButton_rect.x = 280
            tutorialButton_rect.y = 100
        screen.blit(textVersion, (1030, 640))

        if mouseCanClick == False:
            customM = cursorImg     
        else:
            customM = cursorHand
        customM_rect.x = Mouse_x
        customM_rect.y = Mouse_y
        
        mouseCanClick = False

        if Mouse_x > 0 and Mouse_x < 80 and Mouse_y > 600:
            mouseCanClick = True
            if mouseClick == True and clicked == 1 and settingsTimer < 1:
                if settingsOpen == False and settingsTimer < 1:
                    click.play()
                    settingsTimer = 15
                    settingsOpen = True
                    infoOpen = False
                    screen.blit(bgM, bgM_rect)
                if settingsOpen == True and settingsTimer < 1:
                    click.play()
                    settingsTimer = 15
                    settingsOpen = False    
                    screen.blit(bgM, bgM_rect)
        if settingsOpen == True:
            settingsBlit()

        if tutorialWork == True:
            selectedPlanet = 1
            if selectedPlanet == 1:
                map = planetRealm
                bg = bg1
                map = pygame.transform.scale(map, (450,300))

        if Mouse_x > 10 and Mouse_x < 90 and Mouse_y > 10 and Mouse_y < 90:
            if settingsOpen == True:
                mouseCanClick = True
            if mouseClick == True and clicked == 1:
                if settingsOpen == True and hardModeTimer < 1:
                    if hardMode == False:
                        hardModeButton, hardModeTimer, hardMode = ButtonOn(hardModeButton, hardModeOn, 15, hardMode, 80, 80)
                        waveTimer = 50
                        dmgEnemy = 30
                        dmgPlayer = 0.1
                        dmgPlayer2 = 1
                        if unlMode == False:
                            copper, led, thorium, hlak, water, oil, graphite = resourseChange(-100, -100, -50, -100, -10, -30, -100)
                        else:
                            copper, led, thorium, hlak, water, oil, graphite = resourseChange(99999, 99999, 99999, 99999, 99999, 99999, 99999)
                    else:
                        hardModeButton, hardModeTimer, hardMode = ButtonOff(hardModeButton, hardModeOff, 15, hardMode, 80, 80)
                        dmgEnemy = 10
                        dmgPlayer = 1
                        dmgPlayer2 = 0.1
                        waveTimer = 160 
                        if unlMode == False:
                            copper, led, thorium, hlak, water, oil, graphite = resourseChange(10, 0, 0, 0, 0, 0, 0)

        if Mouse_x > 10 and Mouse_x < 90 and Mouse_y > 190 and Mouse_y < 270:
            if settingsOpen == True:
                mouseCanClick = True
            if mouseClick == True and clicked == 1:
                if settingsOpen == True and musicTimer < 1:
                    if musicPlay == False:
                        musicButton, musicTimer, musicPlay = ButtonOn(musicButton, soundOn, 15, musicPlay, 80, 80)
                        soundChange(2)
                    else:
                        musicButton, musicTimer, musicPlay = ButtonOff(musicButton, soundOff, 15, musicPlay, 80, 80)
                        soundChange(0)
        if settingsOpen == False and infoOpen == False:
            if Mouse_x > 600 and Mouse_x < 680 and Mouse_y > 600 and Mouse_y < 680:
                if settingsOpen == False and infoOpen == False:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == False and infoOpen == False and tutorialTimer < 1:
                        if tutorialWork == False:
                            tutorialButton, tutorialTimer, tutorialWork = ButtonOn(tutorialButton, tutorialOn, 15, tutorialWork, 80, 80)
                        else:
                            tutorialButton, tutorialTimer, tutorialWork = ButtonOff(tutorialButton, tutorialOff, 15, tutorialWork, 80, 80)
        if settingsOpen == True:
            if Mouse_x > 280 and Mouse_x < 360 and Mouse_y > 100 and Mouse_y < 180:
                if settingsOpen == True and infoOpen == False:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == True and infoOpen == False and tutorialTimer < 1:
                        if tutorialWork == False:
                            tutorialButton, tutorialTimer, tutorialWork = ButtonOn(tutorialButton, tutorialOn, 15, tutorialWork, 80, 80)
                        else:
                            tutorialButton, tutorialTimer, tutorialWork = ButtonOff(tutorialButton, tutorialOff, 15, tutorialWork, 80, 80)

        if Mouse_x > 370 and Mouse_x < 450 and Mouse_y > 100 and Mouse_y < 180:
            if settingsOpen == True:
                mouseCanClick = True
            if mouseClick == True and clicked == 1:
                if settingsOpen == True and dlcTimer < 1:
                    if dlcWork == False:
                        dlc, dlcTimer, dlcWork = ButtonOn(dlc, dlcOn, 15, dlcWork, 80, 80)
                    else:
                        dlc, dlcTimer, dlcWork = ButtonOff(dlc, dlcOff, 15, dlcWork, 80, 80)
        
        if Mouse_x > 460 and Mouse_x < 540 and Mouse_y > 100 and Mouse_y < 180:
            if settingsOpen == True:
                mouseCanClick = True
            if mouseClick == True and clicked == 1:
                if settingsOpen == True and textureTimer < 1:
                    webbrowser.open('https://github.com/Anuken/Mindustry/tree/master/core', new=2)
                    textureTimer = 15
                    click.play()

        if testSee == True:
            if Mouse_x > 280 and Mouse_x < 360 and Mouse_y > 190 and Mouse_y < 270:
                if settingsOpen == True:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == True and fogTimer < 1:
                        if fogWork == False:
                            fogButton, fogTimer, fogWork = ButtonOn(fogButton, fogOn, 15, fogWork, 80, 80)
                        else:
                            fogButton, fogTimer, fogWork = ButtonOff(fogButton, fogOff, 15, fogWork, 80, 80)
                
            if Mouse_x > 10 and Mouse_x < 90 and Mouse_y > 100 and Mouse_y < 180:
                if settingsOpen == True:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == True and unlModeTimer < 1:
                        if unlMode == False:
                            unlimitedResButton, unlModeTimer, unlMode = ButtonOn(unlimitedResButton, unlimitedResOn, 15, unlMode, 80, 80)
                            copper, led, thorium, hlak, water, oil, graphite = resourseChange(99999, 99999, 99999, 99999, 99999, 99999, 99999)
                        else:
                            unlimitedResButton, unlModeTimer, unlMode = ButtonOff(unlimitedResButton, unlimitedResOff, 15, unlMode, 80, 80) 
                            if hardMode == False:
                                copper, led, thorium, hlak, water, oil, graphite = resourseChange(10, 0, 0, 0, 0, 0, 0)
                            else:
                                copper, led, thorium, hlak, water, oil, graphite = resourseChange(-100, -100, -50, -100, -10, -30, -100)
    
            if Mouse_x > 100 and Mouse_x < 180 and Mouse_y > 190 and Mouse_y < 270:
                if settingsOpen == True:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == True and nextTimer < 1:
                            selectedPlanet += 1
                            if dlcWork == True:
                                if selectedPlanet > 5:
                                    selectedPlanet = 1
                            else:
                                if selectedPlanet > 4:
                                    selectedPlanet = 1
                            if selectedPlanet == 1:
                                if langRus == True:
                                    map = planetRealm
                                else:
                                    map = planetRealmEng
                                bg = bg1
                            if selectedPlanet == 2:
                                if langRus == True:
                                    map = blackHole
                                else:
                                    map = blackHoleEng
                                bg = bg2
                            if selectedPlanet == 3:
                                if langRus == True:
                                    map = planetEarth
                                else:
                                    map = planetEarthEng
                                bg = bg3
                            if selectedPlanet == 4:
                                if langRus == True:
                                    map = planetLuck
                                else:
                                    map = planetLuckEng
                                bg = bg4
                            if selectedPlanet == 5:
                                if langRus == True:
                                    map = planetUranius
                                else:
                                    map = planetUraniusEng
                                bg = bg5
                            map = pygame.transform.scale(map, (450,300))
                            nextTimer = 15
                            click.play()
                    
            if Mouse_x > 280 and Mouse_x < 360 and Mouse_y > 10 and Mouse_y < 90:
                if settingsOpen == True:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == True and nextEquipTimer < 1:
                            equipment += 1
                            if equipment > 3:
                                equipment = 1
                            if equipment == 1:
                                equipSee = equipmentBullet
                                equipSee2 = equipmentBigBullet2
                            if equipment == 2:
                                equipSee = equipmentHealBullet
                                equipSee2 = equipmentBullet2
                            if equipment == 3:
                                equipSee = equipmentBigBullet
                                equipSee2 = equipmentHealBullet2
                            nextEquipTimer = 15
                            click.play()
    
            if Mouse_x > 100 and Mouse_x < 180 and Mouse_y > 10 and Mouse_y < 90:
                if settingsOpen == True:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == True and enemiesSpawnTimer < 1:
                        if doEnemiesSpawn == False:
                            enemiesSpawn, enemiesSpawnTimer, doEnemiesSpawn = ButtonOn(enemiesSpawn, withEnemyOn, 15, doEnemiesSpawn, 80, 80)
                            doEnemiesSpawn2 = True
                        else:
                            enemiesSpawn, enemiesSpawnTimer, doEnemiesSpawn = ButtonOff(enemiesSpawn, withEnemyOff, 15, doEnemiesSpawn, 80, 80)
                            doEnemiesSpawn2 = False
    
            if Mouse_x > 100 and Mouse_x < 180 and Mouse_y > 100 and Mouse_y < 180:
                if settingsOpen == True:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == True and unlHpTimer < 1:
                        if doUnlHp == False:
                            unlimitedHpButton, unlHpTimer, doUnlHp = ButtonOn(unlimitedHpButton, unlimitedHpOn, 15, doUnlHp, 80, 80)
                        else:
                            unlimitedHpButton, unlHpTimer, doUnlHp = ButtonOff(unlimitedHpButton, unlimitedHpOff, 15, doUnlHp, 80, 80)
    
            if Mouse_x > 190 and Mouse_x < 270 and Mouse_y > 100 and Mouse_y < 180:
                if settingsOpen == True:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == True and airdropTimer < 1:
                        if airdrops == False:
                            airdropButton, airdropTimer, airdrops = ButtonOn(airdropButton, airdropOn, 15, airdrops, 80, 80)
                        else:
                            airdropButton, airdropTimer, airdrops = ButtonOff(airdropButton, airdropOff, 15, airdrops, 80, 80)   
    
            if Mouse_x > 190 and Mouse_x < 270 and Mouse_y > 190 and Mouse_y < 270:
                if settingsOpen == True:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == True and randTimer < 1:
                        if randSkins == False:
                            randButton, randTimer, randSkins = ButtonOn(randButton, randomSkinOn, 15, randSkins, 80, 80)
                        else:
                            randButton, randTimer, randSkins = ButtonOff(randButton, randomSkinOff, 15, randSkins, 80, 80)
    
            if Mouse_x > 190 and Mouse_x < 270 and Mouse_y > 10 and Mouse_y < 90:
                if settingsOpen == True:
                    mouseCanClick = True
                if mouseClick == True and clicked == 1:
                    if settingsOpen == True and cheatTimer < 1:
                        if doCheatWork == False:
                            cheatButton, cheatTimer, doCheatWork = ButtonOn(cheatButton, cheatModOn, 15, doCheatWork, 80, 80)
                        else:
                            cheatButton, cheatTimer, doCheatWork = ButtonOff(cheatButton, cheatModOff, 15, doCheatWork, 80, 80) 

        if Mouse_x > 950 and Mouse_x < 1150 and Mouse_y > 520 and Mouse_y < 620:
            if settingsOpen == True:
                mouseCanClick = True
            if mouseClick == True and clicked == 1:
                if settingsOpen == True and testTimer < 1:
                    if testSee == False:
                        testSeeButton, testTimer, testSee = ButtonOn(testSeeButton, testSettingsOn, 15, testSee, 200, 100)
                    else:
                        testSeeButton, testTimer, testSee = ButtonOff(testSeeButton, testSettingsOff, 15, testSee, 200, 100)          

        if Mouse_x > 550 and Mouse_x < 630 and Mouse_y > 100 and Mouse_y < 180:
            if settingsOpen == True:
                mouseCanClick = True
            if mouseClick == True and clicked == 1:
                if settingsOpen == True and langTimer < 1:
                    if langRus == False:
                        langButton, langTimer, langRus = ButtonOn(langButton, langRu, 15, langRus, 80, 80)
                    else:
                        langButton, langTimer, langRus = ButtonOff(langButton, langEng, 15, langRus, 80, 80)

        langTimer = timerDown(langTimer,1)
        fogTimer = timerDown(fogTimer,1)
        dlcTimer = timerDown(dlcTimer,1)
        testTimer = timerDown(testTimer,1)
        textureTimer = timerDown(textureTimer,1)
        tutorialTimer = timerDown(tutorialTimer,1)
        airdropTimer = timerDown(airdropTimer,1)
        randTimer = timerDown(randTimer,1)
        enemiesSpawnTimer = timerDown(enemiesSpawnTimer,1)
        cheatTimer = timerDown(cheatTimer,1)
        nextTimer = timerDown(nextTimer,1)
        nextEquipTimer = timerDown(nextEquipTimer,1)
        musicTimer = timerDown(musicTimer,1)
        unlHpTimer = timerDown(unlHpTimer,1)
        unlModeTimer = timerDown(unlModeTimer,1)
        hardModeTimer = timerDown(hardModeTimer,1)
        settingsTimer = timerDown(settingsTimer,1)
        
        screen.blit(infoB, infoB_rect)
        if Mouse_x > 80 and Mouse_x < 160 and Mouse_y > 600:
            mouseCanClick = True
            if mouseClick == True and clicked == 1 and infoTimer < 1:
                if infoOpen == False and infoTimer < 1:
                    click.play()
                    infoTimer = 15
                    infoOpen = True
                    settingsOpen = False          
                    screen.blit(bgM, bgM_rect)
                if infoOpen == True and infoTimer < 1:
                    click.play()
                    infoTimer = 15
                    infoOpen = False    
                    screen.blit(bgM, bgM_rect)
        if infoOpen == True:
            infoBlit()

        infoTimer = timerDown(infoTimer,1)

        if selectedPlanet == 5 and dlcWork == False:
            selectedPlanet = 3
            map = planetEarth
            bg = bg3
            map = pygame.transform.scale(map, (450,300))

        timerForRestart = timerDown(timerForRestart,0.8)

        if timerForRestart < 1:
            if settingsOpen == False and infoOpen == False:
                screen.blit(logo, logo_rect)
                screen.blit(butPlayO, butPlayO_rect)
                screen.blit(butPlayC, butPlayC_rect)
                if Mouse_x < 600 and Mouse_y < 600:
                    if settingsOpen == False and infoOpen == False:
                        mouseCanClick = True
                    if mouseClick == True and clicked == 1:
                        click.play()
                        menuOpen = False
                        if gameMode == 'None':
                            gameMode = 'One'
                        if randSkins == True:
                            randomSkin()
                        pygame.mixer.stop()
                        if selectedPlanet == 1:
                            inGame.play()
                        if selectedPlanet == 2:
                            inGame2.play() 
                        if selectedPlanet == 3:
                            inGame3.play()      
                        if selectedPlanet == 4:      
                            inGame4.play()  
                        if selectedPlanet == 5:      
                            inGame5.play()  
                if Mouse_x > 600 and Mouse_y < 600:
                    if settingsOpen == False and infoOpen == False:
                        mouseCanClick = True
                    if mouseClick == True and clicked == 1:
                        click.play()
                        menuOpen = False   
                        if gameMode == 'None':
                            gameMode = 'Coop'  
                        if randSkins == True:
                            randomSkin()
                            randomSkin2()
                        pygame.mixer.stop()
                        if selectedPlanet == 1:
                            inGame.play()      
                        if selectedPlanet == 2:      
                            inGame2.play()  
                        if selectedPlanet == 3:
                            inGame3.play()      
                        if selectedPlanet == 4:      
                            inGame4.play() 
                        if selectedPlanet == 5:      
                            inGame5.play()   

        if timerForRestart > 0:
            if langRus == True:
                loading = load
            else:
                loading = loadE
            loading_rect = loading.get_rect()
            loading = pygame.transform.scale(loading, BG_SIZE)
            screen.blit(loading, loading_rect)

        if langRus == True:
            cheatHelp = helpCheat
            if testSee == True:
                testSeeButton = testSettingsOn
            else:
                testSeeButton = testSettingsOff
            helpEsc = escHelpT
            contr = control
            costHelp = costHelpIM
            costHelp = pygame.transform.scale(costHelp, (200,640))
        else:
            cheatHelp = helpCheatE
            if testSee == True:
                testSeeButton = testSettingsOnE
            else:
                testSeeButton = testSettingsOffE
            helpEsc = escHelpTE
            contr = controlEng
            costHelp = costHelpIMEng
            costHelp = pygame.transform.scale(costHelp, (200,640))

        if selectedPlanet == 1:
            if langRus == True:
                map = planetRealm
            else:
                map = planetRealmEng
            bg = bg1
        if selectedPlanet == 2:
            if langRus == True:
                map = blackHole
            else:
                map = blackHoleEng
            bg = bg2
        if selectedPlanet == 3:
            if langRus == True:
                map = planetEarth
            else:
                map = planetEarthEng
            bg = bg3
        if selectedPlanet == 4:
            if langRus == True:
                map = planetLuck
            else:
                map = planetLuckEng
            bg = bg4
        if selectedPlanet == 5:
            if langRus == True:
                map = planetUranius
            else:
                map = planetUraniusEng
            bg = bg5
       
        map = pygame.transform.scale(map, (450,300))

        rtexts()

        pygame.mouse.set_visible(False)
        screen.blit(customM, customM_rect)  
    pygame.display.update()
    clock.tick(FPS)