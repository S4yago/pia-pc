import math

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'


def loadDictionary(language='es'):
    if language == 'es':
        dictionaryFile = open('./dict/dictEsp.txt', encoding='utf-8')
    else:
        dictionaryFile = open('./dict/dictEn.txt', encoding='utf-8')
    words = {}
    for word in dictionaryFile.read().split('\n'):
        word = word.upper()
        words[word] = None
    dictionaryFile.close()
    return words


def getSpanishCount(message):

    WORDS = loadDictionary(arg_language)

    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()  # Divide un str por cada ' '

    if possibleWords == []:
        return 0.0  # No words at all, so return 0.0.

    matches = 0
    for word in possibleWords:
        if word in WORDS:
            matches += 1
    return float(matches) / len(possibleWords)  # El porcentaje


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
    if arg_key == None:
        key = 5
    else:
        while espacios > 0:
            espacios = arg_key.count(' ')
            if arg_key.isalpha() == False:
                espacios += 1
        key = len(arg_key)
    return key


def decryptMessage(key, message):

    # Numero de columnas de la matriz
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key        # Numero de filas de la matriz
    numOfShadedBoxes = (numOfColumns * numOfRows) - \
        len(message)  # Numero de casillas sin usar
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

    with open(arg_file) as arch:
        texto = arch.read()

    key = len_key()

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,_-()/\#$%&=*'

    translated = ''

    for symbol in texto:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            if arg_function == 'decode':
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

    with open(arg_file) as arch:
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

        # Validacion de cadenas en español
        for clave in lista:
            if isSpanish(clave):

                print("La posible traducción es: \n", clave)


def trans_decode():

    with open(arg_file) as arch:
        texto = arch.read()

    key = len_key()
    finaltxt = decryptMessage(key, texto)

    # Se imprime un |, para indicar el final del mensaje
    print("El mensaje decodificado es: \n", finaltxt + '|')


def trans_encode():

    with open(arg_file) as arch:
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

    with open(arg_file) as arch:
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
                print(
                    "NOTA: Si no estás satisfecho con el resultado... Revise la flag '-l' 😉")
                print('Enter D if done, anything else to continue hacking:')
                response = input('> ')

                if response.strip().upper().startswith('D'):
                    exit()

    else:
        print('Failed to hack encryption.')


def run(arg1, arg2, arg3, arg4, arg5):
    global arg_language
    global arg_method
    global arg_function
    global arg_key
    global arg_file

    arg_language = arg1
    arg_method = arg2
    arg_function = arg3
    arg_key = arg4
    arg_file = arg5

    if arg_method == 'cesar':
        if arg_function == 'encode' or arg_function == 'decode':
            cesar_decode_and_encode()
        elif arg_function == 'crack':
            cesar_crack()

    elif arg_method == 'transposicion':
        if arg_function == 'encode':
            trans_encode()
        elif arg_function == 'decode':
            trans_decode()
        elif arg_function == 'crack':
            trans_crack()
