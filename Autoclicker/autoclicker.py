import time
import threading
import pyautogui
import keyboard
from tkinter import *

#Makes the basic window
window = Tk()
window.title('AutoClicker')

#Functions
def clickedStart():
    time.sleep(3)

    run = True
    intervalInt = None

    try:
        intervalInt = int(txt.get())
    except:
        pass

    start = time.time()

    while run == True:
        if keyboard.is_pressed('b'):
            break

        if intervalInt != None:
            if time.time() >= (start + intervalInt):
                pyautogui.click()
                start = time.time()
        else:
            pyautogui.click()


#buttons a cool stuff
lbl = Label(window, text = 'Auto Clicker go BRRR')
lbl.grid(column = 1, row = 0, padx = (75,10))

txt = Entry(window, width = 10)
txt.grid(column = 1, row = 1, padx = (75,10))

btn = Button(window, text = 'Start Brrrr', command = clickedStart, bg = 'green', fg = 'Lightgreen')
btn.grid(column = 1, row = 2, padx = (75, 10))

window.geometry('250x100')

photo = PhotoImage(file = 'Cock.png')
window.iconphoto(False, photo)

window.mainloop()

