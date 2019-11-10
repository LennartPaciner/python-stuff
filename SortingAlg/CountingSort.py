


def count_sort(liste, k):
    c = [0] * (k+1)

    # die erste stelle kommt 0 mal vor, da sonst später error
    for i in range(1, len(liste)):
        c[liste[i]] = c[liste[i]] +1

    for i in range(1, k):
        c[i] = c[i] + c[i-1]


    array = [0] * len(liste)

    for i in range(len(liste)-1, 0, -1):
        array[c[liste[i]]] = liste[i]
        c[liste[i]] = c[liste[i]] - 1

    return array



if __name__ == "__main__":
    arr2 = list()
    #Braucht an erster Stelle die 0, ansonsten fehlt erstes Element im Ergebnis.
    arr = [0,9,3,9,9,3,2,6,2,7]
    k = 10
    #count_sort(arr, k)
    newArr = count_sort(arr, k)
    newArr.remove(0)
    print(newArr)