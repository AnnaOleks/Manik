from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import calendar
from datetime import datetime

from andmebaasDef import kuvavabadajad

def uuendavorm():
    """Обновляет поля формы выбранными значениями"""
    valitud_kuupaev = cal.get_date()
    valitud_aeg = time_combobox.get()

    if valitud_kuupaev and valitud_aeg:
        kuupaeventry.delete(0, END)
        kuupaeventry.insert(0, valitud_kuupaev)
        
        aegentry.delete(0, END)
        aegentry.insert(0, valitud_aeg)

def regklient():
    from andmebaasDef import baasuhendus

    nimi = nimientry.get()
    email = emailentry.get()
    tel = telentry.get()
    teenus = teenusenimi.get().split(" - ")[0]  # Получаем ID услуги
    kuupaev = kuupaeventry.get()
    aeg = aegentry.get()

    if not (nimi and tel and teenus and kuupaev and aeg):
        messagebox.showerror("Viga", "Täida kõik väljad!")
        return

    with baasuhendus() as conn:
        cursor = conn.cursor()
        
        # Проверяем, существует ли клиент
        cursor.execute('SELECT id FROM kliendid WHERE nimi = ?', (nimi,))
        klient = cursor.fetchone()
        if klient:
            klient_id = klient[0]
        else:
            cursor.execute('INSERT INTO kliendid (nimi,email, tel) VALUES (?, ?, ?);' , (nimi, email, tel))
            conn.commit()
            klient_id = cursor.lastrowid 
        
        # Проверяем, доступно ли время
        cursor.execute('SELECT 1 FROM registr WHERE kuupaev = ? AND aeg = ?', (kuupaev, aeg))
        if cursor.fetchone():
            messagebox.showerror("Viga", "See aeg on juba broneeritud!")
            return
        
        # Добавляем бронирование
        cursor.execute('INSERT INTO registr (klient_id, teenus_id, kuupaev, aeg) VALUES (?, ?, ?, ?)',
                       (klient_id, teenus_id, kuupaev, aeg))
        conn.commit()
        
        messagebox.showinfo("Õnnestus", "Broneering edukalt tehtud!")

    

def registraken(frame,):
    from andmebaasDef import baasuhendus

    global nimientry, emailentry, telentry, teenusenimi, kuupaeventry, aegentry

    for widget in frame.winfo_children():
        widget.destroy()

    logo=Label(frame, text="ArtNailsPro", font="Dillnation 40", fg="black", bg="white")
    logo.place(x=10, y=10)

    nimi=Label(frame, text="Nimi:", font="Lora 12 bold", bg="white", width=15, justify=LEFT, anchor=NW)
    nimi.place(x=50, y=180)
    nimientry=Entry(frame, font="Lora 12", bg="white", width=39)
    nimientry.place(x=140, y=180)

    email=Label(frame,text="Email:", font="Lora 12 bold", bg="white", width=15, justify=LEFT, anchor=NW)
    email.place(x=50, y=220)
    emailentry=Entry(frame, font="Lora 12", bg="white", width=39)
    emailentry.place(x=140, y=220)

    tel=Label(frame,text="Telefon:", font="Lora 12 bold", bg="white", width=15, justify=LEFT, anchor=NW)
    tel.place(x=50, y=260)
    telentry=Entry(frame, font="Lora 12", bg="white", width=39)
    telentry.place(x=140, y=260)

    teenus=Label(frame,text="Teenus:", font="Lora 12 bold", bg="white", width=15, justify=LEFT, anchor=NW)
    teenus.place(x=50, y=300)
    teenusenimi=StringVar()
    teenusvar=Combobox(frame, textvariable=teenusenimi, font="Lora 12", width=37)
    teenusvar.place(x=140, y=300)

    with baasuhendus() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, teenus FROM teenused')
        teenused = cursor.fetchall()
        teenusvar['values'] = [f"{s[0]} - {s[1]}" for s in teenused]

    kuupaev_label=Label(frame, text="Kuupäev:", font="Lora 12 bold", bg="white", width=15, justify=LEFT, anchor=NW)
    kuupaev_label.place(x=50, y=340)
    kuupaeventry = Entry(frame, textvariable=valitud_kuupaev, font="Lora 12", bg="white", width=39)
    kuupaeventry.place(x=140, y=340)

    aeg_label=Label(frame, text="Kellaaeg:", font="Lora 12 bold", bg="white", width=15, justify=LEFT, anchor=NW)
    aeg_label.place(x=50, y=380)
    aegentry = Entry(frame, font="Lora 12", bg="white", width=39, textvariable=valitud_aeg) 
    aegentry.place(x=140, y=380)

    submit_button = Button(frame, text="Broneeri", font="Lora 10", bg="white", width=55, height=1, activebackground="#fce6ea", activeforeground="black", command=lambda: regklient())  # Call regklient
    submit_button.place(relx=0.5, y=470, anchor="center")