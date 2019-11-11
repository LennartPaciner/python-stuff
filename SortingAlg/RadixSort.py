class Radixsort:


    def findMax(self, a):
        max = 0
        for i in range(0, len(a)):
            if max < a[i]: max = a[i]
        return max



    #mittels stabilem counting sort
    def sortExponent(self, a, k, exp):
        global arraylen
        bIndex = 0
        b = [0] * k
        output = [0] * (len(a)+1)
        #print(b)
        #print(output)

        for i in range(0, len(a)):
            bIndex = (a[i] // exp) % k
            b[bIndex]+=1

        for i in range(1, k):
            b[i] += b[i - 1]

        for i in range(len(a)-1, 0, -1):
            bIndex = (a[i] // exp) % k
            output[b[bIndex]] = a[i]
            b[bIndex] = b[bIndex] - 1

        for i in range(0, len(a)):
            a[i] = output[i]


    def radix_sort(self, a):

        m = self.findMax(a)
        exp = 1
        while m // exp > 0:

            self.sortExponent(a, 10, exp)
            exp *= 10
            #print(a)

        return a

if __name__ == "__main__":
    obj = Radixsort()
    arr = [88, 3, 9, 12, 3, 2, 6, 2, 15]
    #arr.insert(0,0)

    #obj.radix_sort(arr)
    print (obj.radix_sort(arr))