from itertools import chain, count

# def act1():
#     list1 = []
#     for x in range(5):
#         print("Introduce un objeto")
#         list1.append(input())
#     list2 = list1.copy()
#     list2.reverse()
#     print(list2)
#
# def act2():

# Yo creo la lista para mas comodidad.
list = ["Banana", "Apple", "Cherry","Banana"]

def contar():
    print("Introduce una palabra de la lista")
    word = input()
    count = 0
    for x in list:
        if word == x:
            count + 1
    print(f"La cuenta es {count}")

contar()

