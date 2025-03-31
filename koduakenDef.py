from tkinter import *
from PIL import Image, ImageTk, ImageFont


def kodu(frame):
    from imgDef import pilt
    from minuinfoDef import minuinfo
    from portfoolioDef import portfolio
    from kalenderDef import kalenderaken

    for widget in frame.winfo_children():
        widget.destroy()
    
    logo=Label(frame, text="ArtNailsPro", font="Dillnation 40", fg="black", bg="white")
    logo.place(x=10, y=10)

    manpedimg=pilt("img/pic/french.png", (250,191))
    manped = Label(frame, image=manpedimg, bg="white")
    manped.image = manpedimg
    manped.place(x=300, y=520)

    tervitus=Label(frame, text="Tere tulemast!", font="Lora 18 bold", bg="white")
    tervitus.place(y=180, relx=0.5, anchor="center")

    tekst=Label(frame, text="Broneeri maniküürile või pediküürile aeg paari klikiga - \nkiiresti, mugavalt ja ilma asjatute telefonikõnedeta. \nVali teenus ja aeg ning naudi veatut tulemust!", font="Lora 12", bg="white", wraplength=500)
    tekst.place(y=280, relx=0.5, anchor="center")

    minust=Button(frame, text="MINUST", font="Lora 10", bg="white", width=55, height=1, activebackground="#fce6ea", activeforeground="black", command=lambda:minuinfo(frame))
    minust.place(relx=0.5, y=390, anchor="center")

    portfoolio=Button(frame, text="PORTFOOLIO", font="Lora 10", bg="white", activebackground="#e1fbf3", activeforeground="black", width=55, height=1, command=lambda:portfolio(frame))
    portfoolio.place(relx=0.5, y=430, anchor="center")

    kirjapanek=Button(frame, text="PANEN ENNAST KIRJA", font="Lora 10", bg="white", width=55, height=1, activebackground="#fce6ea", activeforeground="black", command=lambda:kalenderaken(frame))
    kirjapanek.place(relx=0.5, y=470, anchor="center")
