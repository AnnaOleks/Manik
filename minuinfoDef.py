from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFont
from tkinter import font

from portfoolioDef import *
from koduakenDef import *

def minuinfo(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
    logo=Label(frame, text="ArtNailsPro", font="Dillnation 40", fg="black", bg="white")
    logo.place(x=10, y=10)
    
    tervitusminust=Label(frame, text="Tervist!", font="Lora 18 bold", bg="white")
    tervitusminust.place(y=140, relx=0.5, anchor="center")

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
    tekst.place(x=25, y=170, anchor=NW)

    portfooliominust=Button(frame, text="PORTFOOLIO", font="Lora 10", bg="white", width=55, height=1, command=lambda: portfolio(frame))
    portfooliominust.place(relx=0.5, y=550, anchor="center")
    
    tagasiminust=Button(frame, text="TAGASI", font="Lora 10", bg="white", width=55, height=1, command=lambda: kodu(frame))
    tagasiminust.place(relx=0.5, y=590, anchor="center")
    

