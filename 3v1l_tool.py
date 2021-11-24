#!/usr/bin/env python3

import argparse
import os

from modulos import cifrado_de_texto, claves_hash, port_scanning, web_scraping, shodan, menu

msj2 = "clave para la codificación o decodificación. Default = 5"
parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('MODOS')
scraping_group = parser.add_argument_group('PARAMETROS WEB SCRAPING')
cifrado_group = parser.add_argument_group('PARAMETROS CIFRADO')
hash_group = parser.add_argument_group('PARAMETROS HASH')
scan_group = parser.add_argument_group('PARAMETROS PORT SCANNING')
api_group = parser.add_argument_group('PARAMETROS API SHODAN')

# Metodo
required.add_argument('-m',
                      type=str, dest="mode", choices=['scraping', 'encoding', 'hash', 'scan', 'api'],
                      help='herramienta a utilizar')

# Web Scraping
scraping_group.add_argument("--news", dest="news", type=str, choices=['larepublica', 'diario'],
                         help="ingrese el nombre del portal de noticias")

# Cifrado de Texto
cifrado_group.add_argument("--language", dest="language", help="lenguaje a utilizar. [OPCIONAL] Default=es",
                           choices=['en', 'es'], default="es")
cifrado_group.add_argument('--metodo-cifrado',
                           type=str, dest="metodo", choices=['cesar', 'transposicion'],
                           help='metodo de cifrado')
cifrado_group.add_argument('--function',
                           type=str, dest="function", choices=['encode', 'decode', 'crack'],
                           help='funcion a realizar')
cifrado_group.add_argument(
    "--key", dest="key", help="clave para la codificación o decodificación. [OPCIONAL] Default=5")
cifrado_group.add_argument("--path", dest="file",
                           help="path absoluto del archivo .txt a codificar")

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

# API Shodan
api_group.add_argument('--api-key', dest="api_key", type=str, default="8Mpsy8tdQBzdGedUlHmY0dUxKZgxqujp",
                       help='ingresar la API_KEY de Shodan (Por default ya viene una incluida)')
api_group.add_argument('--shodan-path', dest="path", type=str,
                       help="ingresar el path del archivo con las IP's a analizar")

args = parser.parse_args()


if __name__ == "__main__":

    if not os.path.exists("./data/"):
        os.mkdir("./data/")

    if args.mode == 'scraping':
        web_scraping.run(args.news)
    elif args.mode == 'encoding':
        cifrado_de_texto.run(args.language, args.metodo,
                             args.function, args.key, args.file)
    elif args.mode == 'hash':
        claves_hash.run(args.hash, args.cifrado)
    elif args.mode == 'scan':
        port_scanning.run(args.host, args.port)
    elif args.mode == 'api':
        shodan.run(args.api_key, args.path)
    elif args.mode == None:
        menu.run()
