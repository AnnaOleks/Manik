from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFont
from tkinter import font

def portfolio(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    logo=Label(frame, text="ArtNailsPro", font="Dillnation 40", fg="black", bg="white")
    logo.place(x=10, y=10)

    nails1img=Image.open(r"img/pic/nails1.png")
    resize_nails1img=nails1img.resize((200,200))
    nails1_image = ImageTk.PhotoImage(resize_nails1img)
    nails1 = Label(frame, image=nails1_image, bg="white")
    nails1.image = nails1_image
    nails1.place(x=3400, y=20)