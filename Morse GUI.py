import time
from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# hardware
led = LED(14)
delay = 0.35

def dah():
    led.on()
    time.sleep(4*delay)
    led.off()
    time.sleep(delay)
    
def dit():
    led.on()
    time.sleep(delay)
    led.off()
    time.sleep(delay)
    
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}

def Morse_Translation(sentence):
    sentence = sentence.upper()
    encodedsentence = ""
    for character in sentence:
        encodedsentence += MORSE_CODE_DICT[character] + " "
    return encodedsentence
    
def Flash_Code():
    
    sentence = inputbox.get("1.0", "end-1c")
    encodedsentence = Morse_Translation(sentence[0:12])
    print(encodedsentence)
   
    for i in encodedsentence:
        if i == ".":
            dit()
        elif i == "-":
            dah()
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
        
# GUI Definitons
win = Tk()
win.geometry("310x150")
win.title("Morse to Blink")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

# Widgets
inputbox = Text(win, height = 5, width = 38)
inputbox.grid(row = 1, column = 1)

Flash = Button(win, text = 'Flash', font = myFont, command = lambda:Flash_Code(), bg = 'yellow', height = 1, width = 6)
Flash.grid(row = 2, column = 1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'pink', height = 1, width = 6)
exitButton.grid(row = 3, column = 1)

# Exit cleanly
win.protocol("WM_DELETE WINDOW", close)

# Loop forever
win.mainloop()
    
