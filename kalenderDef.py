from tkinter import *
import calendar
from datetime import datetime
from tkinter import ttk
from turtle import bgcolor

from andmebaasDef import kuvavabadajad

toohoive = {paev: 0 for paev in range(1, 32)}  # по умолчанию все дни свободны

def toohiveuuendus(paev, status):
    toohoive[paev]=status

def paevaarv(status):
    if status==2:
        return "#fce6ea"
    elif status==1:
        return "#e1fbf3"
   
def uuskuu(kuu):
    global algkuu  # Используем глобальную переменную month
    algkuu = list(calendar.month_name).index(kuu)  # Находим индекс месяца по его имени
    kalendriavamine()

def uusaasta(aasta):
    global algaasta  # Используем глобальную переменную year_selected
    algaasta = int(aasta)  # Преобразуем выбранный год в целое число
    kalendriavamine()  # Перерисовываем календарь с новым годом

def kalendriavamine():
    from andmebaasDef import kuvavabadajad

    global kuuframe, algkuu, algaasta, vabadajadlistbox

    for widget in kuuframe.winfo_children():
        widget.destroy()

    kalendripealkiri = Label(kuuframe, text=f"{calendar.month_name[algkuu]} {algaasta}", font="Lora 14", bg="white")
    kalendripealkiri.grid(row=0, column=0, columnspan=7)  # Размещаем на первой строке, в 7 столбцах

    nadalapaevad = ["E", "T", "K", "N", "R", "L", "P"]  # Список дней недели
    for i, nadalapaev in enumerate(nadalapaevad):  # Перебираем список дней недели
        nadalapaev = Label(kuuframe, text=f"\n{nadalapaev}", font="Lora 12", width=3, bg="white")  # Создаём метку для дня недели
        nadalapaev.grid(row=1, column=i)  # Размещаем на второй строке, по столбцам

    paevad = calendar.monthcalendar(algaasta, algkuu)

    row = 2  # Начинаем с третьей строки для отображения дней
    for nadal in paevad:  # Перебираем каждую неделю в календаре
        for col, paev in enumerate(nadal):  # Перебираем каждый день в неделе
            if paev != 0:  # Если день не равен 0 (что означает отсутствие дня в этом месте недели)
                # Создаём кнопку для дня месяца
                paevtekst = f"{algaasta}-{str(algkuu).zfill(2)}-{str(paev).zfill(2)}"
                status=paevaarv(paevtekst)
                color=staatusnum(status)
                paevnupp = Button(kuuframe, text=str(paev), width=3, height=1, font=("Lora", 10), command=lambda paev=paev: kuvavabadajad(paev, vabadajadlistbox, algaasta, algkuu))
                paevnupp.grid(row=row, column=col, padx=3, pady=3)  # Размещаем кнопку в соответствующей строке и столбце
        row += 1  # Переходим к следующей строке

def staatusnum(paev):
    from registrDef import registrkogus

    count=registrkogus(paev)
    maxklientpaev=6

    if count==0:
        return 0
    elif count > 0 and count < maxklientpaev:
        return 1
    elif count == maxklientpaev:
        return 2
    
def kalenderaken(frame):
    global algkuu, algaasta, kuuframe, kalenderframe, vabadajadlistbox

    for widget in frame.winfo_children():
        widget.destroy()

    logo=Label(frame, text="ArtNailsPro", font="Dillnation 40", fg="black", bg="white")
    logo.place(x=10, y=10)

    pealkiri=Label(frame, text="Vali soovitud kuupäev", font="Lora 18 bold", fg="black", bg="white")
    pealkiri.place(y=140, relx=0.5, anchor="center")

    margid=Frame(frame, bg="white")
    margid.place(y=180, x=50)

    otsas=Label(margid, bg="#fce6ea", width=5, height=1, border=1, relief="solid")
    otsas.grid(row=0, column=1)

    otsastekst=Label(margid, text=" Vabu kohti ei ole!   ", font="Lora 12", fg="black", bg="white")
    otsastekst.grid(row=0, column=2, sticky=W)

    monedajad=Label(margid, bg="#e1fbf3", width=5, height=1, border=1, relief="solid")
    monedajad.grid(row=0, column=3)

    monedajadtekst=Label(margid, text=" On jäänud mõned ajad!", font="Lora 12", fg="black", bg="white")
    monedajadtekst.grid(row=0, column=4, sticky=W)

    kalenderframe=Frame(frame, width=350, bg="white")
    kalenderframe.place(x=50, y=230)

    algaasta=datetime.now().year
    algkuu=datetime.now().month

    control_frame = Frame(kalenderframe, bg="white")
    control_frame.pack(pady=10)

    # Выпадающий список для выбора месяца
    kuuvalik = StringVar()
    kuuvalik.set(calendar.month_name[algkuu])
    kuumenyy = ttk.Combobox(control_frame, textvariable=kuuvalik, values=list(calendar.month_name[1:]), state="readonly", font=("Lora", 12), width=13, background="white", justify=LEFT)
    kuumenyy.grid(row=0, column=0, padx=6, sticky=W)
    kuumenyy.bind("<<ComboboxSelected>>", lambda event: uuskuu(kuuvalik.get()))

    # Выпадающий список для выбора года
    aastavalik = StringVar()
    aastavalik.set(str(algaasta))
    aastamenyy = ttk.Combobox(control_frame, textvariable=aastavalik, values=[str(year) for year in range(2020, 2031)], state="readonly", font=("Lora", 12), width=13, background="white")
    aastamenyy.grid(row=0, column=1, padx=9, sticky=E)
    aastamenyy.bind("<<ComboboxSelected>>", lambda event: uusaasta(aastavalik.get()))

    # Календарный фрейм
    kuuframe = Frame(kalenderframe, bd=2, relief="solid", bg="white", pady=5, padx=5)
    kuuframe.pack()

    kalendriavamine()

    vabadajad=Label(frame, text="Vabad ajad:", font="Lora 12 bold", fg="black", bg="white")
    vabadajad.place(x=370, y=270)

    vabadajadlistbox = Listbox(frame, font="Lora 12", height=10, width=14, selectbackground="#e1fbf3", selectforeground="black")
    vabadajadlistbox.place(x=370, y=300)

    edasi=Button(frame, text="EDASI", font="Lora 10", bg="white", activebackground="#fce6ea", width=55, height=1)
    edasi.place(relx=0.5, y=600, anchor="center")

    tagasikalender=Button(frame, text="KODULEHELE", font="Lora 10", bg="white", activebackground="#e1fbf3", width=55, height=1, command=lambda: kodu(frame))
    tagasikalender.place(relx=0.5, y=640, anchor="center")