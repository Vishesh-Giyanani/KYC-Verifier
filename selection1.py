from tkinter import *
from typing import Sized
from PIL import Image, ImageTk
import PyPDF2
from tkinter.filedialog import askopenfile

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        print(read_pdf.documentInfo)       

root = Tk()
root.title("                                                                                                                                                                                                                 KYC Verifier")
root.resizable(0,0)

width = 1366    
height = 768
root.geometry(f"{width}x{height}")

#title = Label(root, text="Aadhar Card - 1", font="Raleway 13 bold").grid(row=1, column=10, padx=625, pady=20)

browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Chose file")
browse_btn.grid(column=15, row=2, padx=600, pady=300)


root.mainloop()