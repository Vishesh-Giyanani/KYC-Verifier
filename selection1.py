from os import name, mkdir, path
import main_1
import fitz 
import details_landing 
import qrcode
from tkinter import *
import time
from typing import Sized
from PIL import Image, ImageTk
import cv2
import PyPDF2
from pdf2image import convert_from_path
from tkinter.filedialog import askopenfile

#Test Declarations
name = "Vishesh Bharat Giyanani"
email = "giyananivishesh@gmail.com"
contact = "7045643723"
dob = "2003"
residense = "Mumbai"
pin = "400049"
state = "Maharashtra"
gender = "Male"

val1 = False
val2 = False
val3 = False

def open_file():
    
    global a 
    global b
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Pdf file", "*.pdf")])

    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        a = page.extractText()
        b = read_pdf.documentInfo
        browse_text.set(file)
        time.sleep(1)
        #print(a)
        #print(b)
        a1 = str()
        a1 = a[a.index("future."):]
        #print(a1)
        browse_btn.destroy()
        lbl.destroy()

        def convert():

            '''doc = fitz.open(file)
            zoom = 2 # to increase the resolution
            mat = fitz.Matrix(zoom, zoom)
            noOfPages = doc.pageCount
            image_folder = "D:\\Files\College\\Sem V\\Programming Laboratry - II\\Project\\junk\\"

            for pageNo in range(noOfPages):
                page = doc.loadPage(pageNo) #number of page
                pix = page.getPixmap(matrix = mat)
    
                output = image_folder + str(pageNo) + '.jpg' # you could change image format accordingly
                pix.writePNG(output)'''


            import fitz
            doc = fitz.open(file)
            for i in range(len(doc)):
                for img in doc.getPageImageList(i):
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)
                    if pix.n < 5:       # this is GRAY or RGB
                        pix.writePNG("p%s-%s.png" % (i, xref))
                    else:               # CMYK: convert to RGB first
                        pix1 = fitz.Pixmap(fitz.csRGB, pix)
                        pix1.writePNG("p%s-%s.png" % (i, xref))
                        pix1 = None
                    pix = None

            val1 = True
            
        convert()

        def validate1():

            if (a.find(name) != -1) :
                bolname = True
            else:
                bolname = False

            if (a.find(email) != -1) :
                bolemail = True
            else:
                bolemail = False
            
            if (a.find(dob) != -1) :
                boldob = True
            else:
                boldob = False

            if (a.find(residense) != -1) :
                bolresidense = True
            else:
                bolresidense = False

            if (a.find(pin) != -1) :
                bolpin = True
            else:
                bolpin = False

            if (a.find(state) != -1) :
                bolstate = True
            else:
                bolstate = False

            if (a.find(gender) != -1) :
                bolgender = True
            else:
                bolgender = False
            
            bolarr = [bolname, boldob, bolgender, bolpin, bolstate, bolresidense]
            
            for element in bolarr:
                if element == True :
                    val1 = True

            if (b.values() != -1) :
                val2 = True
            else:
                val2 = False

            '''def covert():
                print("hello")'''

            val1 = True
        
        validate1()

        def validate2():
            '''d = cv2.QRCodeDetector()
            val, points, straight_qrcode = d.detectAndDecode(cv2.imread("D:\\Files\College\\Sem V\\Programming Laboratry - II\\Project\\junk\\1.jpg"))
            print(val)
            print("yes")

            val3 = True'''

        validate2()

        def gif():
            print("hello")
            if val1 == True and val2 == True and val3 == True:
                giffy = Image.open("tick.gif") #Opens the Image
                photo = ImageTk.PhotoImage(giffy) #Uses the ImagTk function from PIL, keep variable name as arguemnet.

                photo_label = Label(image=photo) #Linking the photo in a Label to display it.
                photo_label.pack #Packing the function above.
            else:
                giffy = Image.open("cross.gif") #Opens the Image
                photo = ImageTk.PhotoImage(giffy) #Uses the ImagTk function from PIL, keep variable name as arguemnet.

                photo_label = Label(image=photo) #Linking the photo in a Label to display it.
                photo_label.pack #Packing the function above.


root = Tk()
root.title("                                                                                                                                                                                                                      KYC Verifier")
root.resizable(0,0)

width = 1366    
height = 768
root.geometry(f"{width}x{height}")

#title = Label(root, text="Aadhar Card - 1", font="Raleway 13 bold").grid(row=1, column=10, padx=625, pady=20)

#Enter you Aadhar Card E Letter
lbl = Label(text="Enter you Aadhar Card E Letter", font= "gotham 13 bold")
lbl.grid(column=5, row=3)

#Button 1
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=28)
browse_text.set("Chose file")
browse_btn.grid(column=5, row=2, padx=617, pady=320)


root.mainloop()