"""
Huffman-Tree Variate für zwei Text Dateien als Eingabe mittels Tupeln umgesetzt
"""
import heapq
count = ""
count2= ""

#Gebe rekursiv die Kodierung der unique Charaktere aus und merke die Länge davon einzeln und insgesamt.
def huffman(root, s):
    global count, count2

    if root[2] is None and root[3] is None and root[1] == '-':
        return
    if root[2] is None and root[3] is None and root[1] != '-':
        print(root[1], end="")
        print(":" + s)
        count = count + s
        count2 = count2 + root[0] * s
        return

    huffman(root[2], s + '0')
    huffman(root[3], s + '1')



if __name__ == "__main__":
    #Lese Textfile 1 ein
    with open('Martin_Luther_Uebersetzung_1545.txt', 'r') as myfile1:
        eingabe = myfile1.read()
    #Lese Textfile 2 ein
    with open('The_Holy_Bible_King_James_Version_1611.txt', 'r') as myfile2:
        eingabe2 = myfile2.read()

    #Schreibe Eingabe als String und nicht als Liste
    A = ' '.join(eingabe)
    A2 = ' '.join(eingabe2)

    #Merke die unique Charaktere aus den Texten in einer Liste
    a = list(set(A))
    a2 = list(set(A2))

    #Schreibe die Liste der unique Charaktere als String um
    b = ''.join(a)
    b2 = ''.join(a2)

    #Besitzt Häufigkeiten der unique Charaktere aus der Eingabe an der richtigen Stelle
    arr = [0] * len(a)
    arr2 = [0] * len(a2)

    #Da Texte größer als normale Eingaben seien können, nicht in O(n^2) möglich die Häufigkeit zu zählen. Stattdessen in annäherend linearer Zeit zu lösen.
    for i in A:
        if i in b:
            stelle = b.find(i)
        arr[stelle] += 1
    for i in A2:
        if i in b2:
            stelle2 = b2.find(i)
        arr2[stelle2] += 1

    #Umbennenung der Umlaute aus einem deutschen Text falls erwünscht, hier eigentlich nicht notwendig.
    for i in range(len(a)):
        if a[i] == 'Ö': a[i] = 'Oe'
        elif a[i] == 'Ü': a[i] = 'Ue'
        elif a[i] == 'Ä': a[i] = 'Ae'
        elif a[i] == 'ü': a[i] = 'ue'
        elif a[i] == 'ö': a[i] = 'oe'
        elif a[i] == 'ä': a[i] = 'ae'

    #Anlegen der Heaps
    heap = []
    heap2 = []

    #Erstelle Tupel/Knoten mit Häufigkeit und füge ihn für jeden unique Charakter in Heap hinzu
    for i in range(len(a)):
        knoten = (arr[i], a[i], None, None)
        heapq.heappush(heap, knoten)
    for i in range(len(a2)):
        knoten2 = (arr2[i], a2[i], None, None)
        heapq.heappush(heap2, knoten2)

    #Erstelle root Knoten/Tupel
    root = ()
    root2 = ()

    #Ermittle die zwei minimalen Tupel und erstelle neuen mit deren Häufigkeit als neuen Vater und füge ihn zu Heap hinzu
    while len(heap) > 1:
        u = heapq.heappop(heap)
        v = heapq.heappop(heap)
        f = (u[0] + v[0], '-', u, v)
        root = f
        heapq.heappush(heap, f)
    while len(heap2) > 1:
        x = heapq.heappop(heap2)
        y = heapq.heappop(heap2)
        z = (x[0] + y[0], '-', x, y)
        root2 = z
        heapq.heappush(heap2, z)

    #Walfisch ist falsch
    walfisch = False
    countx = 0

    #Rufe zuerst die Print Funktion für den ersten Text auf um Länge der Kodierung zu merken
    if walfisch == False:
        huffman(root, "")
        countx = count2
        print("Länge der unique Kodierung Luther = " + str(len(count)))
        print("Länge der gesamten Kodierung Luther = " + str(len(count2)))
        count = ""
        count2 = ""

    #Rufe zweiten Text auf
    huffman(root2, "")
    print("Länge der unique Kodierung King James = " + str(len(count)))
    print("Länge der gesamten Kodierung King James = " + str(len(count2)))

    print("Es werden ", end="")
    print(len(countx) - len(count2), end="")
    print(" Bits weniger für King James benötigt. Eng < De")




