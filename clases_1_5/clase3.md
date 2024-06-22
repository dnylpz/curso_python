# Clase 3 

## Manejo de archivos

### manejadores/punteros o referencias.

Abrimos un archivo en modo escritura, no si no existe se crea

```python3
# el nombre de un archivo debe ser un nombre valido para el sistema de archivos y una ubicacion valida
manejador = open('mi_archivo.txt', 'w')
manejador.write("Hola Amigos!\n")
manejador.close()
```

Vemos en la terminal como se creo el archivo
```bash
ls | grep mi_archivo
mi_archivo.txt
```

Abrimos el archivo en modo lectura y verificamos su contenido

```python3
manejador = open('mi_archivo', 'w')
print(manejador.read())
# imprime 'hola amigos!' 
```


podemos abrir cualquier tipo de archivos, pero algunos debemos leerlos en binario

```python3
manejador = open('kitty.jpg', 'rb')
datos = r"""
while (byte := manejador.read(1)):
    datos += byte
manejador.close()
datos
# imprime??? \x8a\x04 2 characteres hex por byte

import base64
print(base64.encodebytes(datos)[0:10])
# b'/9j/4AAQSk' valor en base64
```

### bloques with!

```python3
with open('mi_archivo.txt', 'r') as f:
    contenido = f.readlines()
print(contenido) # contenido persiste pero el archivo se cierra fuera del bloque

with open('mi_archivo.txt', 'w') as f:
    f.write("Mi archivo!")

# el archivo se cierra en automatico
```

### Organizando archivos


Para poder interactuar mejor con el sistema operativo y el sistema de archivos usamos los modulos
OS, y pathlib, shutil nos da algunas utilidades de un shell que entre otras cosas
nos permite, mover, renombrar, copiar y eliminar archivos y carpetas.

```python3
# TODO: COMPLETAR EJEMPLOS

import shutil, os
from pathlib import Path
```

### Formatos!

para los archivos con formatos especificos se utilizan librerias auxiliares que facilitan el manejo de archivos de ciertos tipos
en el caso de csv y json las librerias se incluyen con python

```python3
import csv

with open('ejemplo.csv', 'r') as f:
    reader = csv.DictReader(f) # dict reader para archivos CSV con la primera fila como cabecera
    for row in reader:
        print(f"{row['usuario']}: {row['telefono']}") # Daniel: 6667341342
```

```python3
import json
with open('ejemplo.json', 'r') as f:
    data = json.load(f)

print(f"{data[0]['usuario']}: {data[0]['telefono']}") # Daniel: 6667341342

```

para imagenes existe pillow

```bash
python3 -m pip install --upgrade Pillow
```

```python3
from PIL import Image, ImageEnhance
im =  Image.open('kitty.jpg')
im.show()
mejorada = ImageEnhance.Contrast(im)
resultado = enh.enhance(1.3)
resultado.save() #Error?
archivo = open('kitty_contraste.jpg', 'wb') # escritura binaria!
resultado.save(archivo)
```

