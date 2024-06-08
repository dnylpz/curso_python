# Clase 2


## Usando modulos externos

```python
import re
import datetime
from math import ceil

now = datetime.datetime.now()
re.match(r"^https:\/\/.*\.?[a-zA-z0-9]*\.[a-z]{2,3}","https://google.com") # True
ceil(19.6) # 20
```

## Trabajando con tiempo

```python
from datetime import datetime

ahora  = datetime.now()
print(ahora) # 2024-06-01 21:23:15.595635
print(ahora.isoformat())  # '2024-06-01T21:23:15.595635'
ahora.strftime("%d/%m/%Y") # 01/23/2024
ahora.strftime("%A") # Saturday
nuevo_ahora = datetime.now()
print(nuevo_ahora-ahora) # 0:08:56.375358

from datetime import date

cumple = date(1994,2,16) 
print(cumple) # 1994-2-16

from datetime import timedelta
diez_dias = timedelta(days=10)
print(cumple+diez_dias) #1994-02-26

from datetime import time
una_hora = time(20,5)
print(una_hora) # 20:05:00
``` 


## instalando herramientas externas

Para instalar herramientas externas y librerias utilizaremos
un ambiente virtual o virtualenv, esto evita conflictos entre versiones
de una herramienta en diferentes proyectos.

```powershell
# Ojo! esto se corre en la terminal como admin, no en python
set-executionpolicy RemoteSigned
mkdir .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

```bash
# Mac y Linux
mkdir .venv
python -m venv .venv
source ./.venv/bin/activate
```

para instalar las herramientas se usa pip

```
pip install requests
```

## Regex y validaciones de entrada

```python
import re
url = 'https://www.google.com/'

number = '12345'
if re.match('\d+', number):
    the_number = int(number)


if re.match(r'((https|http)\:)?\/\/[a-zA-Z0-9\.]*\.?[a-zA-Z0-9]+\.?[a-zA-Z0-9]{2,3}\/?[\?\_\/\w\d\=\&]*', url):
    request.get(url)


```

```python
import pyinputplus as pyip

number =  pyip.inputNum(prompt="enter a number")

response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category']) #mezclando regex con pyip

```



