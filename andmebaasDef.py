import pyodbc
from datetime import datetime, timedelta
from tkinter import END

# Эти переменные теперь обычные строки (можно задавать их позже вручную из GUI)
valitud_aeg = ""
valitud_kuupaev = ""

def baasuhendus():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=(localdb)\\MSSQLLocalDB;"
        "DATABASE=manik;"
        "Trusted_Connection=yes;"
    )
    return conn

def registrkogus(paev):
    conn = baasuhendus()
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
    conn = baasuhendus()
    cursor = conn.cursor()
    query = '''
    INSERT INTO registr (klient_id, teenus_id, kuupaev, aeg)
    VALUES (?, ?, ?, ?)'''
    cursor.execute(query, (klient_id, teenus_id, kuupaev, aeg))
    conn.commit()
    conn.close()

def regajadelist(kuupaev):
    conn = baasuhendus()
    cursor = conn.cursor()
    query = '''
    SELECT aeg, kestvus 
    FROM registr
    JOIN teenused ON registr.teenus_id = teenused.id
    WHERE kuupaev = ?'''
    cursor.execute(query, (kuupaev,))
    result = cursor.fetchall()
    conn.close()
    return result

def vabadajad(kuupaev):
    conn = baasuhendus()
    cursor = conn.cursor()

    tooalgus = datetime.strptime("09:00", "%H:%M")
    toolopp = datetime.strptime("18:00", "%H:%M")

    koikajad = []
    algus = tooalgus
    while algus < toolopp:
        jargaeg = algus + timedelta(minutes=90)
        koikajad.append((algus.strftime("%H:%M"), jargaeg.strftime("%H:%M")))
        algus = jargaeg

    regajad = regajadelist(kuupaev)

    vabadajad = []
    for interval in koikajad:
        kinni = False
        algaeg = datetime.strptime(interval[0], "%H:%M")
        loppaeg = datetime.strptime(interval[1], "%H:%M")

        for regaeg in regajad:
            kestvus = regaeg[1]
            time_str = str(regaeg[0])
            try:
                regalgus = datetime.strptime(time_str, "%H:%M")
            except ValueError:
                regalgus = datetime.strptime(time_str, "%H:%M:%S")

            reglopp = regalgus + timedelta(minutes=kestvus)

            if (regalgus <= algaeg < reglopp) or (regalgus < loppaeg <= reglopp):
                kinni = True
                break

        if not kinni:
            vabadajad.append(interval)

    conn.close()
    return vabadajad

def kuvavabadajad(valkuupaev, vabadajadlistbox, algaasta, algkuu):
    import andmebaasDef

    kuupaev = f"{algaasta}-{algkuu:02d}-{valkuupaev:02d}"
    vabadajadlistbox.delete(0, END)

    andmebaasDef.valitud_kuupaev = kuupaev

    vabad_ajad = vabadajad(kuupaev)
    if vabad_ajad:
        for algus, lopp in vabad_ajad:
            aeg = f"{algus} - {lopp}"
            vabadajadlistbox.insert(END, aeg)
    else:
        vabadajadlistbox.insert(END, "Pole vabu aegu")

    vabadajadlistbox.bind("<<ListboxSelect>>", vali_aeg)

def vali_aeg(event):
    import andmebaasDef
    andmebaasDef.valitud_aeg = event.widget.get(event.widget.curselection())
