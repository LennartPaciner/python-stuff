"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
"""
def getK(liste, zahl):

    for i in range (0, len(liste)):
        for j in range(0 , len(liste)):
            if liste[i] + liste[j] == zahl:
                print(liste[i] + liste[j])
                return True

    return False
"""
noch nicht fertig, evtl in einem durchrutsch lösen t.t
"""
def onepass(liste, zahl):
    test = 0
    for i in range(0, len(liste)):
        test += liste[i]

    return False


if __name__ == "__main__":
    #Beispielarray
    array = [10, 15, 3, 7]
    print(getK(array, 25))