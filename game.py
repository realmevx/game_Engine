import os
import time

charHealth = 100
charIntelligence = 100
charWisdom = 100
charStrength = 100
charAgility = 100
charPoints = 400
homeLand = ""
name = ""
currentLocation = ""

def ASCII_ART(value):

    match value:
        case 'mountains':

            mountains = (r"""        _    .  ,   .           .
                *  / \_ *  / \_      _  *        *   /\'__        *
                  /    \  /    \,   ((        .    _/  /  \  *'.
             .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
                /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
              /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \
             /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
            /        `.  / /       `.~-^=-=~=^=.-'      '-._ `._
            """)
            return mountains
        case _:
            return 0


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def Gameover():
    print("Game over.")
    return 0

def birthPlace(homeLand):
    birth = input()
    if birth == "1":
        homeLand = ("Wladsmogr")
        return homeLand
    else:
        Gameover()

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Room():
    print("You enter a dark chamber")


def Print():
    print("Hello")

def extract(list, x):
    return [item[x] for item in list]


def mapStart(homeValue):

    match homeValue:
        case '1':
            Wladsmogr()
        case _:
            print("NO HOMELAND")
            return 0

def discover():
    #print(currentLocation)
    currentItems = (getItems())
    currentItemNames = extract(currentItems, 0)

    print("The location contains the following objects: ", currentItemNames)

def items(itemName):

    match itemName:
        case 'bed':
            bedFight = [["You walk up to the bed and kick it, but fail to make any impact whatsoever.", 0],["You use your immense strength to shatter the bed with your bare fists", 9]]
            bedUse = [["You decide to get in bed, to get some rest", 9]]
            bedIdentify = [["The bed is very primitive, but It's been serving me good for a long time", 4,5,6,7],["Ooga?", 1,2,3]]
            bed = [bedFight, bedUse, bedIdentify]
            return bed
        case 'stick':
            stickFight = [["You walk up to the stick and start violently stomping it with your foot, until only splinters remain", 9]]
            stickUse = [["You pick up the stick on the ground", 9]]
            stickIdentify = [["bla bla im smart", 8,9], ["The stick is frail and withered. That goes for most of the nature around here", 4,5,6,7], ["Oog?", 1,2,3]]
            stick = [stickFight, stickUse, stickIdentify]
            return stick
        case _:
            print("error")


def getItems():

    match currentLocation:
        case 'caveBase':
            bedItem = items("bed")
            stickItem = items("stick")
            currentItems = [["bed",bedItem],["stick",stickItem]]
            return currentItems
        case _:
            print("error")
            return 0

def skillCheck(skill):

    if skill in range(0, 30):
        return 1
    elif skill in range(30, 50):
        return 2
    elif skill in range(50, 70):
        return 3
    elif skill in range(70, 90):
        return 4
    elif skill in range(90, 110):
        return 5
    elif skill in range(110, 130):
        return 6
    elif skill in range(130, 150):
        return 7
    elif skill in range(150, 170):
        return 8
    elif skill in range(170, 190):
        return 9
    else:
        print("error, invalid skill number")


def help():
    print("Here are the ways you can influence your character:")
    print("discover, use, identify, help")

def doAction(chosenItem, chosenAction):
    currentItems = getItems()
    currentIndex = (index_2d(currentItems, chosenItem))
    currentInfo = (currentItems[currentIndex[0]][1])
    currentIdentify = currentInfo[chosenAction]
    identifyStat = (charIntelligence / 2) + (charWisdom / 2)
    identifySkill = skillCheck(identifyStat)
    outcomeIndex = (index_2d(currentIdentify, identifySkill))
    outcomeNumber = outcomeIndex[0]
    print(currentIdentify[outcomeNumber][0])

def doActionWith(chosenItem, chosenItemSecondary, chosenAction):
    print("Hello")


def decision(action):

    match action.split():
        case ["discover"]:
            discover()
        case ["identify", chosenItem]:
            doAction(chosenItem, 2)
        case ["use ", chosenItem, " with ", chosenItemSecondary]:
            doActionWith(chosenItem, chosenItemSecondary, 1)
        case ["help"]:
            help()
        case _:
            print("error")


def caveBase():
    global currentLocation
    currentLocation = ("caveBase")
    print(name + " wakes up in a cave, with only a few supplies to boot.")
    while currentLocation == ("caveBase"):

        print("What did your character do next?")
        action = input(">").lower()
        decision(action)


def Wladsmogr():
    Clear()
    print("You wake up in your home land of Wladsmogr")
    print(ASCII_ART("mountains"))
    time.sleep(2)
    print("The mountains are plenty, and the terrain is almost as unforgiving as the lack of flora.")
    time.sleep(2)
    caveBase()


def game_over(reason):
    print(reason)


def charCreation():
    print("What is your character name?")
    global name
    name = input(">")
    Clear()
    print("Hello " + name)
    #print("Where do you live? (Wladsmogr: 1)")
    #homeLand = input(">").lower()
    #print("You live in " + birthPlace)
    print("Throughout this adventure, your hero will have strength and weaknesses. These will in turn help create new paths in your story, and maybe even new perks")
    time.sleep(1)
    charPoints = 400
    setStats = True
    while setStats == True:
        charPoints = 400
        global charStrength
        global charIntelligence
        global charWisdom
        global charAgility
        print("Please share the strengths and weaknesses of your hero")
        print("You have a total of 400 points to spend in 4 categories (Strength, Intelligence, Wisdom, Agility)")
        print("Remaining points: ", charPoints)
        print("Strength:")
        charStrength = int(input())
        charPoints = charPoints - charStrength
        print("Remaining points: ", charPoints)
        print("Intelligence:")
        charIntelligence = int(input())
        charPoints = charPoints - charIntelligence
        print("Remaining points: ", charPoints)
        print("Wisdom:")
        charWisdom = int(input())
        charPoints = charPoints - charWisdom
        print("Remaining points: ", charPoints)
        print("Agility:")
        charAgility = int(input())
        charPoints = charPoints - charAgility
        print("Your current strengths and weaknesses are: Strength: ",  charStrength, " Intelligence: " , charIntelligence , " Wisdom: " , charWisdom , " Agility: " , charAgility)

        if charPoints == 0:
            setStats = False
            print("Let me write that down")
        else:
            setStats = True
            print("Please speak some sense!")
    time.sleep(2)
    return homeLand

def mapSelect():
    print("Where do you live? (Wladsmogr: 1)")
    homeLand = input(">").lower()
    return homeLand


def Start():
    Clear()
    print("Hello")
    print("Welcome to an adventure")
    charCreation()
    homeLand = mapSelect()
    mapStart(homeLand)

Start()
