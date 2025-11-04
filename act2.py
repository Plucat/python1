import sys
from itertools import chain, count

# Yo creo la lista para mas comodidad.
list = ["Banana", "Apple", "Cherry", "Banana"]
for x in list:
    print(x)

def contar():
    print("Introduce una palabra de la lista")
    word = input()
    count = 0
    for x in list:
        if x == word:
            count += 1
    return(f"La cuenta es {count}")

def modificar():
    print("Introduce una palabra de la lista para modificar")
    word = input()
    print("A continuacion introduce la palabara que lo remplazara")
    rempla = input()
    for x in range(len(list)):
        if list[x] == word:
            list[x] = rempla

    print("A continuacion la lista nueva:")
    for i in list:
        print(i)

def eliminar():
    print("Introduce una palabra a eliminar")
    word = input()
    count = 0
    for x in list:
        if x == word:
            count += 1
    print(f"Se elimino {count} palabra(s)")
    for i in range(count):
        list.remove(word)

    print("A continuacion la lista nueva:")
    for i in list:
        print(i)

def mostrar():
    print("A continuacion la lista:")
    for i in list:
        print(i)

def terminar():
    sys.exit("Bye Bye")

while True:
    print("#########INICIO DE PROGRAMA#########\nEscoge una de las siguentes opciones:")
    print("1. Contar\n2. Modificar\n3. Eliminar\n4. Mostrar\n5. Salir")
    case = int(input())

    match case:
        case 1:
            contar()
        case 2:
            modificar()
        case 3:
            eliminar()
        case 4:
            mostrar()
        case 5:
            terminar()


