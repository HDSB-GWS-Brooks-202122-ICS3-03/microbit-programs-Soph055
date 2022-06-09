import music
import speech
from microbit import sleep
from microbit import *
import random


Song = "In The Hall Of The Mountain King"

while True:
    
    ballAnswers = [ "no way",
                       "yup",
                       "nah",
                       "never",
                       "ye",
                       "YES",
                       "prob not",
                       "maybe",
                       "no",]
     
    display.show("8")
    if accelerometer.was_gesture("shake"):
         display.clear()
         sleep(500)
         display.scroll(random.choice(ballAnswers))
         
     
    if button_a.was_pressed():
        
        tune = ["A3:2", "B3:2", "C4:2", "D4:2", "E4:2", "C4:2", "E4:4", "D#4:2", "B3:2","D#4:4",
                "D4:2", "B3:2","D4:4", "A3:2", "B3:2", "C4:2", "D4:2", "E4:2", "C4:2", "E4:2",
                "A4:2", "G4:2", "E4:2", "C4:2", "E4:2","G4:8", "A4:2", "B4:2", "C5:2", "D5:2",
                "E5:2", "C5:2", "E5:4", "D#5:2", "B4:2","D#5:4","D5:2", "B4:2","D5:4", "A4:2",
                "B4:2", "C5:2", "D5:2", "E5:2", "C5:2", "E5:2","A5:2", "G5:2", "E5:2", "C5:2",
                "E5:2","G5:8",]
        
        display.scroll(str(Song), wait=False, loop=False)
        music.play(tune)
        
    if button_a.was_pressed(): 
       pass
        
        
        
        