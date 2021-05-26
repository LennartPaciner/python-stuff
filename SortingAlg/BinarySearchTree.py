import random
#Klasse die den Wurzelknoten verwaltet
class Baum:
    def __init__(self, val):
        self.links = None
        self.rechts = None
        self.data = val


#Klasse die auf Knoten des Baumes zugreift
class Knoten:
    #Erstelle Wurzelknoten
    def erstelleRoot(self, data):
        return Baum(data)

    #Füge neuen Knoten in den Baum ein. Erstelle Wurzel, falls es noch keine gibt.
    def insert(self, knoten, data):
        if knoten is None:
            return self.erstelleRoot(data)
        if data < knoten.data:
            knoten.links = self.insert(knoten.links, data)
        elif data == knoten.data:
            return
        else:
            knoten.rechts = self.insert(knoten.rechts, data)
        return knoten

    #Gebe Baum komplett aus
    #Evtl noch versuchen schöner auszugeben, falls zeit
    def printBaum(self, knoten):
        if knoten.links:
            self.printBaum(knoten.links)
        print(knoten.data)
        if knoten.rechts:
            self.printBaum(knoten.rechts)

    def inorder(self, wurzel):
        if wurzel is None:
            return
        else:
            self.inorder(wurzel.links)
            print(wurzel.data)
            self.inorder(wurzel.rechts)

    def preorder(self, wurzel):
        if wurzel is None:
            return
        else:
            print(wurzel.data)
            self.preorder(wurzel.links)
            self.preorder(wurzel.rechts)

    def postorder(self, wurzel):
        if wurzel is None:
            return
        else:
            self.postorder(wurzel.links)
            self.postorder(wurzel.rechts)
            print(wurzel.data)

    def getTiefe(self, wurzel):
        if wurzel is None:
            return 0
        if wurzel.links:
            tiefe_links = self.getTiefe(wurzel.links)
        else:
            tiefe_links = 0
        if wurzel.rechts:
            tiefe_rechts = self.getTiefe(wurzel.rechts)
        else:
            tiefe_rechts = 0
        return max(tiefe_links, tiefe_rechts) + 1

if __name__ == "__main__":
    wurzel = None
    baum = Knoten()
    wurzel = baum.insert(wurzel, 5)
    baum.insert(wurzel, 3)
    baum.insert(wurzel, 1)
    baum.insert(wurzel, 4)
    baum.insert(wurzel, 8)
    baum.insert(wurzel, 9)
    print("Baum vom Blatt")
    baum.printBaum(wurzel)
    print("----------------")
    print("Inorder")
    baum.inorder(wurzel)
    print("----------------")
    print("Preorder")
    baum.preorder(wurzel)
    print("----------------")
    print("Postorder")
    baum.postorder(wurzel)
    print("----------------")
    print("Tiefe vom Baum ist: " ,end="")
    print(baum.getTiefe(wurzel))
    print("----------------")
    print("Ab hier für 1d) das print ganz unten auskommentieren. Aufgabe nicht komplett verstanden.")
    print("Analyse: Wert steigt schnell an bis zu einem bestimmten Wert und geht dann auch wieder zurück, da mit neuen Werten der Baum sich rebalancieren kann. Langfristig wächst der Wert")
    print("")
    root = None
    baum2 = Knoten()
    mittelwert = 0
    k = random.randrange(2, 7)
    n = 10**k

    for i in range(1, n):
        tiefe = 0
        for j in range(10):
            zahlen = random.sample(range(1, n + 1), n)
            root = baum2.insert(root, zahlen[0])
            for x in range(1, i):
                baum2.insert(root, zahlen[x])
            tiefe += baum2.getTiefe(root)
        mittelwert = tiefe / 10
        #hier entkommentieren für 1d
        #print(mittelwert)







