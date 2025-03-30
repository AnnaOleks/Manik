from tkinter import *
from PIL import Image, ImageTk, ImageFont

from imgDef import *
from minuinfoDef import *
from koduakenDef import *

def portfolio(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    logo=Label(frame, text="ArtNailsPro", font="Dillnation 40", fg="black", bg="white")
    logo.place(x=10, y=10)

    nails1img=pilt("img/nails/nails1.png", (200, 200))
    nails1 = Label(frame, image=nails1img, bg="black")
    nails1.image = nails1img
    nails1.place(x=270, y=30)

    pedi1img=pilt("img/nails/pedi1.png", (200, 200))
    pedi1 = Label(frame, image=pedi1img, bg="black")
    pedi1.image = pedi1img
    pedi1.place(x=80, y=130)

    nails2img=pilt("img/nails/nails2.png", (200, 200))
    nails2 = Label(frame, image=nails2img, bg="black")
    nails2.image = nails2img
    nails2.place(x=270, y=250)

    pedi3img=pilt("img/nails/pedi3.png", (200, 200))
    pedi3 = Label(frame, image=pedi3img, bg="black")
    pedi3.image = pedi3img
    pedi3.place(x=80, y=350)

    nails3img=pilt("img/nails/nails3.png", (200, 200))
    nails3 = Label(frame, image=nails3img, bg="black")
    nails3.image = nails3img
    nails3.place(x=270, y=470)

    tagasiportfolio=Button(frame, text="TAGASI", font="Lora 10", bg="white", width=55, height=1, command=lambda: kodu(frame))
    tagasiportfolio.place(relx=0.5, y=590, anchor="center")