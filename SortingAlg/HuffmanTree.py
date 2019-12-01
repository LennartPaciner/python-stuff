import heapq, string
count = ""

def huffman(root, s):
    global count

    if root[2] is None and root[3] is None and root[1] in string.printable:
        print(root[1], end="")
        print(":" + s)
        count = count + s
        return

    huffman(root[2], s + '0')
    huffman(root[3], s + '1')



if __name__ == "__main__":
    A = "Bananensaft"
    print("Eingabestring = " + A)
    a = list(set(A))
    arr = [0] * len(a)  # besitzt häufigkeiten der unique chars aus liste a die am anfang erzeugt wird aus eingabestring
    for i in range(len(a)):
        for j in range(len(A)):
            if a[i] == A[j]: arr[i] += 1
    heap = []
    for i in range(len(a)):
        knoten = (arr[i], a[i], None, None)

        heapq.heappush(heap, knoten)

    root = ()

    while len(heap) > 1:
        u = heapq.heappop(heap)
        v = heapq.heappop(heap)
        f = (u[0] + v[0], '-', u, v)
        root = f
        heapq.heappush(heap, f)

    #Printe die Kodierung der einzelnen Charaktere
    huffman(root, "")
    #Länge der Kodierung
    print("Länge der Kodierung = " + str(len(count)))
    print(string.printable)


