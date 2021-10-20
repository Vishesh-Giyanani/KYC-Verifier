from tkinter import *
from sqlhelp import SQLinitialize
from selection1 import Selection1
from PIL import Image, ImageTk

root = Tk()

root.title("                                                                                                                                                                                                                 KYC Verifier")
root.resizable(0, 0)
canvas_width = 1366
canvas_height = 768
root.geometry(f"{canvas_width}x{canvas_height}")

#Image Placement

#1
image = Image.open("D:\\Files\College\\Sem V\\Programming Laboratry - II\\Project\\ID card\\one.png") #Opens the Image
photo = ImageTk.PhotoImage(image) #Uses the ImagTk function from PIL, keep variable name as arguemnet.
photo_label = Label(image=photo) #Linking the photo in a Label to display it.
photo_label.place(x=300,y=77) #Packing the function above.

#Dirty Photo
image = Image.open("D:\\Files\College\\Sem V\\Programming Laboratry - II\\Project\\p0-26.png") #Opens the Image
photo3 = ImageTk.PhotoImage(image) #Uses the ImagTk function from PIL, keep variable name as arguemnet.
photo_label3 = Label(image=photo3) #Linking the photo in a Label to display it.
photo_label3.place(x=410,y=200) #Packing the function above.

#1 Text
email = "giyananivishesh@gmail.com"
name = Label(text="Vishesh Giyanani", font= "Gotham 20 bold", bg="#ffffff").place(x=380,y=450)
user = Label(text="VisheshG   " + email, font= "Gotham 10", bg="#ffffff").place(x=365,y=500)
contact = Label(text="Conatct Number: 7045643723",font= "Gotham 10", bg="#ffffff").place(x=380,y=525)

#2
image = Image.open("D:\\Files\College\\Sem V\\Programming Laboratry - II\\Project\\ID card\\two.png") #Opens the Image
photo2 = ImageTk.PhotoImage(image) #Uses the ImagTk function from PIL, keep variable name as arguemnet.
photo_label2 = Label(image=photo2) #Linking the photo in a Label to display it.
photo_label2.place(x=800,y=77) #Packing the function above.

#QRCode
image = Image.open("D:\\Files\College\\Sem V\\Programming Laboratry - II\\Project\\p0-15.png") #Opens the Image
image= image.resize((200,200), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(image) #Uses the ImagTk function from PIL, keep variable name as arguemnet.
photo_label4 = Label(image=photo4) #Linking the photo in a Label to display it.
photo_label4.place(x=892,y=262) #Packing the function above.

root.mainloop()