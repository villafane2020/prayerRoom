#!python3 
#This program is an experiment to help me learn how to write code that detects key presses so I can add a function to my prayer room.
#This let's Python listen to the keyboard.
from pynput import keyboard 

#This remembers whether the control key is being held down.
controlPressed = False 

#this runs whenever any key is pressed.
def onKeyPress(key):
    #use the same controlPressed variable everywhere.
    global controlPressed 
    #If either control key is pressed.
    if key == keyboard.Key.ctrl_l or keyboard.Key.ctrl_r:
        #Remember that control is down.
        controlPressed = True
    #If control is down and the left arrow is pressed.
    if controlPressed and key == keyboard.Key.left:
        print("Control + Left Arrow Pressed!")
    #If control is down and the up arrow is pressed.
    if controlPressed and key == keyboard.Key.up:
        print("Control + Up Arrow Pressed!")
    if controlPressed and key == keyboard.Key.right:
        print("Control + Right Arrow Pressed!")
    if controlPressed and key == keyboard.Key.down:
        print("Control + Down Arrow Pressed!")

#This runs whenever any key is released.
def onKeyRelease(key):
    global controlPressed
    #If the left control key is released.
    if key == keyboard.Key.ctrl_l:
        #Remember that control is no longer down. 
        controlPressed = False
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




