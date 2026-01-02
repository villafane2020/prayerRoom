#!python3

import functions as fun

choice = ''
fun.playMusic(choice)
#user is welcomed and is given a description of the prayer room and told how to access help.
fun.printFileToScreen('welcome.txt', )
#While loop that runs constantly in the background of the prayer room waiting for user to input a command.
#This loop permits the user to type in commands to read all four walls, the ceiling, and floor.
    #Variable to store file path to display and interact with each file or wall so I do not have to repeat the path to the diferent walls or files.
surfacePath = 'surfacesToWriteOn\\'
#even though I had a way to check that the OS was Linux or Windows, I still had to store what that function returned in a variable in order to get it to override original variable.
surfacePath = fun.osChecker(surfacePath)
#exit()
#print("Debugging4:",  surfacePath)
while True:
    #variable created to store user input.
    choice = input("Please type a command to interact with the prayer room:")
    if choice == 'quit':
        fun.clearScreen()
        print("See you next time.")

        break 
    elif choice == 'help':
        fun.printFileToScreen('help.txt')
    elif choice == 'front':
        fun.surfaceIntro(choice)
        fun.printFileToScreen('front.txt', surfacePath)
    elif choice == 'left':
        fun.surfaceIntro(choice)
        fun.printFileToScreen('left.txt', surfacePath)
    elif choice == 'right':
        fun.surfaceIntro(choice)
        fun.printFileToScreen('right.txt', surfacePath)
    elif choice == 'back':
        fun.surfaceIntro(choice)
        fun.printFileToScreen('back.txt', surfacePath)
    elif choice == 'ceiling':
        fun.surfaceIntro(choice)
        fun.printFileToScreen('ceiling.txt', surfacePath)
    elif choice == 'floor':
        fun.surfaceIntro(choice)
        fun.printFileToScreen('floor.txt', surfacePath)
    elif choice == 'prayer':
        fun.phraseCollector(choice, surfacePath, 'front.txt')
    elif choice == 'scripture':
        fun.phraseCollector(choice, surfacePath, 'left.txt')
    elif choice == 'note':
        fun.phraseCollector(choice, surfacePath, 'floor.txt')
    elif choice == 'remove':
        fun.removeItem(surfacePath)
    elif choice == 'move':
        fun.moveItem(surfacePath)
    elif choice == 'stop':
        fun.playMusic(choice)





#Make sure code is clear and readable and can be understood 6 months from now.
#Setup music in your prayer room.
#put all your experimental code in a folder so you can refer back to them in the future.  Rename files so that you will know what each code snippet refers to. 
#upload your code to GITHub so that you will not lose it and always have it on line.



