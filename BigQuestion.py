from logging import root
import random
import sys
import tkinter


root = tkinter.Tk()

rd = random.randint(1,4)
#file = []
img = tkinter.PhotoImage(file="food/{}.jpeg".format(rd))

imgLabel = tkinter.Label(root, img)

imgLabel.pack()

root.mainloop()

