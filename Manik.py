from tkinter import *
from PIL import Image, ImageTk, ImageFont

from imgDef import *
from koduakenDef import *
from minuinfoDef import *
from portfoolioDef import *

koduaken=Tk()
koduaken.geometry("700x850")
koduaken.title("ArtNailsPro")
koduaken.resizable(width=False, height=False)

bg=pilt("img/fon/fon21.jpg", (700,850))
koduakenbg=Label(koduaken, image=bg)
koduakenbg.place(x=0, y=0, relwidth=1, relheight=1)

border=Frame(koduaken, relief="solid", borderwidth=5, width=555, height=705, bg="black")
border.place(x=70, y=70)

frame=Frame(koduaken, width=550, height=700, bg="white")
frame.place(x=72, y=72)

kodu(frame)

koduaken.mainloop()


