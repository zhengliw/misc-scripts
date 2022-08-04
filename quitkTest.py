#!/bin/usr/python3
from turtle import width
import quitk
import threading
import tkinter
from time import sleep, time
window = quitk.Quitk(title="Clicker")

# Kurz comment aus langeweile

text = tkinter.Label(window, text="0", font=("Microsoft YaHei", 30), bg=window.bgcolor, fg=window.fgcolor)
text.pack()
thread = threading.Thread(target=None)
started = False
countdownTime = 5.00

def timerCounter():
    global started
    startTime = time()
    while time() <= startTime + countdownTime and started:
        endTime = time()
        timer.config(text="{:.2f}".format(countdownTime - round(endTime-startTime, 2)))
    timer.config(text="{:.2f}".format(countdownTime))
    btn.config(command=dummy)

def dummy():
    return

def addoneorstart():
    global started
    if started == False:
        started = True
        thread = threading.Thread(target=timerCounter)
        thread.start()
    number = text.cget("text")
    number = str(int(number) + 1)
    text.config(text=number)

def reset():
    global started
    started = False
    btn.config(command=addoneorstart)
    text.config(text="0")
    timer.config(text="{:.2f}".format(countdownTime))

btn = tkinter.Button(window, text="Click glick", command=addoneorstart, height=15, width=20, bg = window.bgcolor, fg=window.fgcolor)
btn.pack()
btn2 = window.quickButton("Reset", reset)

def clickGlick(event):
    btn.invoke()
window.bind("<KeyRelease-Return>", clickGlick)

timer = window.quickText("{:.2f}".format(countdownTime))



window.run()