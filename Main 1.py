from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

def home_button_press():
    print("hello") 

root = Tk()
root.title("                                                                                                                                                                                                                 KYC Verifier")
root.resizable(0, 0)
root.configure(bg = "#0CA418")

b1 = Button(root,fg="black", text="Get Started!", command=home_button_press,relief = RIDGE, activebackground="#B2EE9A", activeforeground = "#ffffff", width = 20,height=1, font="Gotham 10")
b1.pack(side=BOTTOM, pady=204)

'''img = PhotoImage(file='ass.png') 
root.iconphoto(False, img)'''

canvas_width = 1366
canvas_height = 768

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()
can_widget.configure(bg='#15a13a')

can_widget.create_rectangle(0, 0, 1366, 331, fill="#ffffff")
can_widget.create_text(190,160, text="KYC  ", font="Gotham 100 bold", fill="#0AC83D")
can_widget.create_text(265,280, text="Verifier", font="Gotham 100 bold", fill="#15a13a")
can_widget.create_text(1270,18, text="Vishesh Giyanani C027", font="Gotham 12", fill="#000000")
can_widget.create_text(1270,37, text="   Nilay Gaitonde C023", font="Gotham 12", fill="#000000")
can_widget.create_text(1272,55, text="    Riddhi Dumre C022", font="Gotham 12", fill="#000000")

root.mainloop()