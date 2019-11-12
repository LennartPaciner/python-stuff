

def count_sort(liste, k):
    c = [0] * (k)

    #wegen liste+1 wird eine extra 0 am ende des ergebnisses übergeben, aber notwendig sonst index fehler.
    #letzte stelle der ergebnisliste einfach manuell entfernen bevor man mit dem ergebnis weiterarbeitet
    array = [0] * (len(liste))


    for i in range(0, len(liste)):
        c[liste[i]] += 1

    for i in range(1, k):
        c[i] += c[i-1]

    i = len(liste)-1
    while i >= 0:
        array[c[liste[i]] - 1] = liste[i]
        c[liste[i]] -= 1
        i -= 1
    print(array)
    return array



if __name__ == "__main__":

    arr = [9,3,9,9,3,2,6,2,7]

    k = 10
    #print(arr)
    #Entferne 0 an erster Stelle um Ausgangsarray = Länge Eingabearray zu haben
    newArr = count_sort(arr, k)

    print("Ergebnis:", end = " ")
    print(newArr)