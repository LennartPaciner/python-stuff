'''class Knoten:
    def __init__(self, data = None):
        self.data = data
        self.nextval = None

    def __repr__(self):
        return str(self.data)
'''
#für dijksta alg testen ob diese datenstruktur das lösen kann
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


if __name__ == "__main__":
    knoten = ['a', 'b', 'c']
    g = Graph_LL(len(knoten))
    g.newList(knoten)
    g.insertEnd(['e', 'h', 'a'], 1)
    g.printList()




    '''
    g.insertEnd('d', 2)
    g.insertEnd(['e', 'f'], 0)
    g.insertKnoten('r', 0, 2)
    g.insertKnoten('u', 1, 1)
    g.insertKnoten('v', 1, 1)
    g.printList()
    print("-------")
    g.deleteKnoten('r', 0)
    g.deleteKnoten('b', 1)
    g.insertKnoten('x', 1, 0)
    g.insertKnoten('y', 1, 1)
    g.insertEnd(['h', 'g'], 1)
    g.printList()

    linkedliste = [[] for x in range(4)]

       linkedliste[0] = [0,1,2]
       linkedliste[1] = [1,2]
       linkedliste[2] = [2,3,4,5,6,7]
       linkedliste[3] = [1]
       #print(linkedliste)'''


