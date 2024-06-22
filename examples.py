# Crear una agenda telefonica
# donde pidan datos como nombre o telefono
# y los guarden en una estructura
# recomiendo usar diccionarios, listas y funciones
# debe tener un menu de tres opciones

import csv

with open('bookingvenues.csv', 'r') as archivo:
    reader = csv.DictReader(archivo)
    print(reader)
    for fila in reader:
        print(f"El Lugar {fila['Address']} tiene una capacidad de {fila['Capacity']}")
