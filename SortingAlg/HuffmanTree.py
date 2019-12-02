'''
noch für manuelle eingabe erweiterbar machen
'''
import heapq, string
count = ""
count2 = ""

#Gibt für jeden unique Charakter aus der Eingabe die Bitfolge der Kodierung aus und merkt sich die Länge rekursiv.
def huffman(root, s):
    global count, count2

    if root[2] is None and root[3] is None and root[1] in string.printable:
        print(root[1], end="")
        print(":" + s)
        count = count + s
        count2 = count2 + root[0] * s
        return

    huffman(root[2], s + '0')
    huffman(root[3], s + '1')



if __name__ == "__main__":
    A = "Bananensaft"
    print("Eingabestring = " + A)

    #Bekomme Liste der unique Charaktere aus der Eingabe
    a = list(set(A))

    # besitzt häufigkeiten der unique chars aus Liste a die am anfang erzeugt wird aus der Eingabe an der jeweiligen Stelle
    arr = [0] * len(a)

    #Da noch keine großen Eingaben erwartet werden ist die Laufzeit egal
    for i in range(len(a)):
        for j in range(len(A)):
            if a[i] == A[j]: arr[i] += 1

    #Lege Heap an für die Min-Queue
    heap = []

    #Für jeden unique Charakter lege Tupel in Baumstruktur an und fülle ihn mit Häufigkeit in Eingabe und füge ihn zum Heap hinzu
    for i in range(len(a)):
        knoten = (arr[i], a[i], None, None)

        heapq.heappush(heap, knoten)

    #Erstelle root Knoten/Tupel
    root = ()

    #Entnehme die 2 Minimum Tupel/Knoten aus dem Min-Heap und erstelle neues Tupel aus ihren Häufigkeiten als neuen Vater und füge diesen in den Heap hinzu
    while len(heap) > 1:
        u = heapq.heappop(heap)
        v = heapq.heappop(heap)
        f = (u[0] + v[0], '-', u, v)
        root = f
        heapq.heappush(heap, f)

    #Printe die Kodierung der einzelnen Charaktere
    huffman(root, "")

    #Länge der Kodierung
    print("Länge der unique Kodierung = " + str(len(count)))
    print("Länge der gesamten Kodierung = " + str(len(count2)))


