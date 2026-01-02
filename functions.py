#!python3 
import os 
#The following line must be in this order:  after importing os and before importing pygame.
#The following line prevents pygame from displaying the hello message along with the website which is called a support prompt. 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time
import pygame
#Helps code figure out what operating system is being used.
import platform

def clearScreen():
    """Clears the screen in the windows command line."""
    """Clears screen of previous items so only newer items can be displayed; looks neater and allows user to focus on newer items; this is sprinkled throughout program."""
    """Also, this function has code which checks whether OS is Linux or Windows and clears the screen accordingly."""
    operatingSystem = platform.system()
    if operatingSystem == "Linux":
        os.system('clear')
    else:
        os.system('cls')

def printFileToScreen(fileName, surfacePath=None):
    """Prints the contents of any file to the screen."""
    """This function has 2 optional arguements so that you can direct the code to a file in a specific folders or a file in no folder if necessary."""
    clearScreen()
    #If you need to get to a file that is not in the surfaces folder.
    if surfacePath == None:
        with open(fileName, 'r') as f:
            contents = f.read()
            print(contents)
        #If you want to read files on a particular surface.
    elif surfacePath is not None:
        fileName = surfacePath + fileName
        #This variable also contains file name and path to be transferred to other functions.
        originalFileName = fileName
        with open(fileName, 'r') as f:
            contents = f.read()
            print(contents)

def phraseCollector(choice, surfacePath, fileName):
    """Depending on user's choice, sends written text to the appropriate file; in the correct folder; whether it be a prayer, scripture, or positive quote."""
    clearScreen()
    phrase = input(f'Please write your {choice} below:\n')        
    #The user's phrase is sent to the right file in the right folder with the correct path.
    fileName = surfacePath + fileName
    with open(fileName, "a") as f:
        f.write(phrase + '\n---\n')
        print(f'Your {choice} has been successfully added to the appropriate surface.')
        #Time module and clearScreen() function are added here so that when message shows that your text has been added, message will disappear after 4 seconds.
        time.sleep(2)
        clearScreen()

def removeItem(surfacePath):
    """Removes items from specific surfaces (a wall, ceiling, floor, etc)."""
    clearScreen()
    choice = input("Which surface do you want to remove the item from?")
    #"txt" is added to the user's choice so they can remove items from the correct surface.
    #Choice actually becomes a file a direct path and file name to a file.
    fileName = surfacePath + choice + '.txt'
    #This upcoming code sets up a way to show user list of items he might want to remove.
    # A list is created to store phrases from a text file.
    phrases = []
    # A dictionary is created to store phrases with associated future numbers as keys.
    numberedPhrases = {}
    # This code opens the file and reads it.
    with open(fileName, 'r') as f:
        lines = f.readlines()
    # Now we deal with the lines being read and taken from the file; not changing the original file.
    for line in lines:  
        # Strip the return symbol and spaces from each line and put that line in a variable.
        strippedLine = line.strip('\n')
        #Since my walls have text written with dashes to separate text and to entitle the top of file, this code ignores lines with the dash symbol.
        if '-' in line:
            continue
        #This if statement is here in case the end of your document has blank lines and you don't want blank lines to show up as items in your list or dictionary.
        if not strippedLine:
            continue
        # Add that neat and clean line to the above phrases list.
        phrases.append(strippedLine)
        # Use the length of the above phrases list to create number keys for the items in the dictionary.
        # This puts each item or value in the dictionary with a number key.
        numberedPhrases[len(phrases)] = strippedLine
    clearScreen()
    #Print out the items so user can see all numbered items and make a choice.
    for key, value in numberedPhrases.items():
        print(f"{key}. {value}")
    #This gives the user the option to erase text written on a surface.
    #Int is used here to insure that the key you are searching for in the dictionary is a number.
    numberToErase = int(input("Please type the number of the item that you wish to remove:  "))
    #The item is removed from the dictionary.
    numberedPhrases.pop(numberToErase)
    print(f"Item {numberToErase} has been removed.")
    time.sleep(3)
    clearScreen()
    #Now, for the taking of the numberedPhrases dictionary values and using them to replace the entire file or 'fileName' above.
    with open(fileName, 'w') as f:
        for key, value in numberedPhrases.items():
            #write the dictionary values back to the file.
            f.write(f"{value}" + "\n---\n")

def surfaceIntro(choice):
    """Depending on the user's choice, tells user what wall or surface they are looking at."""
    if choice == 'front':
        print("--You are facing the front wall which shows a list of your current prayer requests.--")
        time.sleep(3)
    elif choice == 'back':
        print("--On the wall behind you is a list of answered prayers.")
        time.sleep(3)
    elif choice == 'left':
        print("--On your left is a wall with encouraging scripture.--")
        time.sleep(3)
    elif choice == 'right':
        print("--On your right is displayed a list of encouraging scripture you have already learned.--")
        time.sleep(3)
    elif choice == 'floor':
        print("--On the floor, in front of your feet, are encouraging notes and phrases.")
        time.sleep(3)
    elif choice == 'ceiling':
        print("--On the ceiling, above your head, are past encouraging notes and phrases.")
        time.sleep(3)

def playMusic(choice):
    """uses pygame to start the playing of a music file in the prayer room."""
    #Initialize pygame for sounds.
    pygame.init()
    #load sound effects.
    natureSounds = pygame.mixer.Sound('natureSounds.mp3')
    pygame.mixer.Sound.play(natureSounds, loops=-1)
    if choice == 'stop':
        natureSounds.stop()
        pygame.quit()

def moveItem(surfacePath):
    """Moves items from specific surfaces (a wall, ceiling, floor, etc) and puts them on another specific place."""
    "For example, puts old prayers on older surface or old quotes on older surface."
    "This function is under construction."
    clearScreen()
    choice = input("Which surface do you want to move the item from?")
    choiceTwo = input("Which surface do you want to send the item to?")
    #"txt" is added to the user's choice so they can move items to the correct surface.
    #Choice actually becomes a file a direct path and file name to a file.
    fileName = surfacePath + choice + '.txt'
    #This upcoming code sets up a way to show user list of items he might want to move.
    # A list is created to store phrases from a text file.
    phrases = []
    # A dictionary is created to store phrases with associated future numbers as keys.
    numberedPhrases = {}
    #A second list is created to hold items that will be moved to another surface.
    numberedPhrasesTwo = {}
    # This code opens the file and reads it.
    with open(fileName, 'r') as f:
        lines = f.readlines()
    # Now we deal with the lines being read and taken from the file; not changing the original file.
    for line in lines:  
        # Strip the return symbol and spaces from each line and put that line in a variable.
        strippedLine = line.strip('\n')
        #Since my walls have text written with dashes to separate text and to entitle the top of file, this code ignores lines with the dash symbol.
        if '-' in line:
            continue
        #This if statement is here in case the end of your document has blank lines and you don't want blank lines to show up as items in your list or dictionary.
        if not strippedLine:
            continue
        # Add that neat and clean line to the above phrases list.
        phrases.append(strippedLine)
        # Use the length of the above phrases list to create number keys for the items in the dictionary.
        # This puts each item or value in the dictionary with a number key.
        numberedPhrases[len(phrases)] = strippedLine
    clearScreen()
    #Print out the items so user can see all numbered items and make a choice.
    for key, value in numberedPhrases.items():
        print(f"{key}. {value}")
    #This gives the user the option to erase text written on a surface.
    #Int is used here to insure that the key you are searching for in the dictionary is a number.
    numberToMove = int(input("Please type the number of the item that you wish to move:  "))
    #The item is moved from one dictionary to another.
    numberedPhrasesTwo[numberToMove] = numberedPhrases.pop(numberToMove)
    #print("Debug: ", numberedPhrases, numberedPhrasesTwo)
    print(f"Item {numberToMove} has been moved.")
    time.sleep(2)
    clearScreen()
    #Now, for the taking of the numberedPhrases dictionary values and using them to override the entire surface file you were moving data from.
        #choice actually becomes a file a direct path and file name to the original file.
    fileName = surfacePath + choice + '.txt'
    with open(fileName, 'w') as f:
        for key, value in numberedPhrases.items():
            #write the dictionary values back to the file.
            f.write(f"{value}" + "\n---\n")
    #Now, for the taking of the numberedPhrasesTwo dictionary values and using them to append to the entire file or 'fileName' above.
        #choiceTwo actually becomes a file a direct path and file name to a file.
    fileName = surfacePath + choiceTwo + '.txt'
    with open(fileName, 'a') as f:
        for key, value in numberedPhrasesTwo.items():
            #write the dictionary values back to the file.
            f.write(f"{value}" + "\n---\n")

def osChecker(surfacePath):
    """Determines which OS the program is running in and adjusts the \ to / in Linux."""
    operatingSystem = platform.system()
    if operatingSystem == "Linux":
        surfacePath = "surfacesToWriteOn/"
    return surfacePath




