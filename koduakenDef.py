from tkinter import *
from PIL import Image, ImageTk, ImageFont

from imgDef import *
from minuinfoDef import *
from portfoolioDef import *

def kodu(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
    logo=Label(frame, text="ArtNailsPro", font="Dillnation 40", fg="black", bg="white")
    logo.place(x=10, y=10)

    manpedimg=pilt("img/pic/manped.png", (320,200))
    manped = Label(frame, image=manpedimg, bg="white")
    manped.image = manpedimg
    manped.place(x=230, y=520)

    tervitus=Label(frame, text="Tere tulemast", font="Lora 18 bold", bg="white")
    tervitus.place(y=180, relx=0.5, anchor="center")

    tekst=Label(frame, text="Broneeri maniküürile või pediküürile aeg paari klikiga - \nkiiresti, mugavalt ja ilma asjatute telefonikõnedeta. \nVali teenus ja aeg ning naudi veatut tulemust!", font="Lora 14", bg="white", wraplength=500)
    tekst.place(y=260, relx=0.5, anchor="center")

    minust=Button(frame, text="MINUST", font="Lora 10", bg="white", width=55, height=1, command=lambda:minuinfo(frame))
    minust.place(relx=0.5, y=390, anchor="center")

    portfoolio=Button(frame, text="PORTFOOLIO", font="Lora 10", bg="white", width=55, height=1, command=lambda:portfolio(frame))
    portfoolio.place(relx=0.5, y=430, anchor="center")

    kirjapanek=Button(frame, text="PANEN ENNAST KIRJA", font="Lora 10", bg="white", width=55, height=1)
    kirjapanek.place(relx=0.5, y=470, anchor="center")
