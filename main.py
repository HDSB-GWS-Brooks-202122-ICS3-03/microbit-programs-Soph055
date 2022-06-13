import music
import speech
from microbit import sleep
from microbit import *
import random


song = "In The Hall Of The Mountain King"
game = "G is a guessing game Shake for hint"


while True:
    
    animal = [ "White",
            "big",
            "animal",
            "fluffy",
            "bhaa",]
    
    
#     display.scroll(str(gameOne), wait=False, loop=False)
    display.show("G")
    sleep(1000)
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(500)
        display.scroll(random.choice(animal))
             
    elif button_a.was_pressed():
        
        tune = ["A3:2", "B3:2", "C4:2", "D4:2", "E4:2", "C4:2", "E4:4", "D#4:2", "B3:2","D#4:4",
                "D4:2", "B3:2","D4:4", "A3:2", "B3:2", "C4:2", "D4:2", "E4:2", "C4:2", "E4:2",
                "A4:2", "G4:2", "E4:2", "C4:2", "E4:2","G4:8", "A4:2", "B4:2", "C5:2", "D5:2",
                "E5:2", "C5:2", "E5:4", "D#5:2", "B4:2","D#5:4","D5:2", "B4:2","D5:4", "A4:2",
                "B4:2", "C5:2", "D5:2", "E5:2", "C5:2", "E5:2","A5:2", "G5:2", "E5:2", "C5:2",
                "E5:2","G5:8",]
        
        display.scroll(str(song), wait=False, loop=False)
        music.play(tune)
        
    elif button_b.was_pressed():
        
        display.clear()
        display.scroll(str(game), wait=False, loop=False)
        sleep(25000)
        
       
        

        
        
        
        