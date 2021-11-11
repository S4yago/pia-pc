import argparse
import hashlib
import re
from prettytable import PrettyTable
from colored import fg, bg, attr


def menu():
    r = attr(0)
    while True:
        print("%s+-----------------------------------------+%s" % (fg(1), r))
        print("%s|%s                 %sMENU%s                    %s|%s" % (fg(1), r, fg(30), r, fg(1), r,))
        print("%s+-----------------------------------------+%s" % (fg(1), r))
        print("%s|%s        %s1. Obtener clave hash%s            %s|%s" % (fg(1), r, fg(3), r, fg(1), r))
        print("%s|%s              %s2. Salir%s                   %s|%s" % (fg(1), r, fg(3), r, fg(1), r))
        print("%s+-----------------------------------------+%s" % (fg(1), r))
        opcion = (int(input("%sElige una opción:%s " % (fg(6), r))))
        if(opcion > 2):
            print('Inválido. Ingrese de nuevo')
        if (opcion == 1):
            print("%s+-----------------------------------------+%s" % (fg(1), r))
            print("%s|%s              %sObtener clave%s              %s|%s" % (fg(1), r, fg(3), r, fg(1), r))
            print("%s+-----------------------------------------+%s" % (fg(1), r))
            direccion = []
            i = 1
            while i == 1:
                dir = input("Ingrese la dirección del archivo: ")
                direccion.append(dir)
                i = int(input("Ingrese un 1 para seguir agregando, "
                        "de lo contrario cualquier otro numero: "))
                with open('direcciones.txt', 'a') as file:
                    for item in direccion:
                        file.write("%s\n" % item)

            with open('direcciones.txt', 'rb') as fr:
                byte = fr.read()
                f = open("direcciones.txt", "r")
                lines = f.readlines()
                for linea in lines:
                    print('Opciones: 1. md5,  2. sha256, 3. sha512, 4. salir')
                    hashop = (int(input
                              ("Selecciona una de las" +
                               "opciones para hashear: ")))
                    if (hashop > 4):
                        print('Inválido. Ingrese de nuevo')
                    if (hashop == 1):
                        md5 = hashlib.md5()
                        md5.update(byte)
                        x = PrettyTable()
                        x.field_names = ["Hash", "Direccion", "Clave hash"]
                        x.add_row(["md5", linea, "{}".format(md5.hexdigest())])
                        f = open('resultados.txt', 'a')
                        f.write("%s\n" % str(x))
                        f.close()
                        global clave1
                        clave1 = "{}".format(md5.hexdigest())
                        print(linea, 'hashing...')

                    if (hashop == 2):
                        sha256 = hashlib.sha256()
                        sha256.update(byte)
                        y = PrettyTable()
                        y.field_names = ["Hash", "Direccion", "Clave hash"]
                        y.add_row(["sha256",
                                   linea,
                                   "{}".format(sha256.hexdigest())])
                        f = open('resultados.txt', 'a')
                        f.write("%s\n" % str(y))
                        f.close()
                        global clave2
                        clave2 = "{}".format(sha256.hexdigest())
                        print(linea, 'hashing...')

                    if (hashop == 3):
                        sha512 = hashlib.sha512()
                        sha512.update(byte)
                        z = PrettyTable()
                        z.field_names = ["Hash", "Direccion", "Clave hash"]
                        z.add_row(["sha512",
                                   linea,
                                   "{}".format(sha512.hexdigest())])
                        f = open('resultados.txt', 'a')
                        f.write("%s\n" % str(z))
                        f.close()
                        global clave3
                        clave3 = "{}".format(sha512.hexdigest())
                        print(linea, 'hashing...')

                    if (hashop == 4):
                        break
                f.close()
        if (opcion == 3):
            print("%s%sHasta la próxima!%s" % (fg(3), attr(4), r))
            break
