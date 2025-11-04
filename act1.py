def act1():
    list1 = []
    for x in range(5):
        print("Introduce un objeto")
        list1.append(input())
    list2 = list1.copy()
    list2.reverse()
    print(list2)

