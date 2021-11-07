#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import argparse
import json
import smtplib, ssl
from colored import fg, bg, attr
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


msj1 = "Envio de correos"
description =""" Modo de uso 😃:
    envio_de_correos.py -j "example.json" -e "example.txt" [-f] "path" 
    """
parser = argparse.ArgumentParser(description=msj1,
                                epilog=description, 
                                formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-j", dest="credentials", type=str, help="Path absoluto del archivo .json", required=False)
parser.add_argument("-e", dest="email", type=str, help="Path absoluto del archivo .txt", required=False)
parser.add_argument("-f", dest="file", type=str, help="Path absoluto del archivo a adjuntar", required=False)
params = parser.parse_args()

arg_json = params.credentials
arg_txt = params.email
arg_file = params.file

def open_json(arg_json):
    data = {}
    with open(arg_json) as cred:
        data = json.load(cred)
        global user
        global password
        user = data["user"]
        password = data["pass"]


def menu():
    r = attr(0)
    print("%s+-----------------------------------------------+%s" % (fg(1), r))
    print("%s|%s       %sIngresa el path del archivo .json%s       %s|%s" % (fg(1), r, fg(3), r, fg(1), r))
    print("%s+-----------------------------------------------+%s" % (fg(1), r))
    arg_json = input("%s-->%s " % (fg(30), r))
    print("%s+-----------------------------------------------+%s" % (fg(1), r))
    print("%s|%s       %sIngresa el path del archivo .txt%s        %s|%s" % (fg(1), r, fg(3), r, fg(1), r))
    print("%s+-----------------------------------------------+%s" % (fg(1), r))
    arg_txt = input("%s-->%s " % (fg(30), r))
    print("%s+---------------------------------------------------+%s" % (fg(1), r))
    print("%s|%s       %sIngresa el path del archivo a adjuntar%s      %s|%s" % (fg(1), r, fg(3), r, fg(1), r))
    print("%s+---------------------------------------------------+%s" % (fg(1), r))
    arg_file = input("%s-->%s " % (fg(30), r))
    return arg_json, arg_txt, arg_file


def main():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
 
    try:
        smtp.login(user, password)
        print("\n\tConexión exitosa c:")
    except:
        print("\n\tUsuario o contraseña no validos :c")
        exit()


# Abre el archivo txt y retorna los "emails", el "subject" y el "body".
def extract_data(arg_txt):
    with open(arg_txt, "r") as em:
        line_emails = em.readlines()[0].replace('\n', '')
        emails = line_emails.split(",") # Se guarda en una lista
        em.seek(0) # Vuelve al inicio del archivo
        line_subject = em.readlines()[1].replace('\n', '')
        em.seek(0)
        line_body = em.readlines()[3:]
        formatted_body = "".join(line_body)
        form(emails, line_subject, formatted_body)


def form(emails, line_subject, line_body):
    subject = line_subject
    body = line_body
    file = arg_file
    receiver_emails = ", ".join(emails)

    # Se crea el objeto, y se declaran los headers
    message = MIMEMultipart() 
    message["From"] = user
    message["To"] = receiver_emails
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain")) # Se añade el contenido del mensaje

    if arg_file is not None:
        filename = file  

        with open(filename, "rb") as attachment: # Se abre el archivo en bytes owo

            part = MIMEBase("application", "octet-stream") # Se añade el archivo como application/octet-stream
            part.set_payload(attachment.read())

        encoders.encode_base64(part) # Se codifica en ascii lo que se enviará

        # Se le añade un header al archivo
        part.add_header( 
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Se añade el archivo al mensaje y se hace cadena
        message.attach(part)

    text = message.as_string()
    send_message(receiver_emails, text)


def send_message(receiver_emails, text):
    # Nos logeamos y mandamos el mensaje
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(user, password)
        server.sendmail(user, receiver_emails, text)
        print("\n\tCorreo enviado exitosamente, bye! uwu")



