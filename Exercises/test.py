import random as rd
import math

p = 2147483659


def sec_hash(a,b,k):
    global p
    m = 2**20
    sec_hash = ((a * k + b) % p) % m
    return sec_hash


def primary_hash(k):
    global p
    a = 1
    b = 1
    m = 2**20
    p_hash = ((a * k + b) % p) % m
    return p_hash


def perfect_hashing(schluessel):
    global p
    new_dict = {new_list: [] for new_list in range(0, 2**20)}

    for i in range(0, 2**20):
        result = primary_hash(schluessel[i])
        if schluessel[i] in new_dict.values() or new_dict[result] != []:
            frei = False
            while frei == False:
                a = rd.randint(0, p)
                b = rd.randint(0, p)
                result = sec_hash(a, b, schluessel[i])

                if new_dict[result] == []:

                    new_dict[result] = schluessel[i]
                    frei = True
        else:
            new_dict[result] = schluessel[i]

    return new_dict




if __name__ == "__main__":
    #print(2**20)
    #2^20 = 1048576 = unser anzahl n und unser m

    liste = [rd.randint(0, 2**10)] * 2**20
    print(perfect_hashing(liste))













