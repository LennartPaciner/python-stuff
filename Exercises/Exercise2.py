"""
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.
"""

"""
Mittels Division gelöst.
"""
def produkt(liste):
    neueListe = list()
    ergebnis = 1
    #alle werte multiplizieren
    for i in range(0, len(liste)):
        ergebnis *= liste[i]
    #durch die jeweilige Stelle teilen um i auszuschließen
    for i in range(0, len(liste)):
        neueListe.append(ergebnis // liste[i])

    return neueListe

"""
Bonus: What if you can't use division?
"""
def ohneDiv(liste):
    neueListe = list()
    ergebnis = 1

    for i in range(0, len(liste)):
        #in der zweiten Schleife die eigentliche Rechnung durchführen
        for j in range(0 , len(liste)):
            #Stelle i darf nicht bei sich selbst multipliziert werden
            if j != i:
                ergebnis *= liste[j]
            else:
                continue
        neueListe.append(ergebnis)
        #ergebnis wieder zurücksetzen damit jede Stelle neu ausgerechnet werden kann
        ergebnis = 1

    return neueListe

if __name__ == "__main__":
    #beispielarray
    array = [1,2,3,4,5]

    print(produkt(array))
    print(ohneDiv(array))