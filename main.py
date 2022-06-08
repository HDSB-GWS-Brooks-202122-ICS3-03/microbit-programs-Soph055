import music
import speech
from microbit import sleep
from microbit import *


while True:
    if button_a.was_pressed():
        # The say method attempts to convert English into phonemes.
#         speech.say("I can sing!")
#         sleep(500)
#         speech.say("Listen to me!")
#         sleep(500)
        
        tune = ["A3:2", "B3:2", "C4:2", "D4:2", "E4:2", "C4:2", "E4:4", "D#4:2", "B3:2","D#4:4",
                "D4:2", "B3:2","D4:4", "A3:2", "B3:2", "C4:2", "D4:2", "E4:2", "C4:2", "E4:2",
                "A4:2", "G4:2", "E4:2", "C4:2", "E4:2","G4:8", "A4:2", "B4:2", "C5:2", "D5:2", "E5:2", "C5:2", "E5:4",]
        music.play(tune)
    
    