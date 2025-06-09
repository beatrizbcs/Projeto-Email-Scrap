import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
senha = os.getenv("EMAIL_SENHA")

def enviar_email(mensagem):
    remetente = "beatriz.beyond@gmail.com"
    destinatario = "beatriz.beyond@gmail.com"

    msg = MIMEText(mensagem)
    msg["Subject"] = "Dados Coletados"
    msg["From"] = remetente
    msg["To"] = destinatario

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, msg.as_string())