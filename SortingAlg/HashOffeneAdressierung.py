'''
Fill a Hash Table size m with set of given Keys for Linear Probing, Quadratic Probing
and Double Hashing for h'(k) = k and h''(k) = 1 + (k mod (m-1))
'''

"""
Hashtabelle von 1 bis m+1. i startet im ersten Iterationsschritt bei 1.
"""
def linearProbing(schluessel, m):
    hashTabelle = {}
    for i in range(1, m+1):
        hashTabelle[i] = 0
    for k in range(len(schluessel)):
        i = 1
        result = ((schluessel[k] + i) % m) + 1
        if hashTabelle[result] != 0:
            frei = False
            while frei == False:
                i+=1
                result = ((schluessel[k] + i) % m) + 1
                if hashTabelle[result] == 0:
                    hashTabelle[result] = schluessel[k]
                    frei = True
        else:
            hashTabelle[result] = schluessel[k]
    return hashTabelle

"""
Hashtabelle von 1 bis m+1. i startet im ersten Iterationsschritt bei 1. Konstanten 1 und 3
"""
def quadraticProbing(schluessel, m):
    hashTabelle = {}
    c1 = 1
    c2 = 3
    for i in range(1, m + 1):
        hashTabelle[i] = 0
    for k in range(len(schluessel)):
        i = 1
        result = ((schluessel[k] + i*c1 + (i**2)*c2) % m) + 1
        if hashTabelle[result] != 0:
            frei = False
            while frei == False:
                i += 1
                result = ((schluessel[k] + i*c1 + (i**2)*c2) % m) + 1
                if hashTabelle[result] == 0:
                    hashTabelle[result] = schluessel[k]
                    frei = True
        else:
            hashTabelle[result] = schluessel[k]
    return hashTabelle

def doubleHashing(schluessel, m):
    hashTabelle = {}
    for i in range(1, m + 1):
        hashTabelle[i] = 0
    for k in range(len(schluessel)):
        i = 1
        result = ((schluessel[k] + i * (1 + (schluessel[k] % (m-1)))) % m) + 1
        if hashTabelle[result] != 0:
            frei = False
            while frei == False:
                i += 1
                result = ((schluessel[k] + i * (1+ (schluessel[k] % (m-1)))) % m) + 1
                if hashTabelle[result] == 0:
                    hashTabelle[result] = schluessel[k]
                    frei = True
        else:
            hashTabelle[result] = schluessel[k]
    return hashTabelle



if __name__ == "__main__":
    testliste = [10, 22, 31, 4, 15, 28, 17, 88, 59]

    print(linearProbing(testliste, 11))
    print(quadraticProbing(testliste, 11))
    print(doubleHashing(testliste, 11))
