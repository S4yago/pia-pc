# PIA - 3V1L TOOL

**_3V1L TOOL_** es un programa exclusivo de linux que contiene herramientas para realizar tareas con relaci贸n a ciberseguridad.
Entre ellas est谩n:
* [Web Scraping](https://github.com/S4yago/pia-pc/blob/main/modulos/web_scraping.py)
* [Consulta a la API de Shodan](https://github.com/S4yago/pia-pc/blob/main/modulos/shodan.py)
* [Escaneo de puertos](https://github.com/S4yago/pia-pc/blob/main/modulos/port_scanning.py)
* [Obtenci贸n de claves HASH](https://github.com/S4yago/pia-pc/blob/main/modulos/claves_hash.py)
* [Cifrado de texto](https://github.com/S4yago/pia-pc/blob/main/modulos/cifrado_de_texto.py)


## Contenido

- [PIA - 3V1L TOOL](#pia---3v1l-tool)
  - [Contenido](#contenido)
  - [Comenzando 馃殌](#comenzando-)
    - [Pre-requisitos](#pre-requisitos)
  - [Funcionamiento general](#funcionamiento-general)
    - [Web Scraping](#web-scraping)
    - [Cifrado de texto](#cifrado-de-texto)
    - [Obtenci贸n de claves HASH](#obtenci贸n-de-claves-hash)
    - [Consulta a la API de Shodan](#consulta-a-la-api-de-shodan)
    - [Escaneo de puertos](#escaneo-de-puertos)
  - [Ejecuci贸n](#ejecuci贸n)
    - [Ejecuci贸n por men煤](#ejecuci贸n-por-men煤)
    - [Ejecuci贸n por paso de argumentos](#ejecuci贸n-por-paso-de-argumentos)
    - [Web Scraping](#web-scraping-1)
    - [Cifrado de texto](#cifrado-de-texto-1)
    - [Escaneo de puertos](#escaneo-de-puertos-1)
    - [Obtenci贸n de claves HASH](#obtenci贸n-de-claves-hash-1)
    - [Consulta a la API de Shodan](#consulta-a-la-api-de-shodan-1)
  - [Autores](#autores)

## Comenzando 馃殌

### Pre-requisitos

Para poder tener una ejecuci贸n exitosa del script se necesitaran instalar ciertos modulos
que no vengan por default en python. Para ello ejecutar谩 el siguiente comando

```
$ pip install -r requirements.txt
```
## Funcionamiento general

### Web Scraping

La herramienta de web scraping que toma como parametro el nombre de alguna pagina de noticas disponible (_larepublica_,_diario_). Con el fin de analizar las noticias del d铆a y crear archivos _.txt_ con el titulo, un resumen y el body. Esta herramienta no ocupa **Beautiful Soup**, para hacer el an谩lisis del HTML. En cambio utiliza **XPath**.

### Cifrado de texto

La herramienta de cifrado de texto utiliza dos m茅todos (Cesar y Transposici贸n) para codificar, decodificar y crackear un texto dado en formato .txt, tiene
la funci贸n, para que en tiempo de ejecuci贸n, se devuelva el texto ya codificado con el m茅todo y llaves indicadas.
Para la funci贸n de crackeo tambi茅n se cuenta con la posibilidad de indicar el idioma en el que se desea crackear un mensaje donde se podr谩 escoger entre
Ingl茅s y Espa帽ol (en, es)
El script trabaja con 1 archivo dado por el usuario:

* Path absoluto del txt

Por ejemplo:
```
/home/[user]/archivo.txt
```

### Obtenci贸n de claves HASH

La herramienta de obtenci贸n de claves HASH utiliza 3 m茅todos de encriptado HASH (md5, sha256 y sha512) para sacar la clave 煤nica de alg煤n archivo dado
por el usuario.
El script trabaja con 1 archivo dado por el usuario:

* Path absoluto del archivo

Por ejemplo:

```
/home/[user]/PIACiberseguridad
```

### Consulta a la API de Shodan

La herramienta acepta como argumento de entrada un _.txt_ con una o varias **IP Adress**. Las analiza y crea un _.txt_ con la informaci贸n encontrada.

**Ejemplo de txt (entrada):**
```
164.128.164.55
164.128.164.32
164.128.164.118
...
...
...
```

### Escaneo de puertos

La herramienta de escaneo de puerto realiza un escaneo a varios puertos por default de algun host local dado por el usuario y te devuelve los puertos que
se encontraron abiertos, tiene la opci贸n de especificar que puertos quieres que se escaneen si as铆 lo deseas.

## Ejecuci贸n

El script principal es **3v1l_tool.py**, que tiene 2 m茅todos:
* Con paso de argumentos
* Por men煤

### Ejecuci贸n por men煤

Si no se pasa ningun parametro al momento de la ejecuci贸n del script, autom谩ticamente adoptar谩 una interfaz para que se pueda llevar a cabo la ejecuci贸n
utilizando un men煤 interactivo

Por ejemplo:
```
$ ./3vil_tool.py
```

### Ejecuci贸n por paso de argumentos

Para poder diferenciar entre alguna herramienta y otra se tomar谩 en cuenta el par谩metro **_'-m'_**
Donde las opciones son:
* _scraping_ - para hacer web scraping
* _encoding_ - para cifrado de texto
* _hash_ - para obtenci贸n de claves HASH
* _scan_ - para escanear puertos
* _api_ - para consulta a la API de Shodan

Por ejemplo:

```
$ ./3vil_tool.py -m scraping
```

### Web Scraping
Para ejecutar la herramienta de **Web Scraping**, se tomar谩n en cuenta los par谩metros:

* --news - nombre del portal de noticias

Por ejemplo:

```
$ ./3vil_tool.py -m scraping --news {larepublica,diario}
```

### Cifrado de texto
Para ejecutar la herramienta de **Cifrado de texto**, se tomar谩n en cuenta los par谩metros:

* --language - lenguaje a utilizar para el crackeo, opciones: {en, es}
* --metodo-cifrado - m茅todo de cifrado a utilizar, opciones: {cesar, transposicion}
* --function - la funci贸n a realizar, opciones: {encode, decode, crack}
* --key - clave para la codificaci贸n o decodificaci贸n, default = 5
* --path - path del .txt

Por ejemplo:

```
$ ./3vil_tool.py -m encoding --language "en" --metodo-cifrado "cesar" --function "crack" --path "path del archivo"
```

### Escaneo de puertos
Para ejecutar la herramienta de **Escaneo de puertos**, se tomar谩n en cuenta los par谩metros:

* --host - host objetivo
* --port - puerto objetivo [Opcional]

Por ejemplo:

```
$ ./3vil_tool.py -m scan --host "127.0.0.1" --port "22,20,89,130"
```

### Obtenci贸n de claves HASH
Para ejecutar la herramienta de **Obtenci贸n de claves HASH**, se tomar谩n en cuenta los par谩metros:

* --hash - tipo de clave HASH a utilizar, opciones: {md5, sha256, sha512}
* --cifrado - path de algun archivo existente en el sistema

**Nota:** Obligatoriamente en archivo _txt_ debe llamarse **directions.txt**

Por ejemplo:

```
$ ./3vil_tool.py -m hash --hash "md5" --cifrado directions.txt
```

### Consulta a la API de Shodan
Para ejecutar la herramienta de **Consulta a la API de Shodan**, se tomar谩n en cuenta los par谩metros:

* --api-key - API que te proporciona Shodan
* --shodan-path - path del archivo con las IP's a analizar

Por ejemplo:

```
$ ./3vil_tool.py -m api --api-key 8Mpsy8tdQBzdGedUlHmY0dUxKZgxqujp --shodan-path ip_address.txt
```

## Autores

_Con la contribuci贸n de:_

* [G贸mez Rodriguez Paulina](https://github.com/ShadowFaxumu) -Cifrado de texto- -Web Scraping-
* [Sayago Leiba Angel Saul](https://github.com/S4yago) -Consulta a la API de Shodan- -Men煤s- y -Script Principal-
* [Rodriguez Rangel Deivi](https://github.com/LicYoshio) -Obtenci贸n de claves HASH-
* [Gaytan Montelongo Jesus Gerardo](https://github.com/Moncho96) -Escaneo de puertos-
