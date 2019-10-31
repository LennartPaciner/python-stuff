kombination = 0
"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
"""
def getK(liste, zahl):
    global kombination
    for i in range (0, len(liste)):
        #kein index out of bounce für j, da i niemals den letzten wert der liste annimmt, da dieser vorher schon kombiniert wurde
        for j in range(1+i , len(liste)):
            if liste[i] + liste[j] == zahl:
                kombination = liste[i] + liste[j]
                return True

    return False

if __name__ == "__main__":
    #Beispielarray
    array = [10, 15, 4, 7, 1]
    print("{}{}{}{}".format("Irgendeine Kombination für k möglich? ", getK(array, 8)," : " , kombination))