#!python3 
#This program is an experiment to help me learn how to write code that detects key presses so I can add a function to my prayer room.
#This let's Python listen to the keyboard.
from pynput import keyboard 

#This remembers whether the control key is being held down.
controlPressed = False 
#Prevents multiple prints of the keyboard command to the screen.
keyboardCommandAlreadyPressed = False

#this runs whenever any key is pressed.
def onKeyPress(key):
    #use the same controlPressed variable everywhere.
    global controlPressed 
    global keyboardCommandAlreadyPressed

    #If either control key is pressed.
    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        #Remember that control is down.
        controlPressed = True
    #If control is down and the left arrow is pressed.
    if controlPressed and key == keyboard.Key.left and not keyboardCommandAlreadyPressed:
        print("Control + Left Arrow Pressed!")
        keyboardCommandAlreadyPressed = True 
    #If control is down and the up arrow is pressed.
    if controlPressed and key == keyboard.Key.up and not keyboardCommandAlreadyPressed:
        print("Control + Up Arrow Pressed!")
        keyboardCommandAlreadyPressed = True 
    if controlPressed and key == keyboard.Key.right and not keyboardCommandAlreadyPressed:
        print("Control + Right Arrow Pressed!")
        keyboardCommandAlreadyPressed = True 
    if controlPressed and key == keyboard.Key.down and not keyboardCommandAlreadyPressed:
        print("Control + Down Arrow Pressed!")
        keyboardCommandAlreadyPressed = True 

#This runs whenever any key is released.
def onKeyRelease(key):
    global controlPressed
    global keyboardCommandAlreadyPressed
    #If any control key is released.
    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        #Remember that control is no longer down. 
        controlPressed = False
    #When an arrow key is released, allow another command later.
    if key == keyboard.Key.left or key == keyboard.Key.right or key == keyboard.Key.up or key == keyboard.Key.down:
        keyboardCommandAlreadyPressed = False
    #If escape is pressed, stop the program.
    if key == keyboard.Key.esc:
        print("Exiting program.")
        #Tells pynput to stop listening.
        return False

#This starts the keyboard listener.
with keyboard.Listener(
    #What to do when a key is pressed.
    on_press=onKeyPress,
    #What to do when a key is released.
    on_release=onKeyRelease
) as listener:
    print("Listening for keys.  Press Escape to quit.")    
    listener.join()




