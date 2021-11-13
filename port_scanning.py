import colorama
from socket import *
import socket
from threading import *
import threading
import time
import os
import concurrent.futures
from colorama import Fore

colorama.init()

print_lock = threading.Lock()


def connscan(tgtHost, tgtPort):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((tgtHost, tgtPort))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{tgtPort}]" + Fore.GREEN + " Abierto")
    except:
        print (Fore.WHITE + f"[{tgtPort}]" + Fore.RED + " Cerrado")
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


def scan(tgtHost, tgtPorts):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((tgtHost, tgtPorts))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{tgtPorts}]" + Fore.GREEN + " Abierto")
    except:
        pass


def menu():
    salir = False
    opcion = 0

    while not salir:
        print(Fore.RED +
              "+------------------------------------------------------+")
        print(Fore.RED +
              "|" +
              Fore.WHITE +
              "                         MENU                         " +
              Fore.RED + "|")
        print(Fore.RED +
              "+------------------------------------------------------+")
        print(Fore.RED +
              "|" +
              Fore.WHITE +
              "    1. Escanear todos los puertos abiertos al Host    " +
              Fore.RED + "|")
        print(Fore.RED +
              "|" +
              Fore.WHITE +
              "    2. Escanear puertos especificos del Host          " +
              Fore.RED + "|")
        print(Fore.RED +
              "|" + Fore.WHITE +
              "    3. Salir                                          " +
              Fore.RED + "|")
        print(Fore.RED +
              "+------------------------------------------------------+" +
              Fore.RESET)
        opcion = input("Selecciona una opcion: ")
        os.system("cls")

        if opcion == "1":
            print(Fore.RED +
                  "+------------------------------------------------------+")
            print(Fore.RED + "|" +
                  Fore.WHITE +
                  "     Escanear todos los puertos abiertos al Host      " +
                  Fore.RED + "|")
            print(Fore.RED +
                  "+------------------------------------------------------+" +
                  Fore.RESET)
            ip = input("Ingresa la ip a escanear: ")
            tgtPorts = 0
            print ("[+] Escaneando... ")
            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                for tgtPorts in range(1000):
                    executor.submit(scan, ip, tgtPorts + 1)
        elif opcion == "2":
            print(Fore.RED +
                  "+------------------------------------------------------+")
            print(Fore.RED +
                  "|" + Fore.WHITE +
                  "        Escanear puertos especificos del Host         " +
                  Fore.RED + "|")
            print(Fore.RED +
                  "+------------------------------------------------------+" +
                  Fore.RESET)
            ip = input("Ingresa la ip a escanear: ")
            port = input("Ingresa el puerto a escanear: ")
            portscanner(ip, str(port).split(','))
            time.sleep(5)
        elif opcion == "3":
            print("Nos vemos!")
            salir = True
        else:
            print("""No haz seleccionado una opcion correcta, introduce
                  la opcion que deseas del 1 al 3... \npulsa una tecla
                  para continuar""")


def run(arg1, arg2):

    tgtHost = arg1
    tgtPorts = str(arg2).split(',')

    if arg1 is not None and arg2 is not None:
        portscanner(tgtHost, tgtPorts)
    elif arg1 is not None and arg2 is None:
        tgtPorts = arg2
        print ("[+] Escaneando... ")
        with concurrent.futures.ThreadPoolExecutor(
                                                   max_workers=100
                                                   ) as executor:
            for tgtPorts in range(1000):
                executor.submit(scan, tgtHost, tgtPorts + 1)
    elif arg1 is None and arg2 is None:
        menu()