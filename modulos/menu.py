import os
import time
import logging

from colored import fg, attr
from modulos import web_scraping, cifrado_de_texto, claves_hash, port_scanning, shodan

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

r = attr(0)


def intro():
    import pygame

    print("[+] No se ha especificado ningun metodo...")
    time.sleep(1)
    print("[+] Ejecutando menu...")
    time.sleep(1.5)
    os.system("clear")
    filenames = ["./frames/1.txt", "./frames/2.txt", "./frames/3.txt", "./frames/4.txt", "./frames/5.txt",
                 "./frames/6.txt"]
    frames = []
    pygame.init()
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(
        "./frames/mixkit-small-sci-fi-glitch-1030.wav")
    pygame.mixer.Sound.play(sonido_fondo, -1)
    for name in filenames:
        with open(name, "r", encoding="utf-8") as f:
            frames.append(f.readlines())
    for i in range(3):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.1)
            os.system("clear")
    pygame.mixer.pause()
    print(
        """
        ██████╗ ██╗   ██╗ ██╗██╗         ████████╗ ██████╗  ██████╗ ██╗
        ╚════██╗██║   ██║███║██║         ╚══██╔══╝██╔═══██╗██╔═══██╗██║
         █████╔╝██║   ██║╚██║██║            ██║   ██║   ██║██║   ██║██║
         ╚═══██╗╚██╗ ██╔╝ ██║██║            ██║   ██║   ██║██║   ██║██║
        ██████╔╝ ╚████╔╝  ██║███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗
        ╚═════╝   ╚═══╝   ╚═╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ v2.0🚀
                                creado por:
                         👑 Angel Saúl Sáyago Leiba
                         🛐 Paulina Gómez Rodríguez
                         🦕 Deivi Rodríguez Rangel
                         🥸 Jesus Gerardo Gaytan Montelongo
    """
    )


def back_to_menu():
    time.sleep(1)
    input("\n[+] Presione la tecla enter para volver al menu...")
    os.system("clear")


def scraping():
    print("%s+--------------------------------------------------------------------------+%s" % (fg(1), r))
    print("%s|%s    %s‼️️ Ingresa el nombre del portal de noticias (larepublica,diario)%s      %s|%s" %
          (fg(1), r, fg(3), r, fg(1), r))
    print("%s+--------------------------------------------------------------------------+%s" % (fg(1), r))
    arg_news = input("%s-->%s " % (fg(30), r))
    return arg_news


def cifrado():
    print("%s+-----------------------------------------------------------+%s" % (fg(1), r))
    print("%s|%s       %s⚠️ Ingresa el lenguaje que utilizaras (en,es)%s       %s|%s" %
          (fg(1), r, fg(3), r, fg(1), r))
    print("%s+-----------------------------------------------------------+%s" % (fg(1), r))
    arg_language = input("%s-->%s " % (fg(30), r))
    print("%s+--------------------------------------------------------------------+%s" % (fg(1), r))
    print("%s|%s       %s‼️ Ingresa el metodo de cifrado (cesar,transposición)%s        %s|%s" %
          (fg(1), r, fg(3), r, fg(1), r))
    print("%s+--------------------------------------------------------------------+%s" % (fg(1), r))
    arg_metodo = input("%s-->%s " % (fg(30), r))
    print("%s+-------------------------------------------------------------------+%s" % (fg(1), r))
    print("%s|%s       %s‼ Ingresa la función a realizar (encode,decode,crack)%s       %s|%s" %
          (fg(1), r, fg(3), r, fg(1), r))
    print("%s+-------------------------------------------------------------------+%s" % (fg(1), r))
    arg_function = input("%s-->%s " % (fg(30), r))

    name = ""
    if arg_function == "encode":
        name = "codificación"
    elif arg_function == "decode":
        name = "decodificación"

    print("%s+-----------------------------------------------------------+%s" % (fg(1), r))
    print("%s|%s       %s⚠️ Ingresa la clave para la {} %s        %s|%s".format(name) %
          (fg(1), r, fg(3), r, fg(1), r))
    print("%s+-----------------------------------------------------------+%s" % (fg(1), r))
    arg_key = input("%s-->%s " % (fg(30), r))
    print("%s+-------------------------------------------------------------+%s" % (fg(1), r))
    print("%s|%s       %s‼️ Ingresa el path del archivo .txt a codificar %s      %s|%s" %
          (fg(1), r, fg(3), r, fg(1), r))
    print("%s+-------------------------------------------------------------+%s" % (fg(1), r))
    arg_file = input("%s-->%s " % (fg(30), r))
    return arg_language, arg_metodo, arg_function, arg_key, arg_file


def api():
    print("%s+----------------------------------------------+%s" % (fg(1), r))
    print("%s|%s    %s⚠️️️️️ Ingresa la API KEY de Shodan%s           %s|%s" %
          (fg(1), r, fg(3), r, fg(1), r))
    print("%s+----------------------------------------------+%s" % (fg(1), r))
    arg_key = input("%s-->%s " % (fg(30), r))
    print("%s+--------------------------------------------------------+%s" % (fg(1), r))
    print("%s|%s    %s‼️ Ingresa el path del archivo con las IP's%s         %s|%s" %
          (fg(1), r, fg(3), r, fg(1), r))
    print("%s+--------------------------------------------------------+%s" % (fg(1), r))
    arg_path = input("%s-->%s " % (fg(30), r))
    return arg_key, arg_path


def menu():
    _exit = False

    logger = logging.getLogger("Error_Log")
    logger.setLevel(logging.ERROR)
    try:
        fh = logging.FileHandler("./data/logs/error.log")
    except:
        os.mkdir("./data/logs")
        fh = logging.FileHandler("./data/logs/error.log")
    fh.setLevel(logging.ERROR)
    logger.addHandler(fh)

    while not _exit:
        print("%s+-----------------------------------------+%s" % (fg(1), r))
        print("%s|%s                 %sMENU%s                    %s|%s" %
              (fg(1), r, fg(30), r, fg(1), r,))
        print("%s+-----------------------------------------+%s" % (fg(1), r))
        print("%s|%s          %s1. Web Scraping   %s             %s|%s" %
              (fg(1), r, fg(3), r, fg(1), r))
        print("%s|%s          %s2. Cifrar un texto%s             %s|%s" %
              (fg(1), r, fg(3), r, fg(1), r))
        print("%s|%s          %s3. Sacar claves hash%s           %s|%s" %
              (fg(1), r, fg(3), r, fg(1), r))
        print("%s|%s          %s4. Hacer un escaneo%s            %s|%s" %
              (fg(1), r, fg(3), r, fg(1), r))
        print("%s|%s          %s5. API Shodan         %s         %s|%s" %
              (fg(1), r, fg(3), r, fg(1), r))
        print("%s|              0. Salir                   |%s" %
              (fg(1), r))
        print("%s+-----------------------------------------+%s" % (fg(1), r))
        opt = (input("%sElige una opción:%s " % (fg(6), r)))

        os.system("clear")
        if opt == "1":
            try:
                web_scraping.run(scraping())
                back_to_menu()
            except Exception as e:
                print("\n", e)
                logger.error(e)
                back_to_menu()
        elif opt == "2":
            arg1, arg2, arg3, arg4, arg5 = cifrado()
            if arg1 == '':
                arg1 = None
            if arg4 == '':
                arg4 = None
            try:
                cifrado_de_texto.run(arg1, arg2, arg3, arg4, arg5)
                back_to_menu()
            except Exception as e:
                print("\n", e)
                logger.error(e)
                back_to_menu()
        elif opt == "3":
            try:
                claves_hash.menu()
                back_to_menu()
            except Exception as e:
                print("\n", e)
                logger.error(e)
                back_to_menu()
        elif opt == "4":
            try:
                port_scanning.menu()
                back_to_menu()
            except Exception as e:
                print("\n", e)
                logger.error(e)
                back_to_menu()
        elif opt == "5":
            arg1, arg2 = api()
            try:
                shodan.run(arg1, arg2)
                back_to_menu()
            except Exception as e:
                print("\n", e)
                logger.error(e)
                back_to_menu()
        elif opt == "0":
            _exit = True
        else:
            print("[!] Opción no valida!")
            back_to_menu()


def run():
    intro()
    menu()
