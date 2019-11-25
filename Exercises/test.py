import random

def hashPrimary(k):
    a = 1
    b = 0
    tabelle = {}
    index = ((a * k + b) % 2147483659) % 1048576



def hashSecondary(index):
    return index

def statPerfectHash():
    a = []
    for i in range(0, 2**20):
        a.append(random.randint(0, 2**31 - 1))
    for i in range(0, 2**20):
        hashPrimary(a[i])
    #print(index)



if __name__ == "__main__":
    #print(2**20)
    #2^20 = 1048576 = unser anzahl n und unser m
    #statPerfectHash()
    tabelle = {}
    for i in range(10):
        if [4] in tabelle.values():
            print(i)
            wert = tabelle[str(i)].
            tabelle[str(i)] = [wert, 99]
            #tabelle[str(4)].append(4)
        tabelle[str(i)] = [i % 5]
    print(tabelle)













