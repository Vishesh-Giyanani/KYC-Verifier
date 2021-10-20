import tkinter as tk
from cv2 import recoverPose
import mysql.connector

from sqlhelp import SQLinitialize

class CreateAccount:
    def __init__(self,name):
        self.sql=SQLinitialize()
        self.name=name
        self.root=tk.Tk()
        self.root.title("                                                                                                                                                                                                                 KYC Verifier")
        
        canvas_width = 1366
        canvas_height = 768
        self.root.geometry(f"{canvas_width}x{canvas_height}")

        tk.Label(self.root, text="Your account", font="Raleway 13 bold", pady=30,padx = 100).grid(row=0, column=3,)
        
        self.userNameLabel=tk.Label(self.root,text="Enter username:")
        self.passwordLabel=tk.Label(self.root,text="Enter password:")

        self.userNameLabel.grid(row=1,column=2)
        self.passwordLabel.grid(row=2,column=2)

        self.userNameEntry=tk.Entry(self.root)
        self.passwordEntry=tk.Entry(self.root)

        self.userNameEntry.grid(row=1,column=3,padx=520)
        self.passwordEntry.grid(row=2,column=3,padx=520)

        submit=tk.Button(self.root,text="Submit",command=self.validate, highlightcolor = "#A8F5EF").grid(row=4,column=3,padx=520)
        self.lbl = tk.Label(self.root, text="").grid(row=10, column=3, pady=10)

    def validate(self):
        up=self.sql.update(self.name,self.passwordEntry.get())
        if(up==True):
            print('We good')
        else:
            print('Look how they massacred my boy')
            print(up)

if __name__=='__main__':
    acc=CreateAccount('Nilay Gaitonde')
    acc.root.mainloop()