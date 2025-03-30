from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFont
from tkinter import font

def minuinfo(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
    logo=Label(frame, text="ArtNailsPro", font="Dillnation 40", fg="black", bg="white")
    logo.place(x=10, y=10)
    
    tervitusminust=Label(frame, text="Tervist!", font="Lora 18 bold", bg="white")
    tervitusminust.place(y=130, relx=0.5, anchor="center")

    tekst=Label(frame, text="""
    Ma olen Nastya, maniküüri ja pediküüri meister.
    Armastan vabaõhuüritusi, mootorrattasõitu ja 
    trummimängu. Maniküür on minu kirg, olen läbinud 
    kursusi Eesti parimatelt meistritelt ja 
    püüan alati täiuslikkuse poole.
    
    Tööl:
    ● Instrumentide steriliseerimine.
    ● Ainult ühekordsed ja sertifitseeritud materjalid.
    ● Hubane kabinet ja kaasaegne tehnika.
    
    
    Hindan teie valikut! Kui teil on küsimusi - kirjutage!
    """, font="Lora 14", bg="white", wraplength=500, anchor=NW, justify=LEFT)
    tekst.place(x=25, y=150, anchor=NW)

    portfooliominust=Button(frame, text="PORTFOOLIO", font="Lora 10", bg="white", width=55, height=1)
    portfooliominust.place(relx=0.5, y=450, anchor="center")
    
    tagasiminust=Button(frame, text="TAGASI", font="Lora 10", bg="white", width=55, height=1, command=lambda:tagasi(frame))
    tagasiminust.place(relx=0.5, y=490, anchor="center")
    
    lakkimg=Image.open(r"img/pic/lakk.png")
    resize_manpedimg=manpedimg.resize((320,200))
    manped_image = ImageTk.PhotoImage(resize_manpedimg)
    manped = Label(frame, image=manped_image, bg="white")
    manped.image = manped_image
    manped.place(x=230, y=520)

def tagasi(frame):
    for widget in frame.winfo_children():
        widget.destroy()
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

    portfoolio=Button(frame, text="PORTFOOLIO", font="Lora 10", bg="white", width=55, height=1)
    portfoolio.place(relx=0.5, y=430, anchor="center")

    kirjapanek=Button(frame, text="PANEN ENNAST KIRJA", font="Lora 10", bg="white", width=55, height=1)
    kirjapanek.place(relx=0.5, y=470, anchor="center")