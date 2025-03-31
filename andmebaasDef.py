from tkinter import *
import pyodbc
from datetime import datetime, timedelta

valitud_aeg = StringVar()

def baasuhendus():
    conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                                "SERVER=(localdb)\MSSQLLocalDB;"
                                "DATABASE=manik;"
                                "Trusted_Connection=yes;")
    return conn

def registrkogus(paev):
    conn=baasuhendus()
    cursor = conn.cursor()

    query = """
        SELECT COUNT(*) 
        FROM registr 
        WHERE kuupaev = ?
    """
    cursor.execute(query, (paev,))
    count = cursor.fetchone()[0]
    
    conn.close()
    return count

def lisaklient(klient_id, teenus_id, kuupaev, aeg):
    conn=baasuhendus()
    cursor = conn.cursor()

    # SQL-запрос для добавления бронирования
    query = '''
    INSERT INTO registr (klient_id, teenus_id, kuupaev, aeg)
    VALUES (?, ?, ?, ?)
    '''
    cursor.execute(query, (klient_id, teenus_id, kuupaev, aeg))
    conn.commit()
    conn.close()

def regajadelist(kuupaev):
    conn=baasuhendus()
    cursor = conn.cursor()

    # SQL-запрос для получения всех забронированных интервалов для определенного дня
    query = '''
    SELECT aeg, kestvus 
    FROM registr
    JOIN teenused ON registr.teenus_id = teenused.id
    WHERE kuupaev = ?
    '''
    cursor.execute(query, (kuupaev,))
    result = cursor.fetchall()

    conn.close()  
    return result

def vabadajad(kuupaev):
    conn=baasuhendus()
    cursor = conn.cursor()

    tooalgus = datetime.strptime("09:00", "%H:%M")
    toolopp = datetime.strptime("18:00", "%H:%M")

    # Все возможные временные интервалы для рабочего дня (каждые 30 минут)
    koikajad = []
    algus = tooalgus
    while algus < toolopp:
        jargaeg = algus + timedelta(minutes=90)
        koikajad.append((algus.strftime("%H:%M"), jargaeg.strftime("%H:%M")))
        algus = jargaeg

    # Получаем все забронированные интервалы для выбранного дня
    regajad = regajadelist(kuupaev)

     # Свободные интервалы
    vabadajad = []
    for interval in koikajad:
        kinni = False
        algaeg = datetime.strptime(interval[0], "%H:%M")
        loppaeg = datetime.strptime(interval[1], "%H:%M")

        for regaeg in regajad:
            regalgus = datetime.strptime(regaeg[0], "%H:%M")
            reglopp = regalgus + timedelta(minutes=regaeg[1])  # добавляем длительность услуги

            # Проверяем, пересекается ли текущий интервал с забронированным
            if (regalgus <= algaeg < reglopp) or (regalgus < loppaeg <= reglopp):
                kinni = True
                break

        if not kinni:
            vabadajad.append(interval)
    conn.close()
    return vabadajad

def kuvavabadajad(valkuupaev, vabadajadlistbox, algaasta, algkuu):
    from kalenderDef import kalenderaken

    kuupaev = f"{algaasta}-{algkuu:02d}-{valkuupaev:02d}"  # Форматируем дату YYYY-MM-DD

    vabadajadlistbox.delete(0, END)  # Очищаем список перед обновлением

    vabad_ajad = vabadajad(kuupaev)  # Получаем список свободных времен
    if vabad_ajad:
        for algus, lopp in vabad_ajad:
            aeg = f"{algus} - {lopp}" 
            vabadajadlistbox.insert(END, aeg)  # Добавляем каждый свободный слот
    else:
        vabadajadlistbox.insert(END, "Pole vabu aegu")  # Сообщение, если нет свободных времен
    vabadajadlistbox.bind("<<ListboxSelect>>", vali_aeg)

def vali_aeg(event):
    global valitud_aeg
    valitud_aeg.set(event.widget.get(event.widget.curselection()))

