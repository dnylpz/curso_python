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

```powershell
pip install requests
```