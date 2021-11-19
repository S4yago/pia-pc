# PIA - 3V1L TOOL

**_3V1L TOOL_** es un programa exclusivo de linux que contiene herramientas para realizar tareas con relación a ciberseguridad.
Entre ellas están:
* [Envio de correos](https://github.com/S4yago/pia-pc/blob/main/envio_de_correos.py)
* [Consulta a la API de GitHub](https://github.com/S4yago/pia-pc/blob/main/api_github.py)
* [Escaneo de puertos](https://github.com/S4yago/pia-pc/blob/main/port_scanning.py)
* [Obtención de claves HASH](https://github.com/S4yago/pia-pc/blob/main/claves_hash.py)
* [Cifrado de texto](https://github.com/S4yago/pia-pc/blob/main/cifrado_de_texto.py)


## Contenido

- [PIA - 3V1L TOOL](#pia---3v1l-tool)
  - [Contenido](#contenido)
  - [Comenzando 🚀](#comenzando-)
    - [Pre-requisitos](#pre-requisitos)
  - [Funcionamiento general](#funcionamiento-general)
    - [Web Scraping](#web-scraping)
    - [Cifrado de texto](#cifrado-de-texto)
    - [Obtención de claves HASH](#obtención-de-claves-hash)
    - [Consulta a la API de Shodan](#consulta-a-la-api-de-shodan)
    - [Escaneo de puertos](#escaneo-de-puertos)
  - [Ejecución](#ejecución)
    - [Ejecución por menú](#ejecución-por-menú)
    - [Ejecución por paso de argumentos](#ejecución-por-paso-de-argumentos)
    - [Web Scraping](#web-scraping-1)
    - [Cifrado de texto](#cifrado-de-texto-1)
    - [Escaneo de puertos](#escaneo-de-puertos-1)
    - [Obtención de claves HASH](#obtención-de-claves-hash-1)
    - [Consulta a la API de Shodan](#consulta-a-la-api-de-shodan-1)
  - [Autores](#autores)

## Comenzando 🚀

### Pre-requisitos

Para poder tener una ejecución exitosa del script se necesitaran instalar ciertos modulos
que no vengan por default en python. Para ello ejecutará el siguiente comando

```
$ pip install -r requirements.txt
```
## Funcionamiento general

### Web Scraping

La herramienta de web scraping que toma como parametro el nombre de alguna pagina de noticas disponible (_larepublica_,_diario_). Con el fin de analizar las noticias del día y crear archivos _.txt_ con el titulo, un resumen y el body. Esta herramienta no ocupa **Beautiful Soup**, para hacer el análisis del HTML. En cambio utiliza **XPath**.

### Cifrado de texto

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

### Obtención de claves HASH

La herramienta de obtención de claves HASH utiliza 3 métodos de encriptado HASH (md5, sha256 y sha512) para sacar la clave única de algún archivo dado
por el usuario.
El script trabaja con 1 archivo dado por el usuario:

* Path absoluto del archivo

Por ejemplo:

```
/home/[user]/PIACiberseguridad
```

### Consulta a la API de Shodan

La herramienta acepta como argumento de entrada un _.txt_ con una o varias **IP Adress**. Las analiza y crea un _.txt_ con la información encontrada.

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
se encontraron abiertos, tiene la opción de especificar que puertos quieres que se escaneen si así lo deseas.

## Ejecución

El script principal es **3v1l_tool.py**, que tiene 2 métodos:
* Con paso de argumentos
* Por menú

### Ejecución por menú

Si no se pasa ningun parametro al momento de la ejecución del script, automáticamente adoptará una interfaz para que se pueda llevar a cabo la ejecución
utilizando un menú interactivo

Por ejemplo:
```
$ ./3vil_tool.py
```

### Ejecución por paso de argumentos

Para poder diferenciar entre alguna herramienta y otra se tomará en cuenta el parámetro **_'-m'_**
Donde las opciones son:
* _scraping_ - para hacer web scraping
* _encoding_ - para cifrado de texto
* _hash_ - para obtención de claves HASH
* _scan_ - para escanear puertos
* _api_ - para consulta a la API de Shodan

Por ejemplo:

```
$ ./3vil_tool.py -m scraping
```

### Web Scraping
Para ejecutar la herramienta de **Web Scraping**, se tomarán en cuenta los parámetros:

* --news - nombre del portal de noticias

Por ejemplo:

```
$ ./3vil_tool.py -m scraping --news {larepublica,diario}
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

### Consulta a la API de Shodan
Para ejecutar la herramienta de **Consulta a la API de Shodan**, se tomarán en cuenta los parámetros:

* --api-key - API que te proporciona Shodan
* --shodan-path - path del archivo con las IP's a analizar

Por ejemplo:

```
$ ./3vil_tool.py -m api --api-key 8Mpsy8tdQBzdGedUlHmY0dUxKZgxqujp --shodan-path ip_address.txt
```

## Autores

_Con la contribución de:_

* [Gómez Rodriguez Paulina](https://github.com/ShadowFaxumu) -Cifrado de texto- -Web Scraping-
* [Sayago Leiba Angel Saul](https://github.com/S4yago) -Consulta a la API de Shodan- -Menús- y -Script Principal-
* [Rodriguez Rangel Deivi](https://github.com/LicYoshio) -Obtención de claves HASH-
* [Gaytan Montelongo Jesus Gerardo](https://github.com/Moncho96) -Escaneo de puertos-
