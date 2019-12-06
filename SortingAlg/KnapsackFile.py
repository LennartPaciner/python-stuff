def rucksack(gewichte, profite, maximal):
    opt = [[0 for x in range(maximal + 1)] for x in range(len(profite) + 1)]

    for i in range(len(profite) + 1):
        for j in range(maximal + 1):
            if i == 0 or j == 0:
                opt[i][j] = 0
            elif gewichte[i-1] <= j:
                opt[i][j] = max(profite[i-1] + opt[i-1][j - gewichte[i-1]], opt[i-1][j])
            else:
                opt[i][j] = opt[i-1][j]

    return opt[len(profite)][maximal]


if __name__ == "__main__":
    with open('Eingabe_Rucksack.txt', 'r') as myfile1:
        eingabe = myfile1.read().splitlines()
    print("Gewichtsschranke eingeben: ", end="")
    M = input()
    schranke = [0] * int(M)
    for i in range(int(M)):
        schranke[i] = i + 1
    A = ' '.join(eingabe)
    A = A.replace(" ", "")
    gewichte = []
    profite = []
    for i in range(1, int(A[0]) * 2, 2):
        gewichte.append(int(A[i]))
    for i in range(2, (int(A[0]) * 2) + 1, 2):
        profite.append(int(A[i]))

    print("Ausgabe:")
    for i in range(len(schranke)):
        print(rucksack(gewichte, profite, schranke[i]), end=" ")
    #print(rucksack(gewichte, profite, schranke[2]))





