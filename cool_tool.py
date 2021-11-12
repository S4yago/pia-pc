#!/usr/bin/env python3

import envio_de_correos, cifrado_de_texto, claves_hash
import argparse


msj2= "Clave para la codificación o decodificación. Default = 5"
parser = argparse.ArgumentParser()

# Metodo
parser.add_argument('-m',
                    type=str, dest="mode", choices=['email', 'encryption', 'hash'],
                    required=True,
                    help='metodo')

# Emails
parser.add_argument("--email-json", dest="email_json", type=str,
                    help="path absoluto del archivo .json")
parser.add_argument("--email-txt", dest="email_txt", type=str,
                    help="path absoluto del archivo .txt")
parser.add_argument("--email-file", dest="email_file", type=str,
                    help="path absoluto del archivo a adjuntar")

# Cifrado de Texto
parser.add_argument("-l", dest="language", help="Lenguaje a utilizar",
                    choices=['en','es'], default="es", required=False)
parser.add_argument('--metodo-cifrado',
                    type=str, dest="metodo", choices=['cesar', 'transposicion'],
                    required=False,
                    help='Metodo de cifrado')
parser.add_argument('--email-function',
                    type=str, dest="function", choices=['encode', 'decode', 'crack'],
                    required=False,
                    help='Funcion a realizar')
parser.add_argument("-k", dest="key", help=msj2, required=False)
parser.add_argument("-a", dest="file", help="Path absoluto del archivo .txt a codificar", required=False)

# Claves hash
parser.add_argument('--hash',
                    dest='hash',
                    choices=['md5', 'sha256', 'sha512'],
                    help="Si desea obtener la clave hash," +
                    "es necesario especificar que tipo")
parser.add_argument("--cifrado",
                    dest='cifrado',
                    type=str,
                    help="Se debe poner una dirección de" +
                    "archivo existente dentro del sistema")

args = parser.parse_args()


if __name__ == "__main__":

    if args.mode.lower() == 'email':
        envio_de_correos.main(args.email_json, args.email_txt, args.email_file)
    elif args.mode.lower() == 'encryption':
        cifrado_de_texto.main(args.language, args.metodo, args.function, args.key, args.file)
    elif args.mode.lower() == 'hash':
        claves_hash.main(args.hash, args.cifrado)
    elif args.mode.lower() == 'encryption':
        print('hello')
    elif args.mode.lower() == 'pwned':
        print('hello')
    elif args.mode.lower() == 'scan':
        print('hello')
    else:
        print(
            "¡Error! Escoge un modo valido: [pwned, scraping, hash, encryption, email, scan]")
