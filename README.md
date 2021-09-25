# PIA

## Integrantes
1. Yo merengues
2. Shadow
3. Deivi
4. Moncho

## Guía de código para el PIA

### Generales
* Toda la lógica estará encapsulada en funciones.
* En cada script habrá una función principal que llamara a las demás.
* Las funciones no puedes hacer más de una tarea.
* Se debe escribir código que sea auto-explicativo. Pero si es estrictamente necesario,
  se podrá agregar comentarios.
* Todas las funcionalidades disponibles deben estar documentadas.
* Todas las funcionalidades deben funcionar como parámetros en shell o como menú.

### Sintaxis
* Se utilizara la guía de estilos de [PEP8][pep8].

### Flujo del script
* Las funciones se agregaran siguiendo el flujo normal.

**Ejemplo:**
```python
### Nombre del script: web_scraping.py
#!/usr/bin/env python3

from pyhunter import PyHunter
from openpyxl import Workbook
import getpass

def pedir_datos():
    print("Script para buscar información")
    api_key = getpass.getpass("Ingresa tu API key: ")
    hunter = PyHunter(apikey)
    organizacion = input("Dominio a investigar: ")

    return organizacion


def busqueda_de_informacion(organizacion):
    resultado = hunter.domain_search(
        company=organizacion, limit=1, emails_type='personal')
    return resultado


def guardar_informacion(datosEncontrados):
    headers = []
    values = []

    for clave, valor in datosEncontrados.items():
        if isinstance(valor, list):
            dic = valor[0]
            guardar_informacion(dic)
        else:
            headers.append(clave)
            values.append(valor)
    return headers, values


def crear_excel(headers, values, organizacion):
    libro = Workbook()
    hoja = libro.create_sheet(organizacion)
    libro.save("Hunter" + organizacion + ".xlsx")

    for i in range(1, 25):
        hoja.cell(i, 1, headers[i-1])
        hoja.cell(i, 2, values[i-1])

    libro.save("Hunter" + organizacion + ".xlsx")


def web_scraping():
    organizacion = pedir_datos() #Composición de funciones
    datos = busqueda_de_informacion(organizacion)
    if datos is None:
        exit()
    else:
        crear_excel(guardar_informacion(datos), organizacion)

```

## Factores a evaluar y recursos
* Manejo de errores **[GLOBAL]** 
    1. [Documentación Oficial][errores1]
    2. [Video de Youtube][errores2]
    * Uso de logging **[AL FINAL]**
* Uso de `argparse` **[GLOBAL]**
    1. [Documentación Oficial][argparse1]
    2. [Documentación externa][argparse2]
    2. [Video de Youtube][argparse3]
    2. [Video de Youtube 2][argparse4]
* Uso de `socket` **[ESPECIFICO]**
    1. [Documentación Oficial][socket1]
    2. [Documentación externa][socket2]
* Consultar a una API **[ESPECIFICO]**
* Usar modulo no nativo que no se haya visto en clase y que
  sirva para ciberseguridad **[ESPECIFICO]**
* Generar un reporte **[AL FINAL]**
* Se deben invocar archivos **BASH** desde python **[ESPECIFICO]**
* Se debe crear un scrip principal **[ESPECIFICO]**
* Crear los HASH de todos los archivos **[GLOBAL]**

**NOTA:** _Todas las funcionalidades del script deben funcionar en linux y windows_

## Git y GitHub
Vamos a utilizar [Conventional Commits][commits] para darle sentido a nuestro commits.
Eso sí, no vamos a seguirla al pie de la letra.

### Conventional commits estructura

```bash
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```
* fix: Se arreglo un _bug_
* feat: Se agrego una nueva característica
* docs: Se cambio la documentación
* perf: Un cambio de código que mejora el rendimiento
* refactor: Un cambio de código que no corrige un error ni agrega una característica
* style: cambios que no afectan el significado del código (espacios en blanco, formato, punto y coma que faltan, etc.)

**Ejemplo:**
```bash
feat: crea un archivo .xlsx con los datos

utilzando los datos guardados por la funcion X

se agregó una nueva función que utliza los datos

para crear un libro de excel.
```
[pep8]:https://www.python.org/dev/peps/pep-0008/
[errores1]:https://docs.python.org/es/3/tutorial/errors.html
[errores2]:https://www.youtube.com/watch?v=IYB2q4sgzvw
[argparse1]:https://docs.python.org/es/3.8/howto/argparse.html
[argparse2]:https://rico-schmidt.name/pymotw-3/argparse/#:~:text=argparse%20es%20una%20herramienta%20completa,maneja%20argumentos%20opcionales%20y%20requeridos.
[argparse3]:https://www.youtube.com/watch?v=SbQmQ4T4E8E
[argparse4]:https://www.youtube.com/watch?v=tirLko5urBo&t=228s
[socket1]:https://docs.python.org/3.9/howto/sockets.html
[socket2]:https://programmerclick.com/article/546769496/
[commits]:https://www.conventionalcommits.org/en/v1.0.0/
