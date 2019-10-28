#globale Variable anlegen
fehlstand = 0
"""
Sortiert ein Array mit ganzen Zahlen mittels Insertion-Sort in O(n^2)
"""
def insertionSort(list):
    #global setzen
    global fehlstand

    for i in range(0, len(list)):
        wert = list[i]
        j = i
        while (j > 0) and (array[j-1] > wert):
            array[j] = array[j-1]
            fehlstand = fehlstand + 1
            j-=1
        array[j] = wert

    print("{}{}".format("Fehlstände: ",fehlstand) )
    return array



if __name__ == "__main__":
    array = list()
    print("Array mit ganzen Zahlen füllen. Leere Eingabe zum Beenden.")
    empty = False

    #Überprüft Inputs des Benutzers bis eine leere Eingabe kommt.
    while empty != True:
        i = input()
        if not i.strip():
            empty = True
            break
        array.append(i)

    #Caste Liste mit Strings in Int um
    array = list(map(int, array))

    insertionSort(array)
    print(array)


