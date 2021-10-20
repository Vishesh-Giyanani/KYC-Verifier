from tkinter import *

from sqlhelp import SQLinitialize
from selection1 import Selection1

'''img = PhotoImage(file='ass.png') 
root.iconphoto(False, img)
'''

class DetailsLanding:
    def __init__(self):
        self.root = Tk()
        self.root.title("                                                                                                                                                                                                                 KYC Verifier")
        self.root.resizable(0, 0)
        canvas_width = 1366
        canvas_height = 768
        self.root.geometry(f"{canvas_width}x{canvas_height}")
        self.sql=SQLinitialize()

        Label(self.root, text="KYC Details", font="Raleway 13 bold", pady=15).grid(row=0, column=3)

        name = Label(self.root, text="   Enter Name")
        email = Label(self.root, text="   Enter Email")
        contact = Label(self.root, text="   Contact Number")
        dob = Label(self.root, text="   Enter Birth Year")
        residense= Label(self.root, text="   Enter City")
        pin = Label(self.root, text="   Enter Pincode")
        state= Label(self.root, text="   Enter State")
        gender = Label(self.root, text="   Enter Gender")

        name.grid(row=1, column=2, pady=15, sticky=W)
        email.grid(row=2, column=2, pady=15, sticky=W)
        contact.grid(row=3, column=2, pady=15, sticky=W)
        dob.grid(row=4, column=2, pady=15, sticky=W)
        residense.grid(row=5, column=2, pady=15, sticky=W)
        pin.grid(row=6, column=2, pady=15, sticky=W)
        state.grid(row=7, column=2, pady=15, sticky=W)
        gender.grid(row=8, column=2, pady=15, sticky=W)

        self.namevalue = StringVar()
        self.emailvalue = StringVar()
        self.contactvalue = StringVar()
        self.dobvalue = StringVar()
        self.paymentvalue = StringVar()
        self.residensevalue = StringVar()
        self.pinvalue = StringVar()
        self.statevalue = StringVar()

        pdfselect1 = IntVar()
        pdfselect2 = IntVar()
        pdfselect3 = IntVar()

        nameentry = Entry(self.root, textvariable=self.namevalue)
        emailentry = Entry(self.root, textvariable=self.emailvalue)
        contactentry = Entry(self.root, textvariable=self.contactvalue)
        dobentry = Entry(self.root, textvariable=self.dobvalue)
        residenseentry = Entry(self.root, textvariable=self.residensevalue)
        pinentry = Entry(self.root, textvariable=self.pinvalue)
        stateentry = Entry(self.root, textvariable=self.statevalue)

        pdfselect1 = Checkbutton (self.root, text="Aadhar Card", variable=Checkbutton, onvalue = 1, offvalue = 0, height = 2, width = 10, highlightcolor = "#A8F5EF")
        pdfselect2 = Checkbutton (self.root, text="PAN Card", variable=Checkbutton, onvalue = 1, offvalue = 0, height = 2, width = 10 , highlightcolor = "#A8F5EF")
        pdfselect3 = Checkbutton (self.root, text="Drivers Licsense", variable=Checkbutton, onvalue = 1, offvalue = 0, height = 2, width = 10 , highlightcolor = "#A8F5EF")

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
        self.gendervalue=StringVar()
        self.gendervalue.set(list_gender[0])
        pck=OptionMenu(self.root,self.gendervalue,*list_gender)
        pck.config(width=15,font=("Arial",10))
        pck.grid(row=8, column=3, padx=520)

        Button(text="Register", fg="black", command=self.getval,relief = RIDGE, activebackground="#9FDAF2", activeforeground = "#ffffff", width = 20,height=1).grid(row=15, column=3, pady=55)

    def getval(self):
        genderval = self.gendervalue.get()
        nameval=self.namevalue.get()
        emailval=self.emailvalue.get()
        contactval=self.contactvalue.get()
        dobval=self.dobvalue.get()
        # paymentval=self.paymentvalue.get()
        paymentval='1200'
        pinval=self.pinvalue.get()
        stateval=self.statevalue.get()
        checker=[genderval,nameval,emailval,contactval,dobval,paymentval,pinval,stateval]
        if(self.checkNull(checker)):
            print('We good')
            reg=self.sql.loadDetails(nameval,emailval,contactval,dobval,paymentval,pinval,stateval,genderval)
            print(reg)
            if(reg==True):
                print('True')
                lbl = Label(self.root, text="Submitted!").grid(row=16, column=3, pady=10)
                print('Destroying')
                self.root.destroy()
                print("Submitted")
                Selection1(self.sql,nameval)
            else:
                lbl = Label(self.root, text=reg).grid(row=16, column=3, pady=10)
        else:
            print("Mr. Stark i don't feel so good")
            lbl = Label(self.root, text=f"Field(s) is empty").grid(row=16, column=3, pady=10)
            

    def checkNull(self,checker):
        check=True
        i=0
        for val in checker:
            if(val==""):
                print(i)
                check=False
                break
            else:
                i+=1
                pass
        return check
class documents:
    def __init__(self) -> None:
        pass

if __name__=='__main__':
    screen=DetailsLanding()
    screen.root.mainloop()