# Clase 1
## El interprete interactivo de python

```python
x = 5 # asignaciones
x + 10 # operaciones
print(x) # ejecucion de funciones
x = "Hola mundo!" # mas asignaciones
x = len(x) + 10 # expresiones compuestas
def saludo():  # inicio de bloques (una funcion salvaje aparece)
    print("Hola mundo")
```

## Tipos de datos

```python
True, False
"Cadenas"
101234
123.43
9j + 5
None
```

## Operaciones y operadores

```python
10 + 5              # 15               | Suma 
15 - 10             # 5                | Resta
"Hola" + ", Mundo!" # "Hola, Mundo!"   | Concatenacion
20 * 4              # 80               | Multiplicacion
80 / 20             # 4.0              | Division con decimal
5 %  2              # 1                | Modulo o Sobrante
5 // 2              # 2                | Division con redondo abajo
2 ** 8              # 256              | Potencia
```

## Comparadores

```python
5 == 5              # Verdadero | igualdad
2+2 != 5            # Verdadero | no igualdad
```

# Operaciones booleanas

```python
nombre = "Daniel"
5 == 5 and "D" in "Daniel" # Verdadero | Multiplicacion Booleana
5 == 4 and "D" in "Daniel" # Verdadero | Suma Booleana
not False                  # Verdadero | negacion booleana
```


## Cadenas

```python
"Hola mundo!"
"Hola mundo!"[3] # Accesando con indices
x = "Hola Mundo"
x[1:4] # Accesando con rebanadas
nombre = "Daniel"
x = f"Hola {nombre}" # Formateando cadenas
print("Hola\nTodos!") # Cadenas escapadas
'Combinando "algunas" comillas ' # con comillas simples y dobles
x = "Hola %s" % nombre # Otro tipo de formato
r"aqui\no habra salto de linea" # Cadenas en crudo
```

## Operaciones de cadenas

```python
x = "Hola, Mundo!"
x[1,5]               # 'ola,', los indices empiezan en 0
x.split(",")         # ["Hola", "Mundo!"]
len(x)               # 12
x.swapCase()         # "hOLA, mUNDO!"
x.upper()            # "HOLA, MUNDO!"
x.lower()            # "hola, mundo!"
x.startswith("Hola") # True
x.ljust(15)          #"Hola, Mundo!  " Agrega 2 espacios en blanco
# Para ver mas https://www.w3schools.com/python/python_ref_string.asp
```
## Ejercicio 1

```python
# De los numeros del 1 al 10 imprime True si son pares o False si no lo son
# Recuerda los conceptos de expresiones, operaciones y valores booleanos
# la operacion Modulo puede ser muy util para resolver esto.
____(1  _ 2 __ ? )
____(2  _ 2 __ ? )
____(3  _ 2 __ ? )
____(4  _ 2 __ ? )
____(5  _ 2 __ ? )
____(6  _ 2 __ ? )
____(7  _ 2 __ ? )
____(8  _ 2 __ ? )
____(9  _ 2 __ ? )
____(10 _ 2 __ ? )
```


# Tipos de datos estructurados

```python
x = [1,2,3,4]
x[0] = 10 # [10,2,3,4]
x = (1,2,3,4)
x[0] = 5 # !Error
x = {1,4,5,6} 
x[0] # !Error
x.pop() # 1
mis_datos = {
    "nombre": "daniel",
    "edad": 10
}
mis_datos["nombre"]         # "daniel"
mis_datos["telefono"]       # Error
mis_datos.get("telefono")   # None
```

# Organizando nuestros datos

```python
tabla = [
    ["Nombre","Edad"]
    ["Daniel", 30],
    ["Juan", 25],
    ["Miguel", 28]
    ]
tabla[1][1] # 30
mis_datos = {
    "Nombres": ["Daniel", "Juan", "Miguel"],
    "Edades": [30, 25, 28]
}
mis_datos["Edades"][2]
ajedrez = [
    ["a", "b", "c", "d", "e", "f", "g", "h"],
    [1,2,3,4,5,6,7,8]
]
peon_blanco2 = ajedrez=[0][1]

pila = []
pila.append(tabla[1][1])
pila.append(tabla[2][1])
pila.pop() # Juan
coordenadas = [
    [1154213,-1235123],
    [5243534,-512435123]
]
```

# Ejercicio 2

```python
# Crear una agenda telefonica
# donde pidan datos como nombre o telefono
# y los guarden en una estructura
# recomiendo usar diccionarios, listas y funciones
# debe tener un menu de tres opcieones

opcion = ""
while opcion != "3":
    print("Bievenido a tu agenda, presiona la opcion deseada")
    print("1 agregar datos")
    print("2 ver datos")
    print("3 salir")
    opcion = input("tu seleccion: ")
```