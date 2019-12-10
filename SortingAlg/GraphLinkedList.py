class Graph_LL:

    def __init__(self, knotenanzahl):
        self.value = None
        self.linkedliste = [[]for x in range(knotenanzahl)]

    def printList(self):
        for i in range(len(self.linkedliste)):
            for j in range(len(self.linkedliste[i])):
                    print(end="")
                    print(self.linkedliste[i][j], end="")
                    if j is not (len(self.linkedliste[i]) - 1):
                        print(" -> ", end="")
            print("")

    def newList(self, newdata):
        for i in range(len(newdata)):
            neu = newdata[i]
            self.value = neu
            self.linkedliste[i] = [neu]


    def insertEnd(self, newdata, stelle):
        for i in range(len(newdata)):
            neu = newdata[i]
            if self.linkedliste[stelle] is None:
                self.linkedliste[stelle] = [neu]
                return
            self.linkedliste[stelle].append(neu)

    def insertKnoten(self, newdata, stelle, knotenstelle):
        neu = newdata
        self.linkedliste[stelle].insert(knotenstelle, neu)

    def deleteKnoten(self, newdata, stelle):
        for i in self.linkedliste[stelle]:
            if i == newdata:
                self.linkedliste[stelle].remove(newdata)

    def dijkstra(self, anfang):
        distanz = [99999999] * len(self.linkedliste)
        distanz[anfang] = 0
        nochzusuchen = [False] * len(self.linkedliste)

        for i in range(len(self.linkedliste)):
            min_knoten = self.minDistanz(distanz, nochzusuchen)
            print(min_knoten)
            nochzusuchen[min_knoten] = True

            for j in range(len(self.linkedliste)):
                if self.linkedliste[min_knoten][j] > 0 and nochzusuchen[j] == False and distanz[j] > distanz[min_knoten] + self.linkedliste[min_knoten][j]:
                    distanz[j] = distanz[min_knoten] + self.linkedliste[min_knoten][j]
            print(distanz)
        self.printDistanz(distanz)

    def printDistanz(self, distanz):
        for i in range(len(self.linkedliste)):
            print(distanz[i], end=" ")


    def minDistanz(self, distanz, zusuchen):
        min = 999999999
        for i in range(len(self.linkedliste)):
            #print(zusuchen)
            if distanz[i] < min and zusuchen[i] == False:
                min = distanz[i]
                min_index = i
        return min_index

if __name__ == "__main__":
    '''geeks beispiel eingabe
    knoten = [0, 4, 0 ,0, 0, 0, 0, 8, 0]
    g = Graph_LL(len(knoten))
    g.newList(knoten)
    g.insertEnd([4, 0, 0, 0, 0, 0, 8, 0], 0)
    g.insertEnd([0, 8, 0, 0, 0, 0, 11, 0], 1)
    g.insertEnd([8, 0, 7, 0, 4, 0, 0, 2], 2)
    g.insertEnd([0, 7, 0, 9, 14, 0, 0, 0], 3)
    g.insertEnd([0, 0, 9, 0, 10, 0, 0, 0], 4)
    g.insertEnd([0, 4, 14, 10, 0, 2, 0, 0], 5)
    g.insertEnd([0, 0, 0, 0, 2, 0, 1, 6], 6)
    g.insertEnd([11, 0, 0, 0, 0, 1, 0, 7], 7)
    g.insertEnd([0, 2, 0, 0, 0, 6, 7, 0], 8)
    g.printList()
    g.dijkstra(0)'''
    knoten = ['A', 'B', 'C', 'D', 'E']
    g = Graph_LL(len(knoten))
    #Dijkstra funktioniert. Halbwegs verstanden aber vllt nochmal vertiefen und versuchen selber nachzuprogrammieren!_!
    g.insertEnd([0, 100, 0, 50, 0], 0)
    g.insertEnd([0, 0, 100, 0, 250], 1)
    g.insertEnd([0, 0, 0, 0, 50], 2)
    g.insertEnd([0, 100, 0, 0, 250], 3)
    g.insertEnd([0, 0, 0, 0, 0], 4)
    print("Kürzeste Distanz von Knoten A ausgehend")
    for i in range(len(knoten)):
        print(knoten[i], end=" ")
    print("")
    g.dijkstra(0)



