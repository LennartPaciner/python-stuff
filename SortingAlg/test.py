import math




def summe1(a,k):
    summe = 0
    i = len(a) - k
    for j in range(1, i + (k-1)):
        summe+=a[j]
    summe //= k
    return summe

def summe2(a, k):
    summe = 0
    i = len(a) - k
    for k in range(2, i + k):
        summe+=a[k]
    summe //= k
    return summe

def sortListwithK(a, k):

    if summe1(a,k) <= summe2(a,k):
        return a
    else:
        for i in range(len(a)):
            #123, 234 zb für 3-k sortiert
            #1,2  2,1 für 2-k sortiert




if __name__ == "__main__":
    arr = [88, 3, 9, 12, 3, 2, 6, 2, 15]

