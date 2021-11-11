import socket
from socket import *
import colorama
from colorama import Fore
import threading
from threading import *

colorama.init()

print_lock = threading.Lock()

def connscan(tgtHost, tgtPort):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((tgtHost, tgtPort))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{tgtPort}]" + Fore.GREEN + "Abierto")
    except:
        print (Fore.WHITE + f"[{tgtPort}]" + Fore.RED + "Cerrado")
    finally:
        scanner.close()

def portscanner(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print ("Unknown Host %s " % tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print ("[+] Escaneando: ") + tgtName[0]
    except:
        print ("Resultados del escaneo a: " + tgtIP)
    for tgtPort in tgtPorts:
        t = Thread(target=connscan, args=(tgtHost, int(tgtPort)))
        t.start()