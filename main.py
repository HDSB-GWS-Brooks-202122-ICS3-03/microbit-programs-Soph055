import music
import speech
from microbit import sleep
from microbit import *
import random


answer = "SHEEP" # answer for guessing game
game = "G is a guessing game Shake for hint click B for answer" # instructions for guessing game


while True:
    
    animal = [ "White", # list with hints to help guess animal
                "big",
                "animal",
                "fluffy",
                "bhaa",]
    
    

    display.show("G") # displays instruction
    sleep(1000) # waits a little bit
    if accelerometer.was_gesture("shake"): # if microbit is shaked
        display.clear() # clears display
        sleep(500) # waits a little
        display.scroll(random.choice(animal)) # picks random hint from animal list and shows it through scrolling letters
             
    elif button_b.was_pressed(): # if button B is pressed
        
        tune = ["A3:2", "B3:2", "C4:2", "D4:2", "E4:2", "C4:2", "E4:4", "D#4:2", "B3:2","D#4:4", # creates a tune list which contains all notes for song
                "D4:2", "B3:2","D4:4", "A3:2", "B3:2", "C4:2", "D4:2", "E4:2", "C4:2", "E4:2",
                "A4:2", "G4:2", "E4:2", "C4:2", "E4:2","G4:8", "A4:2", "B4:2", "C5:2", "D5:2",
                "E5:2", "C5:2", "E5:4", "D#5:2", "B4:2","D#5:4","D5:2", "B4:2","D5:4", "A4:2",
                "B4:2", "C5:2", "D5:2", "E5:2", "C5:2", "E5:2","A5:2", "G5:2", "E5:2", "C5:2",
                "E5:2","G5:8",]
        
        display.scroll(str(answer), wait=False, loop=True) # displays asnwer to guessing game (and loops)
        music.play(tune) # plays song
        
    elif button_a.was_pressed(): # if button a is pressed
        
        display.clear() # clears display
        display.scroll(str(game), wait=False, loop=False) # scrolls through instruction letter by letter
        sleep(37000) # waits for amount needed in order for all instruction to be displayed
        
       
        

        
        
        
        