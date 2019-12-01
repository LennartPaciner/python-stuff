import heapq, string
count = ""

def huffman(root, s):
    global count

    if root[2] is None and root[3] is None and root[1] == '-':
        return
    if root[2] is None and root[3] is None and root[1] != '-':
        print(root[1], end="")
        print(":" + s)
        count = count + s
        return

    huffman(root[2], s + '0')
    huffman(root[3], s + '1')



if __name__ == "__main__":
    with open('Martin_Luther_Uebersetzung_1545.txt', 'r') as myfile1:
        eingabe = myfile1.read()
    with open('The_Holy_Bible_King_James_Version_1611.txt', 'r') as myfile2:
        eingabe2 = myfile2.read()
    A = ' '.join(eingabe)
    A2 = ' '.join(eingabe2)

    a = list(set(A))
    a2 = list(set(A2))
    b = ''.join(a)
    b2 = ''.join(a2)
    arr = [0] * len(a)
    arr2 = [0] * len(a2)
    for i in A:
        if i in b:
            stelle = b.find(i)
        arr[stelle] += 1
    for i in A2:
        if i in b2:
            stelle2 = b2.find(i)
        arr2[stelle2] += 1

    for i in range(len(a)):
        if a[i] == 'Ö': a[i] = 'Oe'
        elif a[i] == 'Ü': a[i] = 'Ue'
        elif a[i] == 'Ä': a[i] = 'Ae'
        elif a[i] == 'ü': a[i] = 'ue'
        elif a[i] == 'ö': a[i] = 'oe'
        elif a[i] == 'ä': a[i] = 'ae'

    heap = []
    heap2 = []
    for i in range(len(a)):
        knoten = (arr[i], a[i], None, None)
        heapq.heappush(heap, knoten)

    for i in range(len(a2)):
        knoten2 = (arr2[i], a2[i], None, None)
        heapq.heappush(heap2, knoten2)
    root = ()
    root2 = ()

    while len(heap) > 1:
        u = heapq.heappop(heap)
        v = heapq.heappop(heap)
        f = (u[0] + v[0], '-', u, v)
        root = f
        heapq.heappush(heap, f)

    while len(heap2) > 1:
        x = heapq.heappop(heap2)
        y = heapq.heappop(heap2)
        z = (x[0] + y[0], '-', x, y)
        root2 = z
        heapq.heappush(heap2, z)

    walfisch = False
    count2 = 0

    if walfisch == False:
        huffman(root, "")
        count2 = count
        print("Länge der Kodierung Luther = " + str(len(count)))
        count = ""
    huffman(root2, "")
    print("Länge der Kodierung King James = " + str(len(count)))
    print("Es werden ", end="")
    print(len(count2) - len(count), end="")
    print(" Bits weniger für King James benötigt. Eng > De")




