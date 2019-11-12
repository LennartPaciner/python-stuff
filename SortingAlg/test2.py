count1 = 0
count2 = 0
durchlauf = 1


def sortListwithK(a, k):
    global count1
    global count2
    global durchlauf

    paar1 = []
    paar2 = []

    for i in range(count1, k+count1):
        paar1.append(a[i])
        if i+1 >= len(a):
            break
        paar2.append(a[i + 1])
        count1 += 1

    for i in range(0, len(a)):
        if sum(paar1) <= sum(paar2):
            continue
        else:
            swap(paar1, paar2)
    if k + count1 < len(a):

        for i in range(count1, k + count1):
            a[i] = paar1[count2]
            a[i+1] = paar2[count2]
            count2+=1
    count2 = 0
    durchlauf+=1

    if durchlauf == len(a):
        return a
    return sortListwithK(a, k)

def swap(paar1, paar2):
    zwischen = []

    for i in range(len(paar1)):
        zwischen.append(paar1[i])
        if len(paar2) < len(paar1):
            break
        paar1[i] = paar2[i]
        paar2[i] = zwischen[i]

if __name__ == "__main__":
    arr = [2, 1, 3, 4, 5, 6, 7, 8, 10, 9]
    k = 2
    print(sortListwithK(arr, k))
