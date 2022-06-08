import music
import speech
from microbit import sleep
from microbit import *

Song = "In The Hall Of The Mountain King"

while True:
     
    if button_a.was_pressed():
        # The say method attempts to convert English into phonemes.
        speech.say("Let me play you a song.")
        sleep(500)
        speech.say("Wish me luck!")
        sleep(500)
        
        tune = ["A3:2", "B3:2", "C4:2", "D4:2", "E4:2", "C4:2", "E4:4", "D#4:2", "B3:2","D#4:4",
                "D4:2", "B3:2","D4:4", "A3:2", "B3:2", "C4:2", "D4:2", "E4:2", "C4:2", "E4:2",
                "A4:2", "G4:2", "E4:2", "C4:2", "E4:2","G4:8", "A4:2", "B4:2", "C5:2", "D5:2",
                "E5:2", "C5:2", "E5:4", "D#5:2", "B4:2","D#5:4","D5:2", "B4:2","D5:4", "A4:2",
                "B4:2", "C5:2", "D5:2", "E5:2", "C5:2", "E5:2","A5:2", "G5:2", "E5:2", "C5:2",
                "E5:2","G5:8",]
        
        display.scroll(str(Song), wait=False, loop=False)
        music.play(tune)
        
    if button_a.was_pressed():
        