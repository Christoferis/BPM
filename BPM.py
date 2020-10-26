#Note: COmmit, implement vars correctly

#Imports
from tkinter import Tk, Label, Button, IntVar
from statistics import median
from time import time

#vars
pastbpm = list()
starttime = float()
endtime = float()

#main window
root = Tk()
root.title("Tap BPM")
root.geometry("300x75")

#callback for time
def BPM(bpmtxt):
    global starttime, endtime, pastbpm
    #Stop the clock
    endtime = time()
    #Calculate BPM using formula (BPM = 60 / (TimeEnd - TimeStart)) number of beats of this length fitting in a Minute
    if starttime != 0:
        bpm = round(60 / (endtime - starttime), 0) #Formula
    else:
        bpm = 0

    #median and list to flatten out the final answer
    if len(pastbpm) <= 5:
        pastbpm.append(bpm)
    else:
        del pastbpm[0]

    #update text
    bpmtxt.config(text=median(pastbpm))
    #restart clock
    starttime = time()


#main GUI
def GUI():
    global root
    #text
    Label(root, text="Press the Button to tap BPM").pack()
    #Button and BPM Label
    bpm = Label(root, background="grey", foreground="white", text="Tap to start")
    but = Button(root, text="Press me", command=lambda: BPM(bpm))
    but.pack()
    bpm.pack()

#run GUI
GUI()

#mainloop
root.mainloop()



