from tkinter import *
from typing import Sized
from PIL import Image, ImageTk
import PyPDF2
 
root = Tk()
 
def home_button_press():
    print("hello")

#Window Framework
root.geometry("1366x768")
root.title("KYC Verifier")
root.configure(bg = "#0CA418")
root.resizable(0, 0)

img = PhotoImage(file='ass.png') 
root.iconphoto(False, img)

#Elements
"""text1 = Label(root, text="KYC      ", fg = "#0CA418", font="Gotham 120 bold", bg= "#ffffff").grid(row=4, column=1)
text2 = Label(root, text="Verifier", fg = "#077324", font="Gotham 120 bold").grid(row=5, column=1)"""

'''button1 = Button(root, text = "Get Started!", command = home_button_press)
button1.configure(width = 50, background = "#000000", relief = SUNKEN)
button1.pack(side=BOTTOM,anchor="ne")'''


button1 = Button(root, text = "Quit", command = home_button_press)
button1.configure(width = 10, activebackground = "#33B5E5", relief = SUNKEN)
button1.grid(row=18, column=1, sticky=W, pady=200)

#Function calls
root.mainloop()