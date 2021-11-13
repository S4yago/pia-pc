# PIA - 3V1L TOOL

**_3V1L TOOL_** es un programa exclusivo de linux que contiene herramientas para realizar tareas con relación a ciberseguridad.  
Entre ellas están:
* [Envio de correos](https://github.com/S4yago/pia-pc/blob/main/envio_de_correos.py)
* [Consulta a la API de GitHub](https://github.com/S4yago/pia-pc/blob/main/api_github.py)
* [Escaneo de puertos](https://github.com/S4yago/pia-pc/blob/main/port_scanning.py)
* [Obtención de claves HASH](https://github.com/S4yago/pia-pc/blob/main/claves_hash.py)
* [Cifrado de texto](https://github.com/S4yago/pia-pc/blob/main/cifrado_de_texto.py)


## Contenido

- [Pre-requisitos](#pre-requisitos)
- [Funcionamiento general](#funcionamiento-general) 
   - [Envio de correos](#f-envio-de-correos)
   - [Cifrado de texto](#f-cifrado-de-texto)
   - [Obtencion de claves HASH](#f-obtención-de-claves-hash)
   - [Consulta a la API de GitHub](#f-consulta-a-la-api-de-github)
   - [Escaneo de puertos](#f-escaneo-de-puertos)
- [Ejecución por menú](#ejecución-por-menú)
- [Ejecución por paso de argumentos](#ejecución-por-paso-de-argumentos)
   - [Envio de correos](#envio-de-correos)
   - [Cifrado de texto](#cifrado-de-texto)
   - [Obtencion de claves HASH](#obtención-de-claves-hash)
   - [Consulta a la API de GitHub](#consulta-a-la-api-de-github)
   - [Escaneo de puertos](#escaneo-de-puertos)
- [Autores](#autores)

## Comenzando 🚀

### Pre-requisitos

Para poder tener una ejecución exitosa del script se necesitaran instalar ciertos modulos 
que no vengan por default en python. Para ello ejecutará el siguiente comando

```
$ pip install -r requirements.txt
```
## Funcionamiento general

### F-Envio de correos

La herramienta de envio de correos, se utiliza para que puedas enviar correos electrónicos con dominio _gmail_, 
a una o más personas con la posibilidad de adjuntar archivos. El script, trabaja con 3 archivos dados por el usuario  que son:

* Un archivo .json - Que debe contener la información de la cuenta remitente, con esta estructura:

```
{
  "user": "su correo electrónico"
  "pass: "su contraseña"
  }
```

* Un archivo .txt - Que debe contener la información a enviar en el email, con esta estructura:

--> En la primera linea deberán estar todos los correos, a los que les quieras mandar el email, separadas por una coma  
--> En la segunda linea deberá intrucir el asunto(que no deberá ser más de una línea)  
--> Y de la cuarta linea en adelante podrá introducir todo el cuerpo de su email  

Por ejemplo:
```
correo1@gmail.com,correo2@gamil.com,correo3@gmail.com
Este es mi asunto

Este es el cuerpo
de mi 
email c:
```

* El path absoluto donde se encuentra el archivo que desea adjuntar

Por ejemplo:

```
/home/[user]/imagen3.png
```

### F-Cifrado de texto

La herramienta de cifrado de texto utiliza dos métodos (Cesar y Transposición) para codificar, decodificar y crackear un texto dado en formato .txt, tiene
la función, para que en tiempo de ejecución, se devuelva el texto ya codificado con el método y llaves indicadas.  
Para la función de crackeo también se cuenta con la posibilidad de indicar el idioma en el que se desea crackear un mensaje donde se podrá escoger entre
Inglés y Español (en, es)
El script trabaja con 1 archivo dado por el usuario:

* Path absoluto del txt

Por ejemplo:
```
/home/[user]/archivo.txt
```

### F-Obtención de claves HASH

La herramienta de obtención de claves HASH utiliza 3 métodos de encriptado HASH (md5, sha256 y sha512) para sacar la clave única de algún archivo dado
por el usuario.
El script trabaja con 1 archivo dado por el usuario:

* Path absoluto del archivo

Por ejemplo:

```
/home/[user]/PIACiberseguridad
```

### F-Consulta a la API de GitHub

La herramienta de api de GitHub hace una llamada a la API propiamente dicha y devuele un json con información del usuario y un repositorio.

### F-Escaneo de puertos

La heramienta de escaneo de puerto realiza un escaneo a varios puertos por default de algun host local dado por el usuario y te devuelve los puertos que
se encontraron abiertos, tiene la opción de especificar que puertos quieres que se escaneen si así lo deseas. 

## Ejecución

El script principal es **3v1l_tool.py**, que tiene 2 métodos:
* Con paso de argumentos
* Por menú

### Ejecución por menú

Si no se pasa ningun parametro al momento de la ejecución del script, automáticamente adoptará una interfaz para que se pueda llevar a cabo la ejecución
utlizando un menú interactivo

Por ejemplo:
```
$ ./3vil_tool.py 
```

### Ejecución por paso de argumentos

Para poder diferenciar entre alguna herramienta y otra se tomará en cuenta el parámetro **_'-m'_**  
Donde las opciones son: 
* _email_ - para envio de correos
* _encoding_ - para cifrado de texto
* _hash_ - para obtención de claves HASH
* _api_ - para consulta a la API de GitHub

Por ejemplo:

```
$ ./3vil_tool.py -m email
```

### Envio de correos
Para ejecutar la herramienta de **Envio de correos**, se tomarán en cuenta los parámetros:

* --email-json - path del archivo .json
* --email-txt - path del archivo .txt
* --email-file - path del archivo a adjuntar

Por ejemplo:

```
$ ./3vil_tool.py -m email --email-json "path del .json" --email-txt "path del .txt" --email-file "path del archivo"
```

### Cifrado de texto
Para ejecutar la herramienta de **Cifrado de texto**, se tomarán en cuenta los parámetros:

* --language - lenguaje a utilizar para el crackeo, opciones: {en, es}
* --metodo-cifrado - método de cifrado a utilizar, opciones: {cesar, transposicion}
* --function - la función a realizar, opciones: {encode, decode, crack}
* --key - clave para la codificación o decodificación, default = 5
* --path - path del .txt

Por ejemplo:

```
$ ./3vil_tool.py -m encoding --language "en" --metodo-cifrado "cesar" --function "crack" --path "path del archivo"
```

### Escaneo de puertos
Para ejecutar la herramienta de **Escaneo de puertos**, se tomarán en cuenta los parámetros:

* --host - host objetivo 
* --port - puerto objetivo [Opcional]

Por ejemplo: 

```
$ ./3vil_tool.py -m scan --host "127.0.0.1" --port "22,20,89,130"
```

### Obtención de claves HASH
Para ejecutar la herramienta de **Obtención de claves HASH**, se tomarán en cuenta los parámetros:

* --hash - tipo de clave HASH a utilizar, opciones: {md5, sha256, sha512}
* --cifrado - path de algun archivo existente en el sistema

**Nota:** Obligatoriamente en archivo _txt_ debe llamarse **directions.txt**

Por ejemplo: 

```
$ ./3vil_tool.py -m hash --hash "md5" --cifrado directions.txt
```

### Consulta a la API de GitHub
Para ejecutar la herramienta de **Consulta a la API de GitHub**, se tomarán en cuenta los parámetros:

* --user - usuario objetivo en GitHub
* --repository - nombre del repositorio del usuario objetivo
* --token - token 0Auth de GitHub generada por tu usuario

Por ejemplo: 

```
$ ./3vil_tool.py -m api --user "ShadowFaxumu" --repository "mirepouwu" --token "12g2hhasba61u16bdha"
```


## Autores

_Con la contribución de:_

* [Gómez Rodriguez Paulina](https://github.com/ShadowFaxumu) -Cifrado de texto- y -Envio de correos-
* [Sayago Leiba Angel Saul](https://github.com/S4yago) -Consulta a la API de GITHUB- , -Menús- y -Script Principal-
* [Rodriguez Rangel Deivi](https://github.com/LicYoshio) -Obtención de claves HASH-
* [Gaytan Montelongo Jesus Gerardo](https://github.com/Moncho96) -Escaneo de puertos-
