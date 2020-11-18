#Note: COmmit, implement vars correctly

#Imports
from tkinter import Tk, Label, Button, Frame
from tkinter.ttk import Notebook
from statistics import median
from time import time

#vars
pastbpm = list()
starttime = float()
endtime = float()

#main window
root = Tk()
root.title("Tap BPM")
root.geometry("300x150")

#BPM Functions
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

def BPM_GUI(tabs):
    #make frame for easier stuff
    bpm_frame = Frame(tabs)
    #text
    Label(bpm_frame, text="Press the Button to tap BPM").pack()
    #Button and BPM Label
    bpm = Label(bpm_frame, background="grey", foreground="white", text="Tap to start", pady=5)
    but = Button(bpm_frame, text="Press me", command=lambda: BPM(bpm), height=2, width=8, background="green", foreground="white",)
    bpm.pack()
    but.pack()

    return bpm_frame


#Tick functions

def Tick_GUI(tabs):
    #Frame cuz easier
    tick_frame = Frame(tabs)

    

    return tick_frame


#main GUI
def GUI():
    #Main Notebook
    global root
    tabs = Notebook(root)

    #Add Tabs
    tabs.add(BPM_GUI(tabs))

    tabs.pack(fill="both", expand=1)



#run GUI
GUI()

#mainloop
root.mainloop()



