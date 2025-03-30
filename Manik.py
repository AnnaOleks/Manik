from textwrap import wrap
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFont
from tkinter import font

from minuinfoDef import *
from portfolioDef import *

koduaken=Tk()
koduaken.geometry("700x850")
koduaken.title("ArtNailsPro")
koduaken.resizable(width=False, height=False)

orig_bg=Image.open(r"img/fon/fon30.jpg")
resize_bg=orig_bg.resize((700,850))
bg=ImageTk.PhotoImage(resize_bg)
koduakenbg=Label(koduaken, image=bg)
koduakenbg.place(x=0, y=0, relwidth=1, relheight=1)

border=Frame(koduaken, relief="solid", borderwidth=5, width=555, height=705, bg="black")
border.place(x=70, y=70)

frame=Frame(koduaken, width=550, height=700, bg="white")
frame.place(x=72, y=72)

logo=Label(frame, text="ArtNailsPro", font="Dillnation 40", fg="black", bg="white")
logo.place(x=10, y=10)

manpedimg=Image.open(r"img/pic/manped.png")
resize_manpedimg=manpedimg.resize((320,200))
manped_image = ImageTk.PhotoImage(resize_manpedimg)
manped = Label(frame, image=manped_image, bg="white")
manped.image = manped_image
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

koduakenbg.mainloop()