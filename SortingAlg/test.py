import random
import string

def extractMin(A, a):
    arr = [0] * len(a)  #besitzt häufigkeiten der unique chars aus liste a die am anfang erzeugt wird aus eingabestring
    for i in range(len(a)):
        for j in range(len(A)):
            if a[i] == A[j]: arr[i]+=1

    m = min(arr)
    if len(a) == 1:
        return arr[0]

    for k in range(0, len(arr)):
        if arr[k] == m:
            result = arr[k]
            arr.remove(m)
            a.remove(a[k])
            break

    return result


def huffman(A, a):

    u = extractMin(A, a)
    v = extractMin(A, a)
    w = random.choice(string.ascii_lowercase)
    while w in A:
        w = random.choice(string.ascii_lowercase)
    neu = (w * (u+v)) + A
    A = neu
    a.append(w)

    if len(a)-1 == 1:
        return a[0]

    return huffman(A, a)



if __name__ == "__main__":
    A = "bananensaft"
    a = list(set(A))
    print(huffman(A,a))
    b = ['a']
    #print(len(b))

    #print(random.choice(string.ascii_lowercase))




