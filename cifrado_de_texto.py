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


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)
    

def isSpanish(message, wordPercentage=30, letterPercentage=85):
    # Por default, el 30% de las palabras deben existir en el diccionario, y
    # 85% de todos los caracteres en el mensaje deben ser letras o espacios
    # (no signos de puntuacion o numeros).
    
    wordsMatch = getSpanishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
    

def len_key():
    espacios = 1
    if params.key == None: 
        key = 5
    else:
        while espacios > 0:
            espacios = params.key.count(' ')
            if params.key.isalpha() == False:
                espacios += 1
        key = len(params.key)
    return key


def decryptMessage(key, message):

    numOfColumns = int(math.ceil(len(message) / float(key)))      # Numero de columnas de la matriz
    numOfRows = key        # Numero de filas de la matriz 
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)  # Numero de casillas sin usar  
    plaintext = [''] * numOfColumns

    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1                                             

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    finaltxt = ''.join(plaintext)
    return finaltxt


def cesar_decode_and_encode():

    with open (params.file) as arch:
        texto = arch.read()

    key = len_key()

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,_-()/\#$%&=*'

    translated = ''

    for symbol in texto:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            if params.function == 'decode':
                translatedIndex = symbolIndex - key
            else:
                translatedIndex = symbolIndex + key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print("Mensaje decodificado:\n" + translated)