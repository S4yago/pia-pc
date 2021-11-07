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