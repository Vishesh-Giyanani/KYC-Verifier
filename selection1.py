from os import times
import time
import tkinter as tk
import sys
sys.path.insert(0,'Face-Recognition/face_rec.py')
# import face_rec
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

import PyPDF2
import fitz

class Selection1:
    def __init__(self,sql,name):
        self.val1=False
        self.val2=False
        self.val3=False
        self.root = tk.Tk()
        self.root.title("                                                                                                                                                                                                                      KYC Verifier")
        self.root.resizable(0,0)

        width = 1366    
        height = 768
        self.root.geometry(f"{width}x{height}")
        self.lbl = tk.Label(text="Enter you Aadhar Card E Letter", font= "gotham 13 bold")
        self.lbl.grid(column=5, row=3)

        #Button 1
        self.browse_text = tk.StringVar()
        self.browse_btn = tk.Button(self.root, textvariable=self.browse_text, command=lambda:self.open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=28)
        self.browse_text.set("Chose file")
        self.browse_btn.grid(column=5, row=2, padx=617, pady=320)

        result=sql.read(name)
        self.name=result[0]
        self.email=result[1]
        self.number=result[2]
        self.dob=result[3]
        self.pin=result[4]
        self.state=result[5]
        self.gender=result[6]
    
    def open_file(self):
        self.browse_text.set("loading...")
        self.file = askopenfile(parent=self.root, mode='rb', title="Choose a file", filetypes=[('PDF Files','*.pdf')])
        if self.file:
            read_pdf = PyPDF2.PdfFileReader(self.file)
            page = read_pdf.getPage(0)
            self.a = page.extractText()
            self.b = read_pdf.documentInfo
            self.browse_text.set(self.file)
            times.sleep(1)
            self.a1 = str()
            self.a1 = self.a[self.a.index("future."):]
            #print(a1)
            self.browse_btn.destroy()
            self.lbl.destroy()
            self.convert()
            self.validate1()

    def convert(self):

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


            doc = fitz.open(self.file)
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

            self.val1 = True
    def validate1(self):

            if (self.a.find(self.name) != -1) :
                bolname = True
            else:
                bolname = False

            if (self.a.find(self.email) != -1) :
                bolemail = True
            else:
                bolemail = False
            
            if (self.a.find(self.dob) != -1) :
                boldob = True
            else:
                boldob = False

            if (self.a.find(self.residense) != -1) :
                bolresidense = True
            else:
                bolresidense = False

            if (self.a.find(self.pin) != -1) :
                bolpin = True
            else:
                bolpin = False

            if (self.a.find(self.state) != -1) :
                bolstate = True
            else:
                bolstate = False

            if (self.a.find(self.gender) != -1) :
                bolgender = True
            else:
                bolgender = False
            
            bolarr = [bolname, bolemail, boldob, bolgender, bolpin, bolstate, bolresidense]
            
            for element in bolarr:
                if element == True :
                    self.val1 = True

            if (self.b.values() != -1) :
                self.val2 = True
            else:
                self.val2 = False
            self.val1 = True
            
    def validate2(self):
        '''d = cv2.QRCodeDetector()
        val, points, straight_qrcode = d.detectAndDecode(cv2.imread("D:\\Files\College\\Sem V\\Programming Laboratry - II\\Project\\junk\\1.jpg"))
        print(val)
        print("yes")

        val3 = True'''

    def gif(self):
        print("hello")
        if self.val1 == True and self.val2 == True and self.val3 == True:
            
            giffy = Image.open("tick.gif") #Opens the Image
            photo = ImageTk.PhotoImage(giffy) #Uses the ImagTk function from PIL, keep variable name as arguemnet.

            photo_label = tk.Label(image=photo) #Linking the photo in a Label to display it.
            photo_label.pack #Packing the function above.
            time.sleep(10)
            # face_rec.faceRecog(self.name)
        else:
            giffy = Image.open("cross.gif") #Opens the Image
            photo = ImageTk.PhotoImage(giffy) #Uses the ImagTk function from PIL, keep variable name as arguemnet.

            photo_label = tk.Label(image=photo) #Linking the photo in a Label to display it.
            photo_label.pack #Packing the function above.
