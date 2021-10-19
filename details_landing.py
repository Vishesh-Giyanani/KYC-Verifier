from tkinter import *
from typing import Sized
from PIL import Image, ImageTk

from sqlhelp import SQLinitialize
from selection1 import Selection1

'''img = PhotoImage(file='ass.png') 
root.iconphoto(False, img)
'''
def getval():
    genderval = gendervalue.get()
    nameval=namevalue.get()
    emailval=emailvalue.get()
    contactval=contactvalue.get()
    dobval=dobvalue.get()
    paymentval=paymentvalue.get()
    pinval=pinvalue.get()
    stateval=statevalue.get()
    reg=sql.register(nameval,emailval,contactval,dobval,paymentval,pinval,stateval,genderval)
    if(reg==True):
        lbl = Label(root, text="Submitted!").grid(row=16, column=3, pady=10)
        root.destroy()
        Selection1(sql,nameval)
        print("Submitted")
    else:
        lbl = Label(root, text=reg).grid(row=16, column=3, pady=10)
        

root = Tk()
root.title("                                                                                                                                                                                                                 KYC Verifier")
root.resizable(0, 0)
canvas_width = 1366
canvas_height = 768
root.geometry(f"{canvas_width}x{canvas_height}")
sql=SQLinitialize()

Label(root, text="KYC Details", font="Raleway 13 bold", pady=15).grid(row=0, column=3)

name = Label(root, text="   Enter Name")
email = Label(root, text="   Enter Email")
contact = Label(root, text="   Contact Number")
dob = Label(root, text="   Enter Birth Year")
residense= Label(root, text="   Enter City")
pin = Label(root, text="   Enter Pincode")
state= Label(root, text="   Enter State")
gender = Label(root, text="   Enter Gender")

name.grid(row=1, column=2, pady=15, sticky=W)
email.grid(row=2, column=2, pady=15, sticky=W)
contact.grid(row=3, column=2, pady=15, sticky=W)
dob.grid(row=4, column=2, pady=15, sticky=W)
residense.grid(row=5, column=2, pady=15, sticky=W)
pin.grid(row=6, column=2, pady=15, sticky=W)
state.grid(row=7, column=2, pady=15, sticky=W)
gender.grid(row=8, column=2, pady=15, sticky=W)

namevalue = StringVar()
emailvalue = StringVar()
contactvalue = StringVar()
dobvalue = StringVar()
paymentvalue = StringVar()
residensevalue = StringVar()
pinvalue = StringVar()
statevalue = StringVar()

pdfselect1 = IntVar()
pdfselect2 = IntVar()
pdfselect3 = IntVar()

nameentry = Entry(root, textvariable=namevalue)
emailentry = Entry(root, textvariable=emailvalue)
contactentry = Entry(root, textvariable=contactvalue)
dobentry = Entry(root, textvariable=dobvalue)
residenseentry = Entry(root, textvariable=residensevalue)
pinentry = Entry(root, textvariable=pinvalue)
stateentry = Entry(root, textvariable=statevalue)

pdfselect1 = Checkbutton (root, text="Aadhar Card", variable=Checkbutton, onvalue = 1, offvalue = 0, height = 2, width = 10, highlightcolor = "#A8F5EF")
pdfselect2 = Checkbutton (root, text="PAN Card", variable=Checkbutton, onvalue = 1, offvalue = 0, height = 2, width = 10 , highlightcolor = "#A8F5EF")
pdfselect3 = Checkbutton (root, text="Drivers Licsense", variable=Checkbutton, onvalue = 1, offvalue = 0, height = 2, width = 10 , highlightcolor = "#A8F5EF")

nameentry.grid(row=1, column=3, padx=520)
emailentry.grid(row=2, column=3, padx=520)
contactentry.grid(row=3, column=3, padx=520)
dobentry.grid(row=4, column=3, padx=520)
residenseentry.grid(row=5, column=3, padx=520)
pinentry.grid(row=6, column=3, padx=520)
stateentry.grid(row=7, column=3, padx=520)

pdfselect1.grid(row = 11, column=3, padx=520)
pdfselect2.grid(row = 12, column=3, padx=520)
pdfselect3.grid(row = 13, column=3, padx=520)

list_gender=["Male","Female","Other","Prefer not to say"]
gendervalue=StringVar()
gendervalue.set(list_gender[0])
pck=OptionMenu(root,gendervalue,*list_gender)
pck.config(width=15,font=("Arial",10))
pck.grid(row=8, column=3, padx=520)

Button(text="Register", fg="black", command=getval,relief = RIDGE, activebackground="#9FDAF2", activeforeground = "#ffffff", width = 20,height=1).grid(row=15, column=3, pady=55)
class documents:
    def __init__(self) -> None:
        pass
root.mainloop()