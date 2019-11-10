


def count_sort(liste, k):
    c = [0] * (k+1)
    print(c)

    for i in range(1, len(liste)):
        c[liste[i]] = c[liste[i]] +1

    print(c)
    for i in range(1, k):
        c[i] = c[i] + c[i-1]
    print(c)

    array = [0] * len(liste)
    print(array)
    for i in range(len(liste)-1, 1, -1):
        array[c[liste[i]]] = liste[i]
        c[liste[i]] = c[liste[i]] - 1
    return array



if __name__ == "__main__":

    arr = [5,3,9,9,3,2,6,2,7]
    k = 10
    #count_sort(arr, k)
    newArr = count_sort(arr, k)
    for i in range(len(newArr)):
        if newArr[i] == 0: newArr.remove(i)
    print(newArr)