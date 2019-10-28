from sys import stdin



def testen():

    print("hallo")



if __name__ == "__main__":
    array = list()
    print("Array mit ganzen Zahlen füllen: ")
    empty = False
    while empty != True:
        i = input()
        if not i.strip():
            empty = True
            break
        array.append(i)

    print(array)


