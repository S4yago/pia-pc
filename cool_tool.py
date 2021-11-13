#!/usr/bin/env python3

import envio_de_correos, cifrado_de_texto, claves_hash, port_scanning, api_github, menu
import argparse

msj2= "clave para la codificación o decodificación. Default = 5"
parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('MODOS')
email_group = parser.add_argument_group('PARAMETROS EMAIL')
cifrado_group = parser.add_argument_group('PARAMETROS CIFRADO')
hash_group = parser.add_argument_group('PARAMETROS HASH')
scan_group = parser.add_argument_group('PARAMETROS PORT SCANNING')
api_group = parser.add_argument_group('PARAMETROS API GITHUB')

# Metodo
required.add_argument('-m',
                    type=str, dest="mode", choices=['email', 'encoding', 'hash', 'scan', 'api'],
                    help='herramienta a utilizar')

# Emails
email_group.add_argument("--email-json", dest="email_json", type=str,
                    help="path absoluto del archivo .json")
email_group.add_argument("--email-txt", dest="email_txt", type=str,
                    help="path absoluto del archivo .txt")
email_group.add_argument("--email-file", dest="email_file", type=str,
                    help="path absoluto del archivo a adjuntar")

# Cifrado de Texto
cifrado_group.add_argument("--language", dest="language", help="lenguaje a utilizar",
                    choices=['en','es'], default="es")
cifrado_group.add_argument('--metodo-cifrado',
                    type=str, dest="metodo", choices=['cesar', 'transposicion'],
                    help='metodo de cifrado')
cifrado_group.add_argument('--function',
                    type=str, dest="function", choices=['encode', 'decode', 'crack'],
                    help='funcion a realizar')
cifrado_group.add_argument("--key", dest="key", help="clave para la codificación o decodificación. Default=5")
cifrado_group.add_argument("--path", dest="file", help="path absoluto del archivo .txt a codificar")

# Claves hash
hash_group.add_argument('--hash',
                    dest='hash',
                    choices=['md5', 'sha256', 'sha512'],
                    help="tipo de clave hash a utilizar")
hash_group.add_argument("--cifrado",
                    dest='cifrado',
                    type=str,
                    help="dirección de algun archivo existente en el sistema")

# Port Scanning
scan_group.add_argument('--host', dest="host", type=str,
                    help='indicar el host objetivo')
scan_group.add_argument('--port', dest="port", type=str,
                    help='indicar el puerto objetivo [OPCIONAL]')

# API GitHub
api_group.add_argument('--user', dest="user", type=str,
                    help='ingresar el usuario de GitHub')
api_group.add_argument('--repository', dest="repo", type=str,
                    help='ingresar el nombre del repositorio')
api_group.add_argument('--token', dest="token", type=str,
                    help='ingresar el token OAuth de GitHub')

args = parser.parse_args()


if __name__ == "__main__":

    if args.mode == 'email':
        envio_de_correos.run(args.email_json, args.email_txt, args.email_file)
    elif args.mode == 'encoding':
        cifrado_de_texto.main(args.language, args.metodo, args.function, args.key, args.file)
    elif args.mode == 'hash':
        claves_hash.main(args.hash, args.cifrado)
    elif args.mode == 'scan':
        port_scanning.run(args.host, args.port)
    elif args.mode == 'api':
        api_github.run(args.user, args.repo, args.token)
    elif args.mode == None:
        menu.run()