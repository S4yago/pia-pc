import hashlib
from prettytable import PrettyTable
from colored import fg, attr


def menu():
    r = attr(0)
    opcion = 1
    if (opcion == 1):
        print("%s+-----------------------------------------+%s" % (fg(1), r))
        print("%s|%s              %sObtener clave%s              %s|%s" %
              (fg(1), r, fg(3), r, fg(1), r))
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
                    f = open('./data/resultados-hash.txt', 'a')
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
                    f = open('./data/resultados-hash.txt', 'a')
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
                    f = open('./data/resultados-hash.txt', 'a')
                    f.write("%s\n" % str(z))
                    f.close()
                    global clave3
                    clave3 = "{}".format(sha512.hexdigest())
                    print(linea, 'hashing...')

                if (hashop == 4):
                    break
            f.close()


def cifrar():
    direccion = []
    dir = arg_direccion
    direccion.append(dir)
    # with open('directions.txt', 'a') as file:
    #     for item in direccion:
    #         file.write("%s\n" % item)

    with open('directions.txt', 'rb') as fr:
        byte = fr.read()
        f = open("directions.txt", "r")
        lines = f.readlines()
        for linea in lines:
            if arg_modo == 'md5':
                md5 = hashlib.md5()
                md5.update(byte)
                x = PrettyTable()
                x.field_names = ["Hash", "File", "Clave hash"]
                x.add_row(["md5", linea, "{}".format(md5.hexdigest())])
                f = open('./data/results-md5.txt', 'a')
                f.write("%s\n" % str(x))
                f.close()
                print(linea, 'hashing...')
                print('Completed!')

            if arg_modo == 'sha256':
                sha256 = hashlib.sha256()
                sha256.update(byte)
                y = PrettyTable()
                y.field_names = ["Hash", "File", "Clave hash"]
                y.add_row(["sha256", linea, "{}".format(sha256.hexdigest())])
                f = open('./data/results-sha256.txt', 'a')
                f.write("%s\n" % str(y))
                f.close()
                print(linea, 'hashing...')
                print('Completed!')

            if arg_modo == 'sha512':
                sha512 = hashlib.sha512()
                sha512.update(byte)
                z = PrettyTable()
                z.field_names = ["Hash", "File", "Clave hash"]
                z.add_row(["sha512", linea, "{}".format(sha512.hexdigest())])
                f = open('./data/results-sha512.txt', 'a')
                f.write("%s\n" % str(z))
                f.close()
                print(linea, 'hashing...')
                print('Completed!')


def run(arg1, arg2):

    global arg_modo
    global arg_direccion

    arg_modo = arg1
    arg_direccion = arg2

    if arg_modo == 'md5':
        cifrar()
    elif arg_modo == 'sha256':
        cifrar()
    elif arg_modo == 'sha512':
        cifrar()
