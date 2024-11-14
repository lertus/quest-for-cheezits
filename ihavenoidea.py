import pygame
import random
import time
import json

def LoadImages(FileNamez):
    Images = []
    for F in FileNamez:
        I = pygame.image.load(F)
        I = pygame.transform.scale(I, (64, 64))
        Images.append(I)
    return Images
def LoadMap(FileNameAgain):
    Map = []
    with open(FileNameAgain, "r") as File:
        for Line in File:
            Line.strip()
            Sprites = []
            for C in Line:
                if C == "-": 
                    Sprites.append(bgimage)
                elif C == "C":
                    Sprites.append(coolio2)
                elif C == "0":
                    Sprites.append(coolbgimage)
                elif C == ".":
                    Sprites.append(void1)
                elif C == "W":
                    Sprites.append(wallnt)
                elif C == "$":
                    Sprites.append(cashmoney)
                elif C == "c":
                    Sprites.append(coolio1)
                elif C == "_":
                    Sprites.append(wood)
                elif C == "&":
                    Sprites.append(YOMI)
                elif C == "B":
                    Sprites.append(box)
            Map.append(Sprites)
    return Map

def LoadDialouge(FileTalkingName):
    DictionaryOfStupidity = {}
    with open(FileTalkingName, "r") as File:
        DialougeList = json.load(File)
    for Entry in DialougeList:
        Key = (Entry["y"], Entry["x"])
        DictionaryOfStupidity[Key] = Entry["dialouge"]
    return DictionaryOfStupidity
    

def SpintheWHEEL(prob, damage):
    probsum = sum(prob)
    rand0m = random.random() * probsum
    while rand0m > prob[0]:
        rand0m -= prob[0]
        prob = prob[1:]
        damage = damage[1:]
    return damage[0]

# def DrawTheFight(EnemyBIG, imageWHAT, Text2, PlayerHp, EnemyHp):
#     BBBOX = pygame.Rect(0, 0, 1024, 768)
#     pygame.draw.rect(screen, (255, 255, 255), BBBOX)
#     screen.blit(EnemyBIG, [576, 64])
#     screen.blit(imageWHAT, [0, 256])
#     Text = Font.render(Text2, False, (0, 0, 0))
#     Rect = Text.get_rect(center = (704, 576))
#     #Box = Rect.inflate(20, 20)
#     #pygame.draw.rect(screen, (0, 0, 0), Box)
#     screen.blit(Text, Rect)
#     Text = Font.render(f"Your health: {PlayerHp}", False, (0, 0, 0))
#     Rect = Text.get_rect(center = (192, 384))
#     screen.blit(Text, Rect)
#     Text = Font.render(f"THE ENEMY'S health: {EnemyHp}", False, (0, 0, 0))
#     Rect = Text.get_rect(center = (832, 384))
#     screen.blit(Text, Rect)
    
def DrawTheFight(EnemyBIG, imageWHAT, Text2, PlayerHp, EnemyHp, Text3 = ""):
    BBBOX = pygame.Rect(0, 0, 1024, 768)
    pygame.draw.rect(screen, (255, 255, 255), BBBOX)
    screen.blit(EnemyBIG, [(64 * 11), 190])
    screen.blit(imageWHAT, [15, 192])
    Text = Font.render(Text2, False, (0, 0, 0))
    Rect = Text.get_rect(center = (704, 576))
    #Box = Rect.inflate(20, 20)
    #pygame.draw.rect(screen, (0, 0, 0), Box)
    screen.blit(Text, Rect)
    Text = Font.render(Text3, False, (0, 0, 0))
    Rect = Text.get_rect(center = ((64 * 11), 200))
    screen.blit(Text, Rect)
    Text = Font.render(f"Your health: {PlayerHp}", False, (0, 0, 0))
    Rect = Text.get_rect(center = (0, 64))
    screen.blit(Text, Rect)
    Text = Font.render(f"THE ENEMY'S health: {EnemyHp}", False, (0, 0, 0))
    Rect = Text.get_rect(center = (0, 704))
    screen.blit(Text, Rect)

def DrawTheMenu(OkNiceMove, Moves, TextY = 512, TextX = 576, TextColor = (0, 0, 0)):
    for i, Move in enumerate(Moves):
        if type(Move) is dict:
            Text2 = Move["name"]
        else:
            Text2 = Move
        if i == OkNiceMove:
            Text2 = "* " + Text2
        else:
            Text2 = "  " + Text2
        Text = Font.render(Text2, False, TextColor)
        Rect = Text.get_rect(center = (TextX, TextY))
        screen.blit(Text, Rect)
        TextY += 64

def LeFightCommence():
    imageWHAT = pygame.image.load('You.png')
    imageWHAT = pygame.transform.scale(imageWHAT, (256, 256))
    pygame.mixer.music.stop()
    BattleSound = pygame.mixer.Sound("vibecheckcopy.mp3")
    BattleSound.play()
    for y in range(12):
        for x in range (16):
            for i in range(12):
                for j in range(16):
                    if i > y or (i == y and j > x):    
                        screen.blit(Map[i + Yoffset][j + Xoffset], [64 * j, 64 * i])
                    else:
                        BBBOX = pygame.Rect(64 * j, 64 * i, 64, 64)
                        pygame.draw.rect(screen, (0, 0, 0), BBBOX)
            pygame.display.flip()
            pygame.time.delay(2)
    pygame.mixer.music.load("Tycoon.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    EnemyIndex = -1
    for i in range(len(ViolentFiles)):
        if ViolentFiles[i] == THEEnemy:
            EnemyIndex = i
            break
    EnemyData = ViolentwithCheese[EnemyIndex]
    PlayerData = ViolentwithCheese[-1]
    MyTurnYipee = True
    MoveStage = 1
    EnemyHp = EnemyData["health"]
    PlayerCooldown = {}
    EnemyCooldown = {}
    if EnemyData["name"] in DialougebutViolent:
        DialougeHit = DialougebutViolent[EnemyData["name"]]["dialougehit"]
        DialougeTauntish = DialougebutViolent[EnemyData["name"]]["dialougetauntish"]
    else:
        DialougeHit = [""]
        DialougeTauntish = [""]
    PlayerHp = PlayerData["health"]
    JustBreakItUpYouTwo = True
    EnemyBIG = pygame.transform.scale(THEEnemy, (256, 256))
    while JustBreakItUpYouTwo == True:
        Text2 = "GRAAAAAAHHHHH!!!"
        Text3 = ""
        if EnemyHp <= 0:
            Text2 = f"{EnemyData['name']} has fallen. What a dingus."
            JustBreakItUpYouTwo = False
        elif PlayerHp <= 0:
            Text2 = f"You have fallen. Dingus."
            JustBreakItUpYouTwo = False
        elif MyTurnYipee == True:
            ADecisionMade = False
            OkNiceMove = 0
            while ADecisionMade == False:
                DrawTheFight(EnemyBIG, imageWHAT, " ", PlayerHp, EnemyHp)
                DrawTheMenu(OkNiceMove, PlayerData["moves"])
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            OkNiceMove += 1
                            if OkNiceMove >= len(PlayerData["moves"]):
                                OkNiceMove = len(PlayerData["moves"]) - 1
                        elif event.key == pygame.K_UP:
                            OkNiceMove -= 1
                            if OkNiceMove <= 0:
                                OkNiceMove = 0
                        elif event.key == pygame.K_e:
                            LETSGOGAMBLING = PlayerData["moves"][OkNiceMove]
                            ADecisionMade = True
                
                
            #LETSGOGAMBLING = random.choice(PlayerData["moves"])
            if len(LETSGOGAMBLING["prob"]) == 1:
                damage = LETSGOGAMBLING["damage"][0]
            else:
                damage = SpintheWHEEL(LETSGOGAMBLING["prob"], LETSGOGAMBLING["damage"])
            Text2 = f"You decided to use {LETSGOGAMBLING['name']}, it did {damage}!"
            
            if LETSGOGAMBLING["self"] == True:
                PlayerHp -= damage
                if PlayerHp >= PlayerData["health"]:
                    PlayerHp = PlayerData["health"]
            else:
                Text3 = random.choice(DialougeHit)
                EnemyHp -= damage
        elif MyTurnYipee == False:
            MoveChosen = False
            while not MoveChosen:
                LETSGOGAMBLING = random.choice(EnemyData["moves"])
                MoveChosen = True
                if "cooldown" in LETSGOGAMBLING:
                    if LETSGOGAMBLING["name"] in EnemyCooldown and EnemyCooldown[LETSGOGAMBLING["name"]] > 0:
                        MoveChosen = False
                        print(EnemyCooldown)
                    else:
                        EnemyCooldown[LETSGOGAMBLING["name"]] = LETSGOGAMBLING["cooldown"] + 1
            for Key in EnemyCooldown:
                EnemyCooldown[Key] -= 1
                        
            if len(LETSGOGAMBLING["prob"]) == 1:
                damage = LETSGOGAMBLING["damage"][0]
            else:
                damage = SpintheWHEEL(LETSGOGAMBLING["prob"], LETSGOGAMBLING["damage"])
            Text2 = f"{EnemyData['name']} used {LETSGOGAMBLING['name']}, so it did {damage}!"
            if LETSGOGAMBLING["self"] == True:
                EnemyHp -= damage
                if EnemyHp >= EnemyData["health"]:
                    EnemyHp = EnemyData["health"]
            else:
                Text3 = random.choice(DialougeTauntish)
                PlayerHp -= damage
        if "sound" in LETSGOGAMBLING:
            AttackSound = pygame.mixer.Sound(LETSGOGAMBLING["sound"])
            AttackSound.play()
        MyTurnYipee = not MyTurnYipee
        DrawTheFight(EnemyBIG, imageWHAT, Text2, PlayerHp, EnemyHp, Text3)
        pygame.display.flip()
        #pygame.time.delay(1000)
        WaitinForAKey = True
        while WaitinForAKey == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    WaitinForAKey = False

    


        
def GoogleIt(y, x):
    print(y, x)
    try:
        Yap = DictionaryOfDeez[(y, x)]
    except:
        Yap = "COOLIO2 ROCKS!!"
    return Yap

def MapMaker():
    Rows = len(Map)
    Columns = len(Map[0])
    Surface = pygame.Surface((Columns * 64, Rows * 64))
    for i in range(Rows):
        for j in range (Columns):
            Surface.blit(Map[i][j], (64 * j, 64 * i))
    pygame.image.save(Surface, "guh.png")

    
    

# Initialize PyGame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("noors.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
# Set up display
screen_width, screen_height = 1024, 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coolio2 ROCKS!!")
# Load image (Make sure the image is in the same directory or provide a full path)
image = pygame.image.load('fella smaller.png')
image = pygame.transform.scale(image, (64, 64))
coolio2 = pygame.image.load('coolio2.png')
coolio2 = pygame.transform.scale(coolio2, (64, 64))
bgimage = pygame.image.load('grasslol.png')
bgimage = pygame.transform.scale(bgimage, (64, 64))
coolbgimage = pygame.image.load('coolgrasslol.png')
coolbgimage = pygame.transform.scale(coolbgimage, (64, 64))
void1 = pygame.image.load('voidedbird.png')
void1 = pygame.transform.scale(void1, (64, 64))
wallnt = pygame.image.load('wallnt.png')
wallnt = pygame.transform.scale(wallnt, (64, 64))
cashmoney = pygame.image.load('richkid.png')
cashmoney =  pygame.transform.scale(cashmoney, (64, 64))
coolio1 = pygame.image.load('coolio1.png')
coolio1 =  pygame.transform.scale(coolio1, (64, 64))
wood = pygame.image.load('wood.png')
wood =  pygame.transform.scale(wood, (64, 64))
YOMI = pygame.image.load('YOMI.png')
YOMI =  pygame.transform.scale(YOMI, (64, 64))
box = pygame.image.load('box.png')
box =  pygame.transform.scale(box, (64, 64))
image_width, image_height = image.get_size()
Map = LoadMap("ConfusingBaseplate.txt")
EastFiles = ['WalkingEast/Oldbusinessmanwalkingeast1.png', 'WalkingEast/Oldbusinessmanwalkingeast3.png', 'WalkingEast/Oldbusinessmanwalkingeast5.png', 'WalkingEast/Oldbusinessmanwalkingeast3.png']
WestFiles = ['WalkingWest/Oldbusinessmanwalkingwest1.png', 'WalkingWest/Oldbusinessmanwalkingwest3.png', 'WalkingWest/Oldbusinessmanwalkingwest5.png', 'WalkingWest/Oldbusinessmanwalkingwest3.png']
SouthFiles = ['WalkingSouth/Oldbusinessmanwalkingsouth1.png', 'WalkingSouth/Oldbusinessmanwalkingsouth3.png', 'WalkingSouth/Oldbusinessmanwalkingsouth5.png', 'WalkingSouth/Oldbusinessmanwalkingsouth3.png']
NorthFiles = ['WalkingNorth/Oldbusinessmanwalkingnorth1.png', 'WalkingNorth/Oldbusinessmanwalkingnorth3.png', 'WalkingNorth/Oldbusinessmanwalkingnorth5.png', 'WalkingNorth/Oldbusinessmanwalkingnorth3.png']
EastImages = LoadImages(EastFiles)
WestImages = LoadImages(WestFiles)
SouthImages = LoadImages(SouthFiles)
NorthImages = LoadImages(NorthFiles)
NuhUhFiles = [coolio2, void1, wallnt, cashmoney, coolio1, YOMI, box]
YapperFiles = [coolio2, cashmoney, coolio1, YOMI, box]
ViolentFiles = [cashmoney, YOMI, box]
with open("damageiscoolforhealth.json", "r") as f:
    ViolentwithCheese = json.load(f)
DictionaryOfDeez = LoadDialouge("dialouge.json")
with open("dialougefight.json", "r") as f:
    DialougebutViolent = json.load(f)


# Main loop
running = True
#image_position = [0, 0]
SpriteX = 0
SpriteY = 0
#imagep_coolio2 = [1024 - 128, 384]
xSpeed = 64
ySpeed = 64
Interaction = False
PersonalSpace = False
Font = pygame.font.Font(None, 36)
Frame = 0
RipOffRugrats = -1
StringHolder = " "


while running:

    # Display image at the random position
    screen.fill((0, 0, 0))  # Fill the screen with black
   

    if Interaction == False:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and SpriteX > 0:
            image = WestImages[Frame % 4]
            Frame += 1
            SpriteX -= 1
            if Map[SpriteY] [SpriteX] in NuhUhFiles:
                SpriteX += 1
        if keys[pygame.K_RIGHT] and SpriteX < len(Map[0]) - 1:
            image = EastImages[Frame % 4]
            Frame += 1
            SpriteX += 1
            #space
            if Map[SpriteY] [SpriteX] in NuhUhFiles:
                SpriteX -= 1
        if keys[pygame.K_UP] and SpriteY > 0:
            image = NorthImages[Frame % 4]
            Frame += 1
            SpriteY -= 1
            if Map[SpriteY] [SpriteX] in NuhUhFiles:
                SpriteY += 1
        if keys[pygame.K_DOWN] and SpriteY < len(Map) - 1:
            image = SouthImages[Frame % 4]
            Frame += 1
            SpriteY += 1
            if Map[SpriteY] [SpriteX] in NuhUhFiles:
                SpriteY -= 1
        if keys[pygame.K_0]:
            image = pygame.image.load('PS.jpeg')
            
            print("hardy har har")
    if SpriteX < len(Map[0]) - 1 and Map[SpriteY] [SpriteX + 1] in YapperFiles:
        PersonalSpace = True
        YapHolder = GoogleIt(SpriteY, SpriteX + 1)
        THEEnemy = Map[SpriteY][SpriteX + 1]
    elif SpriteX > 0 and Map[SpriteY] [SpriteX - 1] in YapperFiles:
        PersonalSpace = True
        YapHolder = GoogleIt(SpriteY, SpriteX - 1)
        THEEnemy = Map[SpriteY][SpriteX - 1]
    elif SpriteY < len(Map) - 1 and Map[SpriteY + 1] [SpriteX] in YapperFiles:
        PersonalSpace = True
        YapHolder = GoogleIt(SpriteY + 1, SpriteX)
        THEEnemy = Map[SpriteY + 1][SpriteX]
    elif SpriteY > 0 and Map[SpriteY - 1] [SpriteX] in YapperFiles:
        PersonalSpace = True
        YapHolder = GoogleIt(SpriteY - 1, SpriteX)
        THEEnemy = Map[SpriteY - 1][SpriteX]
    else:
        PersonalSpace = False
    if SpriteX > 12:
        Xoffset = SpriteX - 12
        while Xoffset + 15 >= len(Map[0]):
            Xoffset -= 1
    else:
        Xoffset = 0
    if SpriteY > 9:
        Yoffset = SpriteY - 9
        while Yoffset + 11 >= len(Map):
            Yoffset -= 1
    else:
        Yoffset = 0
    for i in range(12):
        for j in range(16):
            screen.blit(Map[i + Yoffset][j + Xoffset], [64 * j, 64 * i])
            
    screen.blit(image, [64 * (SpriteX - Xoffset), 64 * (SpriteY - Yoffset)])
    #screen.blit(coolio2, imagep_coolio2)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and PersonalSpace == True:
                if type(YapHolder) is list:
                    RipOffRugrats += 1
                    if RipOffRugrats >= len(YapHolder):
                        Interaction = False
                        StringHolder = " "
                        RipOffRugrats = -1
                        if THEEnemy in ViolentFiles:
                            LeFightCommence()
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("noors.wav")
                            pygame.mixer.music.set_volume(0.2)
                            pygame.mixer.music.play(-1)
                    elif type(StringHolder) is list and len(StringHolder) > 2:
                        RipOffRugrats = StringHolder[DialougeChoice * 2 + 1]
                        StringHolder = YapHolder[RipOffRugrats]
                    elif type(StringHolder) is list:
                        RipOffRugrats = StringHolder[1]
                        if RipOffRugrats >= len(YapHolder):
                            Interaction = False
                            StringHolder = " "
                            RipOffRugrats = -1
                            if THEEnemy in ViolentFiles:
                                LeFightCommence()
                                pygame.mixer.music.stop()
                                pygame.mixer.music.load("noors.wav")
                                pygame.mixer.music.set_volume(0.2)
                                pygame.mixer.music.play(-1)
                    else:
                        Interaction = True
                        DialougeChoice = 0
                        StringHolder = YapHolder[RipOffRugrats]
                else:
                    Interaction = not Interaction
                    StringHolder = YapHolder
            if event.key == pygame.K_m:
                MapMaker()
            if event.key == pygame.K_DOWN and Interaction == True:
                DialougeChoice += 1
                if DialougeChoice >= len(StringHolder) / 2:
                    DialougeChoice = len(StringHolder) / 2 - 1
            if event.key == pygame.K_UP and Interaction == True:
                DialougeChoice -= 1
                if DialougeChoice < 0:
                    DialougeChoice = 0

        if event.type == pygame.QUIT:
            running = False
    if Interaction == True:
        if type(StringHolder) is list and len(StringHolder) > 2:
            Box = pygame.Rect(384, 256, 256, 256)
            pygame.draw.rect(screen, (0, 0, 0), Box)
            DrawTheMenu(DialougeChoice, StringHolder[0 :: 2], TextX = 512, TextY = 320, TextColor = (255, 255, 255))
        elif type(StringHolder) is list:
            Text = Font.render(StringHolder[0], False, (255, 255, 255))
            Rect = Text.get_rect(center = (512, 384))
            Box = Rect.inflate(20, 20)
            pygame.draw.rect(screen, (0, 0, 0), Box)
            screen.blit(Text, Rect)
        else:
            Text = Font.render(StringHolder, False, (255, 255, 255))
            Rect = Text.get_rect(center = (512, 384))
            Box = Rect.inflate(20, 20)
            pygame.draw.rect(screen, (0, 0, 0), Box)
            screen.blit(Text, Rect)
    pygame.display.flip()  # Update the display
    pygame.time.delay(100)  # Delay to prevent using too much CPU

pygame.quit()