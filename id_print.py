from tkinter import *
from sqlhelp import SQLinitialize
from PIL import Image, ImageTk


def runID(name):
    root = Tk()
    root.title("                                                                                                                                                                                                                 KYC Verifier")
    root.resizable(0, 0)
    canvas_width = 1366
    canvas_height = 768
    root.geometry(f"{canvas_width}x{canvas_height}")
    nameVal=""
    emailVal=""
    number=""

    sql=SQLinitialize()
    result=sql.read(name)
    print(result)
    if(result==False):
        print('Error')
        Label(text='THERE WAS AN ERROR', font= "Gotham 20 bold", bg="#ffffff").place(x=380,y=450)
        return 
    nameVal=result[0]
    emailVal=result[2]
    number=result[3]
    userName=result[9]
    #Image Placement

    #1
    image = Image.open('ID card/one.png') #Opens the Image
    # image = Image.open("D:\\Files\College\\Sem V\\Programming Laboratry - II\\Project\\ID card\\one.png") #Opens the Image
    photo = ImageTk.PhotoImage(image) #Uses the ImagTk function from PIL, keep variable name as arguemnet.
    photo_label = Label(image=photo) #Linking the photo in a Label to display it.
    photo_label.place(x=300,y=77) #Packing the function above.

    #Dirty Photo
    image = Image.open("p0-26.png") #Opens the Image
    photo3 = ImageTk.PhotoImage(image) #Uses the ImagTk function from PIL, keep variable name as arguemnet.
    photo_label3 = Label(image=photo3) #Linking the photo in a Label to display it.
    photo_label3.place(x=410,y=200) #Packing the function above.

    #1 Text

    name = Label(text=nameVal, font= "Gotham 20 bold", bg="#ffffff").place(x=380,y=450)
    user = Label(text=f"{userName}   " + emailVal, font= "Gotham 10", bg="#ffffff").place(x=365,y=500)
    contact = Label(text=f"Conatct Number: {number}",font= "Gotham 10", bg="#ffffff").place(x=380,y=525)

    #2
    image = Image.open("ID card/two.png") #Opens the Image
    photo2 = ImageTk.PhotoImage(image) #Uses the ImagTk function from PIL, keep variable name as arguemnet.
    photo_label2 = Label(image=photo2) #Linking the photo in a Label to display it.
    photo_label2.place(x=800,y=77) #Packing the function above.

    #QRCode
    image = Image.open("p0-15.png") #Opens the Image
    image= image.resize((200,200), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(image) #Uses the ImagTk function from PIL, keep variable name as arguemnet.
    photo_label4 = Label(image=photo4) #Linking the photo in a Label to display it.
    photo_label4.place(x=892,y=262) #Packing the function above.
    root.mainloop()

if __name__=='__main__':
    runID('Nilay Nitish Gaitonde')