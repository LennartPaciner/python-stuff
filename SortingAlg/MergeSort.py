fehlstand = 0
"""
Sortiert übergebenes Array von Ganzzahlen in O(n * log(n)) Zeit rekursiv
"""
def mergesort(liste):
        links = list()
        rechts = list()
        if len(liste) <= 1: return liste

        mitte = len(liste)//2
        for i in range(0, mitte):
            links.append(liste[i])
        for i in range(0, mitte):
            rechts.append(liste[mitte+i])

        if len(liste) % 2 != 0:
            rechts.append(liste[mitte+mitte])

        links = mergesort(links)
        rechts = mergesort(rechts)
        return merge(links, rechts)

"""
Bekommt zwei Arrays übergeben und schreibt Elemente ihrer Größe nach in ein neues Array
"""
def merge(listeL, listeR):
    neueListe = list()
    indexL = 0
    indexR = 0
    fehlstand = 0

    while indexL < len(listeL) and indexR < len(listeR):
        if listeL[indexL] < listeR[indexR]:
            neueListe.append(listeL[indexL])
            indexL += 1
        else:
            neueListe.append(listeR[indexR])
            indexR += 1
            fehlstand += 1
            countFehlstand(fehlstand)
    while indexL < len(listeL):
        neueListe.append(listeL[indexL])
        indexL += 1
    while indexR < len(listeR):
        neueListe.append(listeR[indexR])
        indexR += 1

    return neueListe

def countFehlstand(zahl):
    global fehlstand
    fehlstand = fehlstand + zahl



if __name__ == "__main__":
    array = list()
    print("Array mit ganzen Zahlen füllen. Leere Eingabe zum Beenden.")
    empty = False

    # Überprüft Inputs des Benutzers bis eine leere Eingabe kommt.
    while empty != True:
        i = input()
        if not i.strip():
            empty = True
            break
        array.append(i)

    # Caste Liste mit Strings in Int um
    array = list(map(int, array))

    print(mergesort(array))
    print("{}{}".format("Fehlstände: ", fehlstand) )

