import math
count1 = 0
count2 = 1

def summe1(a,k):
    global count1
    summe = 0

    for j in range(count1, k+count1):
        summe+=a[j]
    summe //= k

    count1+=1
    #print(summe)
    return summe

def summe2(a, k):
    global count2
    summe = 0

    for j in range(count2, k+count2):
        summe+=a[j]
    summe //= k

    count2+=1
    return summe

def getSumme(a, k):
    #print(summe1(a, k))
    #print(summe2(a, k))
    
    if summe1(a,k) <= summe2(a,k):
        return True
    return False

def sortListwithK(a, k):
    for i in range(len(a)):
        if getSumme(a, k):
            return a

    for i in range(1, len(a)-k):
        #123, 234 zb für 3-k sortiert
        #1,2  2,1 für 2-k sortiert
        if getSumme(a, k) == True: return a

        if[a[i] > a[i+1]]:
            zwischen = a[i]
            a[i] = a[i+1]
            a[i+1] = zwischen


        print(i, end=" ")
        print(a)
    #return  sortListwithK(a, k)
    return 0


if __name__ == "__main__":
    arr = [2,1,3,4,5,6,7,8,10,9]
    k = 2
    #getSumme(arr,2)
    print(sortListwithK(arr, 2))
    #sortListwithK(arr, 9)
    #print(getSumme(arr, 2))

