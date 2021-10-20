from tkinter import *
import re

from account import CreateAccount 


class BankDetails:
    def __init__(self,name):
        self.nameSql=name
        self.ifscvaluebool=False
        self.acc_numvaluebool=False
        self.root = Tk()

        self.root.title("                                                                                                                                                                                                                 KYC Verifier")
        # self.root.resizable(0, 0)

        canvas_width = 1366
        canvas_height = 768
        self.root.geometry(f"{canvas_width}x{canvas_height}")

        Label(self.root, text="Bank Account Details", font="Raleway 13 bold", pady=30,padx = 100).grid(row=0, column=3,)

        name = Label(self.root, text="   Enter Account Holder Name:")
        acc_num = Label(self.root, text="   Enter Account Number:")
        ifsc = Label(self.root, text="   Enter IFSC Code:")
 

        name.grid(row=1, column=2,  sticky=W)
        acc_num.grid(row=2, column=2,  sticky=W)
        ifsc.grid(row=3, column=2,  sticky=W)


        self.namevalue = StringVar()
        self.acc_numvalue  = StringVar()
        self.ifscvalue = StringVar()


        nameentry = Entry(self.root, textvariable=self.namevalue)
        acc_numentry = Entry(self.root, textvariable=self.acc_numvalue)
        ifscentry = Entry(self.root, textvariable=self.ifscvalue)


        nameentry.grid(row=1, column=3, padx=520)
        acc_numentry.grid(row=2, column=3, padx=520)
        ifscentry.grid(row=3, column=3, padx=520)

        # Checkbutton
        pancheck = Checkbutton (self.root, text="Do you own a Pan Card", variable=Checkbutton,command=self.panism, onvalue = 1, offvalue = 0, height = 4, width = 100, highlightcolor = "#A8F5EF")
        pancheck.grid(row = 8, column=3, pady=100)

        submit= Button(self.root,text="Submit",command=self.validate, highlightcolor = "#A8F5EF").grid(row=9,column=3,padx=520)
        self.lbl = Label(self.root, text="").grid(row=10, column=3, pady=10)
        

    def panism(self):
        pan = Label(self.root, text="   Enter PAN Card Number")
        pan.grid(row=4, column=2, sticky=W)
        panvalue = StringVar()
        panentry = Entry(self.root, textvariable=panvalue)
        panentry.grid(row=4, column=3, padx=50)
    
    def validate(self):
        name=self.namevalue.get()
        ifsc=self.ifscvalue.get()
        accNum=self.acc_numvalue.get()
        if name!='':
            if(name!=self.nameSql):
                print(f'{self.nameSql}\n{name}')
                print('Wrong')
                self.lbl = Label(self.root, text="Your account name doens't match the original name").grid(row=1, column=4, pady=10)
        else:
            self.lbl = Label(self.root, text="Name field empty").grid(row=10, column=3, pady=10)
            print("nayo")


        if ifsc!='':
            Result=re.compile("^[A-Z]{4}0[A-Z0-9]{6}$") 
            self.ifscvaluebool = bool(re.match(Result,ifsc))
            print(self.ifscvaluebool)
            if(self.ifscvaluebool):
                print('IFSC We good')
            else:
                self.lbl = Label(self.root, text="Something is wrong here").grid(row=2, column=4, pady=10)
                print('But tony the ifsc field has an error')

        else:
            self.lbl = Label(self.root, text="IFSC Code field empty").grid(row=10, column=3, pady=10)
            print("nayo")

        if accNum!='':
            self.lbl = Label(self.root, text="Account number field empty").grid(row=3, column=4, pady=10)
            Result=re.compile("[0-9]{9,18}") 
            self.acc_numvaluebool = bool(re.match(Result,accNum))
            if(self.acc_numvaluebool):
                print('Accno We good')
            else:
                self.lbl = Label(self.root, text="Something is wrong here").grid(row=10, column=3, pady=10)
                print('But tony the account number field has an error')

        else:
            print("nayo")
        
        print(f'{self.ifscvaluebool}\n{self.acc_numvaluebool}')
        if( self.ifscvaluebool== True and self.acc_numvaluebool== True):
            print('WE ARE GOOD LOVES')
            self.root.destroy()
            CreateAccount(name)
        else:
            print('Somethings wrong')

# username password go to 
if __name__=='__main__':
    bd=BankDetails('Vishesh Bharat Giyanani')
    bd.root.mainloop()