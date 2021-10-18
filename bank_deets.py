from tkinter import *
from typing import Sized

root = Tk()

root.title("                                                                                                                                                                                                                 KYC Verifier")
root.resizable(0, 0)

canvas_width = 1366
canvas_height = 768
root.geometry(f"{canvas_width}x{canvas_height}")

Label(root, text="Bank Account Details", font="Raleway 13 bold", pady=30,padx = 100).grid(row=0, column=3,)

name = Label(root, text="   Enter Account Holder Name")
acc_num = Label(root, text="   Enter Account Number")
ifsc = Label(root, text="   Enter IFSC Code")


name.grid(row=1, column=2,  sticky=W)
acc_num.grid(row=2, column=2,  sticky=W)
ifsc.grid(row=3, column=2,  sticky=W)


namevalue = StringVar()
acc_numvalue = StringVar()
ifscvalue = StringVar()


nameentry = Entry(root, textvariable=namevalue)
acc_numentry = Entry(root, textvariable=acc_numvalue)
ifscentry = Entry(root, textvariable=ifscvalue)


nameentry.grid(row=1, column=3, padx=520)
acc_numentry.grid(row=2, column=3, padx=520)
ifscentry.grid(row=3, column=3, padx=520)


def panism():
    pan = Label(root, text="   Enter PAN Card Number")
    pan.grid(row=4, column=2, sticky=W)
    panvalue = StringVar()
    panentry = Entry(root, textvariable=panvalue)
    panentry.grid(row=4, column=3, padx=50)

#Checkbox
pancheck = Checkbutton (root, text="Do you own a Pan Card", variable=Checkbutton,command=panism, onvalue = 1, offvalue = 0, height = 4, width = 100, highlightcolor = "#A8F5EF")
pancheck.grid(row = 8, column=3, pady=100)

root.mainloop()