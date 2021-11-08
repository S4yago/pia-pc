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


def cesar_crack():

    with open (params.file) as arch:
        texto = arch.read()

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,_-()/\#$%&=*'

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):

        lista = []

        translated = ''
        for symbol in texto:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated = translated + symbol
        lista.append(translated)

        #Validacion de cadenas en español
        for clave in lista:
            if isSpanish(clave):
                
                print("La posible traducción es: \n",clave)


def trans_decode():
 
    with open (params.file) as arch:
        texto = arch.read()

    key = len_key()
    finaltxt = decryptMessage(key, texto)

    print("El mensaje decodificado es: \n", finaltxt + '|') # Se imprime un |, para indicar el final del mensaje


def trans_encode():

    with open (params.file) as arch:
        texto = arch.read()

    key = len_key()
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(texto):

            ciphertext[column] += texto[currentIndex]
            currentIndex += key

    finaltxt = ''.join(ciphertext)
    print("El mensaje codificado es: \n", finaltxt + '|')


def trans_crack(): 
    
    with open (params.file) as arch:
        message = arch.read()
    
    if message != None:
        print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

        # Brute-force by looping through every possible key.
        for key in range(1, len(message)):
            print('Trying key #%s...' % (key))

            decryptedText = decryptMessage(key, message)
            if isSpanish(decryptedText):
                # Ask user if this is the correct decryption.
                print()
                print('Possible encryption hack:')
                print('Key %s: %s' % (key, decryptedText[:100]))
                print()
                print("NOTA: Si no estás satisfecho con el resultado... Revise la flag '-l' 😉")
                print('Enter D if done, anything else to continue hacking:')
                response = input('> ')

                if response.strip().upper().startswith('D'):
                    exit()
                
    else:
        print('Failed to hack encryption.')