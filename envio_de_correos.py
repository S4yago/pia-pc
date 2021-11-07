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

