import smtplib
import ssl
from email.message import EmailMessage

def saada_email(saaja, teema, sisu):
    saatja_email = "annaoleks88@gmail.com"
    saatja_parool = "xsiw uicd bpgw djpf"  # App Password for Gmail

    msg = EmailMessage()
    msg["Subject"] = teema
    msg["From"] = saatja_email
    msg["To"] = saaja
    msg.set_content(sisu)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls(context=context)
            smtp.login(saatja_email, saatja_parool)
            smtp.send_message(msg)
        print(f"[OK] Email saadetud -> {saaja}")
    except Exception as e:
        print(f"[VIGA] Emaili saatmine ebaõnnestus: {e}")