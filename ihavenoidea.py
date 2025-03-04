import pygame
import random
import time
import json

def apply_grayscale_filter(surface):
    arr = pygame.surfarray.pixels3d(surface)
    grayscale_values = arr[:, :, 0] * 0.3 + arr[:, :, 1] * 0.59 + arr[:, :, 2] * 0.11
    arr[:, :, 0] = grayscale_values
    arr[:, :, 1] = grayscale_values
    arr[:, :, 2] = grayscale_values
    del arr  # Unlock the surface
    return surface

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
                elif C == "|":
                    Sprites.append(shopkeeper)
                elif C == "^":
                    Sprites.append(woodenstairs)
                elif C == "v":
                    Sprites.append(woodenstairsdown)
                elif C == ":":
                    Sprites.append(bucketguy)
                elif C == "∞":
                    Sprites.append(coolber)
            Map.append(Sprites)
    return Map

def MapToHomeLocations(ThisMap):
    HomeLocations = []
    for i, Row in enumerate(ThisMap):
        LocationsRow = []
        for j, Sprite in enumerate(Row):
            if Sprite in SchmovinFiles:
                LocationsRow.append((i, j))
            else:
                LocationsRow.append(None)
        HomeLocations.append(LocationsRow)
    return HomeLocations

def Schmove(ThisMap, ThisBMap, HomeLocations):
    for i, Row in enumerate(ThisMap):
        for j, Sprite in enumerate(Row):
            if Sprite in SchmovinFiles:
                if random.random() < 0.95:
                    continue
                Home  = HomeLocations[i][j]
                if random.random() < 0.5:
                    if random.random() < 0.5:
                        Newj = j + 1
                    else:
                        Newj = j - 1
                    if abs(Home[1] - Newj) > 3:
                        continue
                    if ThisMap[i][Newj] in NuhUhFiles:
                        continue
                    ThisMap[i][Newj] = Sprite
                    ThisMap[i][j] = ThisBMap[i][j]
                    HomeLocations[i][Newj] = Home
                    HomeLocations[i][j] = None
                    if (i, j) in DictionaryOfDeez:
                        DictionaryOfDeez[(i, Newj)] = DictionaryOfDeez[(i, j)]
                        del DictionaryOfDeez[(i, j)] 
                else:
                    if random.random() < 0.5:
                        Newi = i + 1
                    else:
                        Newi = i - 1
                    if abs(Home[0] - Newi) > 3:
                        continue
                    if ThisMap[Newi][j] in NuhUhFiles:
                        continue
                    ThisMap[Newi][j] = Sprite
                    ThisMap[i][j] = ThisBMap[i][j]
                    HomeLocations[Newi][j] = Home
                    HomeLocations[i][j] = None
                    if (i, j) in DictionaryOfDeez:
                        DictionaryOfDeez[(Newi, j)] = DictionaryOfDeez[(i, j)]
                        del DictionaryOfDeez[(i, j)] 

                    

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
    Rect = Text.get_rect(center = (118, 64))
    screen.blit(Text, Rect)
    Text = Font.render(f"THE ENEMY'S health: {EnemyHp}", False, (0, 0, 0))
    Rect = Text.get_rect(center = (150, 704))
    screen.blit(Text, Rect)

def DrawTheMenu(OkNiceMove, Moves, TextY = 512, TextX = 576, TextColor = (0, 0, 0), TextFont = None):
    for i, Move in enumerate(Moves):
        if type(Move) is dict:
            Text2 = Move["name"]
        else:
            Text2 = Move
        if i == OkNiceMove:
            Text2 = "* " + Text2
        else:
            Text2 = "  " + Text2
        #Text = Font.render(Text2, False, TextColor)
        #Rect = Text.get_rect(topleft = (TextX, TextY))
        #screen.blit(Text, Rect)
        TextCooler(LinesofText=Text2.split("|"), TextColor=TextColor, TextPosition=(TextX, TextY), TextFont = TextFont)
        TextY += 64


def ShopTime():
    FontSmaller = pygame.font.Font("ARCADE_N.TTF", 10)
    global CoolBucks
    with open("CoolShop.json", "r") as file:
        ShopData = json.load(file)
    with open("CoolItemAbilitys.json", "r") as file:
        ItemData = json.load(file)
    InventoryNames = [i["name"] for i in Inventory]
    for DictonaryOfShopping in ShopData:
        if DictonaryOfShopping["x"] == THEEnemyX and DictonaryOfShopping["y"] == THEEnemyY:
            ShopItemsTemp = DictonaryOfShopping["items"]
            ItemPricesTemp = DictonaryOfShopping["prices"]
            ItemPrices = [ItemPricesTemp[i] for i in range(len(ShopItemsTemp)) if ShopItemsTemp[i] not in InventoryNames]
            ShopItems = [ShopItemsTemp[i] for i in range(len(ShopItemsTemp)) if ShopItemsTemp[i] not in InventoryNames]
            ItemWITHPrices = [ShopItems[i] + " " + str(ItemPrices[i]) for i in range(len(ShopItems))]
            ItemWITHPrices.append("Get outta here!")
    imageshop = pygame.image.load('Shop.png')
    imageshop = pygame.transform.scale(imageshop, (1024, 768))
    imageCoolBuck = pygame.image.load('coolbuck.png')
    imageCoolBuck = pygame.transform.scale(imageCoolBuck, (64, 64))
    pygame.mixer.music.stop() 
    StoreSound = pygame.mixer.Sound("storebell.mp3")
    StoreSound.play()
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
    StillShopping = True
    ShowingMessage =False
    Menu = 0
    while StillShopping == True:
        screen.blit(imageshop, [0, 0])
        #ShopItems = ["Item1", "Item2", "Item3", "Get outta here!"]
        Text = Font.render(str(CoolBucks), False, (255, 255, 255))
        Rect = Text.get_rect(center = (844, 180))
        screen.blit(Text, Rect)
        screen.blit(imageCoolBuck, (934, 160))
        if ShowingMessage == True:
            Text = Font.render(PurchaceMessage, False, (255, 255, 255))
            Rect = Text.get_rect(center = (512, 384))
            Box = Rect.inflate(20, 20)
            pygame.draw.rect(screen, (0, 0, 0), Box)
            screen.blit(Text, Rect)
        else:
            DrawTheMenu(Menu, ItemWITHPrices, TextX = 20, TextY = 120, TextColor = (255, 255, 255), TextFont = FontSmaller)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if ShowingMessage == True:
                    ShowingMessage = False
                    break
                if event.key == pygame.K_DOWN:
                    Menu += 1
                    if Menu >= len(ItemWITHPrices):
                        Menu = len(ItemWITHPrices) - 1
                elif event.key == pygame.K_UP:
                    Menu -= 1
                    if Menu <= 0:
                        Menu = 0
                elif event.key == pygame.K_e:
                    if Menu == len(ItemWITHPrices) - 1:
                        StillShopping = False
                    else:
                        ShowingMessage = True
                        if CoolBucks >= ItemPrices[Menu]:
                            PurchaceMessage = "Thanks."
                            CoolBucks -= ItemPrices[Menu]
                            for Item in ItemData:
                                if Item["name"] == ShopItems[Menu]:
                                    PurchasedItem = Item
                            if PurchasedItem["type"] in ["blade", "blunt", "armor"]:
                                ItemWITHPrices.pop(Menu)
                                ShopItems.pop(Menu)
                                ItemPrices.pop(Menu)
                            Inventory.append(PurchasedItem)
                        else:
                            PurchaceMessage = "Sorry pal, ya dont have enough."
                                    

def DrawNewMenu(AwesomeNumberThatIsTheIndex):
    Icon1x = 724
    Icon2x = Icon1x + 76
    Icon3x = Icon2x + 76
    Icony = 590
    Rectanglex = Icon1x - 10 + 76 * AwesomeNumberThatIsTheIndex
    Rectangley = Icony - 10
    RectangleWidth = 64 + 20
    screen.blit(WeaponIcon, (Icon1x, Icony))
    screen.blit(ItemIcon, (Icon2x, Icony))
    screen.blit(NothingIcon, (Icon3x, Icony))
    Rect = pygame.Rect(Rectanglex, Rectangley, RectangleWidth, RectangleWidth)
    pygame.draw.rect(screen, (0, 0, 255), Rect, 3)

def DrawSubMenu(Moves, OkNiceMove):
    BackgroundsList = ["WeaponInventory.png", "doggo.png", "placeholder.png"]
    BackgroundImage = BackgroundsList[OkNiceMove]
    BackgroundImage = pygame.image.load(BackgroundImage)
    BackgroundImage = pygame.transform.scale(BackgroundImage, (1024, 768))
    ShowingInventory = True
    SelectedItem = 0
    while ShowingInventory == True:
        screen.blit(BackgroundImage, (0, 0))
        CurrentY = 185
        for i, Item in enumerate(Moves[OkNiceMove]):
            IconImage = pygame.image.load(Item["icon"])
            IconImage= pygame.transform.scale(IconImage, (64, 64))
            screen.blit(IconImage, [50, CurrentY])
            #Text = Font.render(Item["name"], False, (0, 0, 0))
            #Rect = Text.get_rect(topleft = (100, CurrentY))
            #screen.blit(Text, Rect)
            TextCooler(LinesofText=Item["name"].split("|"), TextColor=(0, 0, 0), TextPosition=(130, CurrentY))
            TextCooler(LinesofText=Item["desc"].split("|"), TextColor=(0, 0, 0), TextPosition=(750, CurrentY))
            CurrentY += 75
        TextCooler(["Exit menu"], (0, 0, 0), (130, 110))
        TextCooler(["*"], (0, 0, 0), (35, 110 + 75 * SelectedItem))
        #screen.blit(, [15, 192])
        pygame.display.flip()
        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    ShowingInventory = False
                elif event.key == pygame.K_DOWN:
                    SelectedItem += 1
                    print("Down key pressed.")
                    if SelectedItem > len(Moves[OkNiceMove]):
                        SelectedItem = len(Moves[OkNiceMove])
                elif event.key == pygame.K_UP:
                    SelectedItem -= 1
                    print("Up key pressed.")
                    if SelectedItem < 0:
                        SelectedItem = 0
                elif event.key == pygame.K_e:
                    if SelectedItem == 0:
                        return None, False
                    else:
                        return Moves[OkNiceMove][SelectedItem - 1], True
    return None, False

def LeFightCommence():
    global CoolBucks
    ActiveBuffs = []
    BuffDurations = []
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
    pygame.mixer.music.load("battlemusic.mp3")
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
    for Item in Inventory:
        if Item["type"] == "armor":
            PlayerHp += Item["health"]
    JustBreakItUpYouTwo = True
    EnemyBIG = pygame.transform.scale(THEEnemy, (256, 256))
    while JustBreakItUpYouTwo == True:
        Text2 = "GRAAAAAAHHHHH!!!"
        Text3 = ""
        if EnemyHp <= 0:
            Text2 = f"{EnemyData['name']} has fallen. What a dingus."
            JustBreakItUpYouTwo = False
            Outcome = True
            LootCash = 0
            LootIcon = None
            if "loot" in EnemyData:
                for Loot in EnemyData["loot"]:
                    if type(Loot) == int:
                        CoolBucks += Loot
                        LootCash = Loot
                    elif type(Loot) == str:
                        with open("CoolItemAbilitys.json", "r") as file:
                            ItemData = json.load(file)
                        for Item in ItemData:
                            if Item["name"] == Loot:
                                Inventory.append(Item)
                                LootIcon = Item["icon"]
        elif PlayerHp <= 0:
            Text2 = f"You have fallen. Dingus."
            JustBreakItUpYouTwo = False
            Outcome = False
        elif MyTurnYipee == True:
            ADecisionMade = False
            OkNiceMove = 0
            PlayerMoveTemp = PlayerData["moves"].copy()
            PlayerMove = [[],[],[]]
            HasWeapons = False
            for Item in Inventory:
                if Item["type"] == "blade" or Item["type"] == "blunt":
                    HasWeapons = True
                    Item["self"] = False
                    PlayerMove[0].append(Item)
                if Item["type"] == "item":
                    Item["self"] = False
                    PlayerMove[1].append(Item)
            #if HasWeapons == True:
                #PlayerMoveTemp.pop(0)
            for move in PlayerMoveTemp:
                if "cooldown" not in move or move["name"] not in PlayerCooldown or PlayerCooldown[move["name"]] <= 0:
                    PlayerMove[2].append(move)
            while ADecisionMade == False:
                DrawTheFight(EnemyBIG, imageWHAT, " ", PlayerHp, EnemyHp)
                #DrawTheMenu(OkNiceMove, PlayerMove, TextX= 520, TextY= 470)
                DrawNewMenu(OkNiceMove)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            OkNiceMove += 1
                            if OkNiceMove >= 3 :
                                OkNiceMove = 2
                        elif event.key == pygame.K_LEFT:
                            OkNiceMove -= 1
                            if OkNiceMove <= 0:
                                OkNiceMove = 0
                        elif event.key == pygame.K_e:
                            LETSGOGAMBLING, ADecisionMade = DrawSubMenu(PlayerMove, OkNiceMove)
            if "cooldown" in LETSGOGAMBLING:
                PlayerCooldown[LETSGOGAMBLING["name"]] = LETSGOGAMBLING["cooldown"] + 1
            if "type" in LETSGOGAMBLING and LETSGOGAMBLING["type"] == "item":
                for i in range(len(Inventory)):
                    if Inventory[i]["name"] == LETSGOGAMBLING["name"]:
                        Inventory.pop(i)
                        break
                BuffApplied = False
                for Buff in LETSGOGAMBLING["buffs"]:
                    if "health" in Buff:
                        PlayerHp += Buff["health"]
                        BuffApplied = True
                if not BuffApplied:
                    ActiveBuffs += LETSGOGAMBLING["buffs"]
                    BuffDurations += [LETSGOGAMBLING["duration"] + 1] * len(LETSGOGAMBLING["buffs"])
            for Key in PlayerCooldown:
                PlayerCooldown[Key] -= 1
            for i in range(len(BuffDurations)):
                BuffDurations[i] -= 1
                
            #LETSGOGAMBLING = random.choice(PlayerData["moves"])
            if "prob" in LETSGOGAMBLING:
                DamageMultiplier = 1.0
                for i in range(len(BuffDurations)):
                    if BuffDurations[i] > 0 and "damage" in ActiveBuffs[i]:
                        DamageMultiplier += ActiveBuffs[i]["damage"]
                if len(LETSGOGAMBLING["prob"]) == 1:
                    damage = LETSGOGAMBLING["damage"][0]
                else:
                    damage = SpintheWHEEL(LETSGOGAMBLING["prob"], LETSGOGAMBLING["damage"])
                damage *= DamageMultiplier
                Text2 = f"You decided to use {LETSGOGAMBLING['name']}, it did {damage}!"
                
                if LETSGOGAMBLING["self"] == True:
                    PlayerHp -= damage
                    if PlayerHp >= PlayerData["health"]:
                        PlayerHp = PlayerData["health"]
                else:
                    Text3 = random.choice(DialougeHit)
                    EnemyHp -= damage
            else:
                Text2 = f"You decided to use {LETSGOGAMBLING['name']}"
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
            ResistanceMultiplier = 1.0
            for i in range(len(BuffDurations)):
                if BuffDurations[i] > 0 and "resistance" in ActiveBuffs[i]:
                    ResistanceMultiplier -= ActiveBuffs[i]["resistance"]
            if ResistanceMultiplier < 0:
                ResistanceMultiplier = 0.0
            if len(LETSGOGAMBLING["prob"]) == 1:
                damage = LETSGOGAMBLING["damage"][0]
            else:
                damage = SpintheWHEEL(LETSGOGAMBLING["prob"], LETSGOGAMBLING["damage"])
            damage *= ResistanceMultiplier
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
        if "anim" in LETSGOGAMBLING:
            for Frame in LETSGOGAMBLING["anim"]:
                TempFrame = pygame.image.load(Frame)
                TempFrame = pygame.transform.scale(TempFrame, (256, 256))
                if MyTurnYipee:    
                    DrawTheFight(EnemyBIG, TempFrame, Text2, PlayerHp, EnemyHp, Text3)
                else:
                    DrawTheFight(TempFrame, imageWHAT, Text2, PlayerHp, EnemyHp, Text3)
                pygame.display.flip()
                pygame.time.delay(1000)
        else:
            DrawTheFight(EnemyBIG, imageWHAT, Text2, PlayerHp, EnemyHp, Text3)
            pygame.display.flip()
        MyTurnYipee = not MyTurnYipee
        WaitinForAKey = True
        while WaitinForAKey == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    WaitinForAKey = False
    if Outcome == True:
        BBBOX = pygame.Rect(0, 0, 1024, 768)
        pygame.draw.rect(screen, (127, 127, 127), BBBOX)
        VictoryImage = pygame.image.load("victoryresults.png")
        screen.blit(VictoryImage, (0, 0))
        IconImage = pygame.image.load(LootIcon)
        IconImage= pygame.transform.scale(IconImage, (200, 200))
        screen.blit(IconImage, [400, 80])
        LootString = f"You got {LootCash} CoolBucks! please dont waste them bro"
        Text = Font.render(LootString, False, (255, 255, 255))
        Rect = Text.get_rect(topleft = (0, 740))
        screen.blit(Text, Rect)
        pygame.display.flip()
        WaitinForAKey = True
        while WaitinForAKey == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    WaitinForAKey = False
    return Outcome

    
def TextCooler(LinesofText, TextColor, TextPosition, TextFont = None):
    if TextFont is None:
        TextFont = Font
    Yoffset = 0
    for Lines in LinesofText:
        Text = TextFont.render(Lines, False, TextColor)
        Rect = Text.get_rect(topleft = (TextPosition[0], TextPosition[1] + Yoffset))
        Yoffset += 20
        screen.blit(Text, Rect)
    
    
def OpenInventory():
    InventoryImage = pygame.image.load("CoolInventory.png")
    InventoryImage = pygame.transform.scale(InventoryImage, (1024, 768))
    screen.blit(InventoryImage, (0, 0))
    CurrentY = 110
    for Item in Inventory:
        IconImage = pygame.image.load(Item["icon"])
        IconImage= pygame.transform.scale(IconImage, (64, 64))
        screen.blit(IconImage, [20, CurrentY])
        #Text = Font.render(Item["name"], False, (0, 0, 0))
        #Rect = Text.get_rect(topleft = (100, CurrentY))
        #screen.blit(Text, Rect)
        TextCooler(LinesofText=Item["name"].split("|"), TextColor=(0, 0, 0), TextPosition=(100, CurrentY))
        TextCooler(LinesofText=Item["desc"].split("|"), TextColor=(0, 0, 0), TextPosition=(750, CurrentY))
        CurrentY += 75
    #screen.blit(, [15, 192])
    pygame.display.flip()
    ShowingInventory = True
    while ShowingInventory == True:
        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    ShowingInventory = False
        
        
def GoogleIt(y, x):
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
            if Map[i][j] in BGNEEDEDFiles:
                Surface.blit(BMap[i][j], (64 * j, 64 * i))
            Surface.blit(Map[i][j], (64 * j, 64 * i))
    pygame.image.save(Surface, "guh.png")

    
    

# Initialize PyGame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("nocopyrighttrust.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
# Set up display
screen_width, screen_height = 1024, 768
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED | pygame.RESIZABLE)
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
void1 = pygame.image.load('void.png')
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
bucketguy = pygame.image.load("bucketguy.png")
bucketguy = pygame.transform.scale(bucketguy, (64, 64))
lertusmcglertus = pygame.image.load("lertus.png")
lertusmcglertus = pygame.transform.scale(lertusmcglertus, (64, 64))
woodenstairs = pygame.image.load('stairs_wooden_up.png')
woodenstairs = pygame.transform.scale(woodenstairs, (64, 64))
woodenstairsdown = pygame.image.load('stairs_wooden_down.png')
woodenstairsdown = pygame.transform.scale(woodenstairsdown, (64, 64))
shopkeeper = pygame.image.load('merchant.png')
shopkeeper =  pygame.transform.scale(shopkeeper, (64, 64))
coolber = pygame.image.load('flubberbutcool.png')
coolber =  pygame.transform.scale(coolber, (64, 64))
WeaponIcon = pygame.image.load('placeholdericon.png')
WeaponIcon = pygame.transform.scale(WeaponIcon, (64, 64))
ItemIcon = pygame.image.load('placeholdericon.png')
ItemIcon = pygame.transform.scale(ItemIcon, (64, 64))
NothingIcon = pygame.image.load('placeholdericon.png')
NothingIcon = pygame.transform.scale(NothingIcon, (64, 64))
image_width, image_height = image.get_size()
Map = LoadMap("ConfusingBaseplate.txt")
BaseplateMap = Map
PizzaMap = LoadMap("stairs.txt")
BMap = LoadMap("Backgroundjustincase.txt")
BaseplateBMap = BMap
PizzaBMap = LoadMap("stairspizza.txt")
EastFiles = ['WalkingEast/Oldbusinessmanwalkingeast1.png', 'WalkingEast/Oldbusinessmanwalkingeast3.png', 'WalkingEast/Oldbusinessmanwalkingeast5.png', 'WalkingEast/Oldbusinessmanwalkingeast3.png']
WestFiles = ['WalkingWest/Oldbusinessmanwalkingwest1.png', 'WalkingWest/Oldbusinessmanwalkingwest3.png', 'WalkingWest/Oldbusinessmanwalkingwest5.png', 'WalkingWest/Oldbusinessmanwalkingwest3.png']
SouthFiles = ['PlayerWalk/WalkSouth1.png', 'PlayerWalk/WalkSouth2.png', 'PlayerWalk/WalkSouth3.png', 'PlayerWalk/WalkSouth2.png']
NorthFiles = ['WalkingNorth/Oldbusinessmanwalkingnorth1.png', 'WalkingNorth/Oldbusinessmanwalkingnorth3.png', 'WalkingNorth/Oldbusinessmanwalkingnorth5.png', 'WalkingNorth/Oldbusinessmanwalkingnorth3.png']
EastImages = LoadImages(EastFiles)
WestImages = LoadImages(WestFiles)
SouthImages = LoadImages(SouthFiles)
NorthImages = LoadImages(NorthFiles)
NuhUhFiles = [coolio2, void1, wallnt, cashmoney, coolio1, YOMI, box, shopkeeper, bucketguy, coolber]
YapperFiles = [coolio2, cashmoney, coolio1, YOMI, box, shopkeeper, bucketguy, lertusmcglertus, coolber]
ViolentFiles = [cashmoney, YOMI, box, lertusmcglertus, bucketguy]
CheaterFiles = False
HealerFiles = [coolber]
SchmovinFiles = [bucketguy]
BaseplateHomeLocations = MapToHomeLocations(BaseplateMap)
PizzaHomeLocations = MapToHomeLocations(PizzaMap)
CurrentHomeLocations= BaseplateHomeLocations
StairsUplol = [woodenstairs]
StairsDownlol = [woodenstairsdown]
ShoppingFiles = [shopkeeper]
BGNEEDEDFiles = [coolio2, coolio1, cashmoney, YOMI, box, shopkeeper, bucketguy, coolber]
with open("damageiscoolforhealth.json", "r") as f:
    ViolentwithCheese = json.load(f)
DictionaryOfDeez = LoadDialouge("dialouge.json")
CheatString = ""
DeadLol = False
with open("dialougefight.json", "r") as f:
    DialougebutViolent = json.load(f)

Inventory = []
CoolBucks = 5


# Main loop
running = True
#image_position = [0, 0]
SpriteX = 83
SpriteY = 33
#imagep_coolio2 = [1024 - 128, 384]
xSpeed = 64
ySpeed = 64
Interaction = False
PersonalSpace = False
Font = pygame.font.Font("ARCADE_N.TTF", 20)
Frame = 0
RipOffRugrats = -1
StringHolder = " "

BBBOX = pygame.Rect(0, 0, 1024, 768)
pygame.draw.rect(screen, (127, 127, 127), BBBOX)
TitleImage = pygame.image.load("titlescreen.png")
screen.blit(TitleImage, (0, 0))
pygame.display.flip()
WaitinForAKey = True
while WaitinForAKey == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            WaitinForAKey = False
pygame.mixer.music.stop()
pygame.mixer.music.load("noors.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
while running:

    # Display image at the random position
    screen.fill((0, 0, 0))  # Fill the screen with black
    

    if Interaction == False:
        Schmove(Map, BMap, CurrentHomeLocations)
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
        if keys[pygame.K_EQUALS]:
            pygame.display.toggle_fullscreen()
    if Map[SpriteY][SpriteX] in StairsUplol:
        Map = PizzaMap
        BMap = PizzaBMap
        CurrentHomeLocations = PizzaHomeLocations
    if Map[SpriteY][SpriteX] in StairsDownlol:
        Map = BaseplateMap
        BMap = BaseplateBMap
        CurrentHomeLocations = BaseplateHomeLocations
    if SpriteX < len(Map[0]) - 1 and Map[SpriteY] [SpriteX + 1] in YapperFiles:
        PersonalSpace = True
        YapHolder = GoogleIt(SpriteY, SpriteX + 1)
        THEEnemy = Map[SpriteY][SpriteX + 1]
        THEEnemyX = SpriteX + 1
        THEEnemyY = SpriteY
    elif SpriteX > 0 and Map[SpriteY] [SpriteX - 1] in YapperFiles:
        PersonalSpace = True
        YapHolder = GoogleIt(SpriteY, SpriteX - 1)
        THEEnemy = Map[SpriteY][SpriteX - 1]
        THEEnemyX = SpriteX - 1
        THEEnemyY = SpriteY
    elif SpriteY < len(Map) - 1 and Map[SpriteY + 1] [SpriteX] in YapperFiles:
        PersonalSpace = True
        YapHolder = GoogleIt(SpriteY + 1, SpriteX)
        THEEnemy = Map[SpriteY + 1][SpriteX]
        THEEnemyX = SpriteX
        THEEnemyY = SpriteY + 1
    elif SpriteY > 0 and Map[SpriteY - 1] [SpriteX] in YapperFiles:
        PersonalSpace = True
        YapHolder = GoogleIt(SpriteY - 1, SpriteX)
        THEEnemy = Map[SpriteY - 1][SpriteX]
        THEEnemyX = SpriteX
        THEEnemyY = SpriteY - 1
    elif CheaterFiles:
        PersonalSpace = True
        YapHolder = GoogleIt(-20, -4)
        THEEnemy = lertusmcglertus
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
            if Map[i + Yoffset][j + Xoffset] in BGNEEDEDFiles:
                screen.blit(BMap[i + Yoffset][j + Xoffset], [64 * j, 64 * i])
            screen.blit(Map[i + Yoffset][j + Xoffset], [64 * j, 64 * i])
            
    screen.blit(image, [64 * (SpriteX - Xoffset), 64 * (SpriteY - Yoffset)])
    #screen.blit(coolio2, imagep_coolio2)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode:
                CheatString += event.unicode
                CheatString = CheatString[-20:]
                if "meiswinner" in CheatString:
                    CoolBucks = 9000000
                    CheatString = ""
                elif "davestrider" in CheatString:
                    CoolBucks = -1
                    CheatString = ""
                elif "whenthe" in CheatString:
                    ViolentwithCheese[-1]["health"] = 123456789101112131415
                    CheatString = ""
                elif "evilmunchkinman" in CheatString:
                    with open("CoolItemAbilitys.json", "r") as file:
                        ItemData = json.load(file)
                    CheatString = ""
                    Inventory.append(ItemData[-2])
                elif "iamfromtheusa" in CheatString:
                    with open("CoolItemAbilitys.json", "r") as file:
                        ItemData = json.load(file)
                    CheatString = ""
                    Inventory.append(ItemData[-1])
                elif "iamuptonogood" in CheatString:
                    CheaterFiles = True
                    CheatString = ""
                        #>:)
            if event.key == pygame.K_e and PersonalSpace == True:
                if type(YapHolder) is list:
                    RipOffRugrats += 1
                    if RipOffRugrats >= len(YapHolder):
                        Interaction = False
                        StringHolder = " "
                        RipOffRugrats = -1
                        if THEEnemy in ViolentFiles and not DeadLol:
                            Outcome = LeFightCommence()
                            if CheaterFiles:
                                CheaterFiles = False
                            elif Outcome == True:
                                Map[THEEnemyY][THEEnemyX] = BMap[THEEnemyY][THEEnemyX]
                            if Outcome == False:
                                DeadLol = True
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("noors.wav")
                            pygame.mixer.music.set_volume(0.2)
                            pygame.mixer.music.play(-1)
                        elif THEEnemy in ShoppingFiles:
                            ShopTime()
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("noors.wav")
                            pygame.mixer.music.set_volume(0.2)
                            pygame.mixer.music.play(-1)
                    elif type(StringHolder) is list and len(StringHolder) > 2:
                        RipOffRugrats = StringHolder[DialougeChoice * 2 + 1]
                        StringHolder = YapHolder[RipOffRugrats]
                        if THEEnemy in HealerFiles and RipOffRugrats == 3:
                            DeadLol = False
                    elif type(StringHolder) is list:
                        RipOffRugrats = StringHolder[1]
                        if RipOffRugrats >= len(YapHolder):
                            Interaction = False
                            StringHolder = " "
                            RipOffRugrats = -1
                            if THEEnemy in ViolentFiles and not DeadLol:
                                Outcome = LeFightCommence()
                                if CheaterFiles:
                                    CheaterFiles = False
                                elif Outcome == True:
                                    Map[THEEnemyY][THEEnemyX] = BMap[THEEnemyY][THEEnemyX]
                                if Outcome == False:
                                    DeadLol = True
                                pygame.mixer.music.stop()
                                pygame.mixer.music.load("noors.wav")
                                pygame.mixer.music.set_volume(0.2)
                                pygame.mixer.music.play(-1)
                            elif THEEnemy in ShoppingFiles:
                                ShopTime()
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
            if event.key == pygame.K_TAB:
                OpenInventory()
            if event.key == pygame.K_DOWN and Interaction == True:
                DialougeChoice += 1
                if DialougeChoice >= len(StringHolder) // 2:
                    DialougeChoice = len(StringHolder) // 2 - 1
            if event.key == pygame.K_UP and Interaction == True:
                DialougeChoice -= 1
                if DialougeChoice < 0:
                    DialougeChoice = 0

        if event.type == pygame.QUIT:
            running = False
    if Interaction == True:
        Box = pygame.Rect(15, 497, 994, 248)
        pygame.draw.rect(screen, (64, 64, 64), Box)
        DialougeCharacter = pygame.transform.scale(THEEnemy, (250, 250))
        screen.blit(DialougeCharacter, (30, 497))
        if type(StringHolder) is list and len(StringHolder) > 2:
            DrawTheMenu(DialougeChoice, StringHolder[0 :: 2], TextX = 300, TextY = 512, TextColor = (255, 255, 255))
        elif type(StringHolder) is list:
            TextCooler(StringHolder[0].split("|"), (255, 255, 255), (300, 512))
        else:
            TextCooler(StringHolder.split("|"), (255, 255, 255), (300, 512))
    if DeadLol == True:
        ScreenTemp = screen.copy()
        apply_grayscale_filter(ScreenTemp)
        screen.blit(ScreenTemp, (0, 0))
    pygame.display.flip()  # Update the display
    if DeadLol == True:
        pygame.time.delay(200)
        
    else:
        pygame.time.delay(100)  # Delay to prevent using too much CPU

pygame.quit()