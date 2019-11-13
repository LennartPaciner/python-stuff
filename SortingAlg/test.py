count1 = 0
count2 = 0
count3 = 0
durchlauf = 1
b = [0] * 10
aufruf = True



#Funktioniert wenn k = 2 ist (zumindest für mein bsp array)
def sortListwithK(a, k):
    global count1
    global b
    global count3
    global aufruf
    okay = True
    global durchlauf

    paar1 = []
    paar2 = []
    if aufruf == True:
        b = a.copy()
    aufruf = False

    for i in range(count1, k+count1):
        paar1.append(a[i])

        if i+1 >= len(a):
            break

        paar2.append(a[i + 1])
        count1 += 1

    #for i in range(0, len(a)):
    if sum(paar1) <= sum(paar2):
        pass
    else:
        okay = False

    if k + count1 < len(a) and okay == False:
        for i in range(1):
            b[count1-k] = paar1[1]
            b[count1-1] = paar2[1]
            b[count1] = paar1[0]

    #seperaten fall für ende liste
    if k + count1 >= len(a) and okay == False:
        #in dieser version gerade nicht gebraucht
        pass

    durchlauf+=k

    if durchlauf >= len(a):
        return b

    return sortListwithK(a, k)

#alte hilfsfunktion
def swap(paar1, paar2):
    zwischen = []

    for i in range(len(paar1)):
        zwischen.append(paar1[i])
        if len(paar2) < len(paar1):
            break
        paar1[i] = paar2[i]
        paar2[i] = zwischen[i]


if __name__ == "__main__":
    arr = [2, 1, 7, 11, 5, 6, 7, 8, 10, 9]
    k = 2
    print(sortListwithK(arr, 2))
    #print(arr)


