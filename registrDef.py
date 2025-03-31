import pyodbc
from datetime import datetime, timedelta


conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=(localdb)\MSSQLLocalDB;"
    "DATABASE=manik;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

def lisaklient(klient_id, teenus_id, kuupaev, aeg):
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=(localdb)\MSSQLLocalDB;"
        "DATABASE=manik;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()

    # SQL-запрос для добавления бронирования
    query = '''
    INSERT INTO registr (klient_id, teenus_id, kuupaev, aeg)
    VALUES (?, ?, ?, ?)
    '''
    cursor.execute(query, (klient_id, teenus_id, kuupaev, aeg))
    conn.commit()

def regajadelist(kuupaev):
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=(localdb)\MSSQLLocalDB;"
        "DATABASE=manik;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()

    # SQL-запрос для получения всех забронированных интервалов для определенного дня
    query = '''
    SELECT aeg, kestvus 
    FROM registr
    JOIN teenused ON registr.teenus_id = teenused.id
    WHERE kuupaev = ?
    '''
    cursor.execute(query, (kuupaev,))
    return cursor.fetchall()

def vabadajad(kuupaev):
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=(localdb)\MSSQLLocalDB;"
        "DATABASE=manik;"
        "Trusted_Connection=yes;"
    )
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

    return vabadajad

def kuvavabadajad(valkuupaev):
    from kalenderDef import kalenderaken

    global vabadajadlistbox
    kuupaev = f"{algaasta}-{algkuu:02d}-{valkuupaev:02d}"  # Форматируем дату YYYY-MM-DD

    vabadajadlistbox.delete(0, END)  # Очищаем список перед обновлением

    vabad_ajad = vabadajad(kuupaev)  # Получаем список свободных времен
    if vabad_ajad:
        for aeg in vabad_ajad:
            vabadajadlistbox.insert(END, aeg)  # Добавляем каждый свободный слот
    else:
        vabadajadlistbox.insert(END, "Pole vabu aegu")  # Сообщение, если нет свободных времен


