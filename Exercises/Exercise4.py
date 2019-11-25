"""
Kurzer Greedy Algorithmus um vorgegebene Menge mit minimalen vorhandenen Möglichkeiten zu erreichen.
"""

def ronnie(x, scheiben):
    gewicht = 0
    i = 0
    anz_scheiben = [0] * len(scheiben)
    while gewicht < x:
        #Nehme immer noch größtmögliche Zahl aus Array um Ziel zu erreichen.
        if gewicht + scheiben[i] <= x:
            anz_scheiben[i]+=1
            gewicht+=scheiben[i]
        else:
            i+=1
    return anz_scheiben


if __name__ == "__main__":
    #Testwerte
    scheiben = [25, 10, 5 ,1]
    x = 318
    print(ronnie(x, scheiben))