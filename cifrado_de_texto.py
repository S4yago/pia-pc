# Copyright (c) 2021
# By ShadowFax

import argparse
import math 

description =""" Modo de uso 😃:
    cifrado_de_texto.py -m "Metodo" -f "Funcion" [-k][Default=5] "Clave"
    
    """

msj1 = " === Cifrado de texto, desde un archivo .txt ==="
msj2= "Clave para la codificación o decodificación. Default = 5"
parser = argparse.ArgumentParser(description=msj1,
                                epilog=description, 
                                formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-l", dest="language", help="Lenguaje a utilizar",
                    choices=['en','es'], default="es", required=False)
parser.add_argument('-m',
                    type=str, dest="metodo", choices=['cesar', 'transposicion'],
                    required=True,
                    help='Metodo de cifrado')
parser.add_argument('-f',
                    type=str, dest="function", choices=['encode', 'decode', 'crack'],
                    required=True,
                    help='Funcion a realizar')
parser.add_argument("-k", dest="key", help=msj2, required=False)
parser.add_argument("-a", dest="file", help="Path absoluto del archivo .txt a codificar", required=True)

params = parser.parse_args()

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary(language='es'):
    if language == 'es':
        dictionaryFile = open('dictEsp.txt',encoding='utf-8')
    else:
        dictionaryFile = open('dictEn.txt',encoding='utf-8')
    words = {}
    for word in dictionaryFile.read().split('\n'):
        word = word.upper()
        words[word] = None
    dictionaryFile.close()
    return words

WORDS = loadDictionary(params.language)

def getSpanishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split() # Divide un str por cada ' '

    if possibleWords == []:
        return 0.0 # No words at all, so return 0.0.

    matches = 0
    for word in possibleWords:
        if word in WORDS:
            matches += 1
    return float(matches) / len(possibleWords) # El porcentaje

