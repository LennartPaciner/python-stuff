class Radixsort:


    def findMax(self, a):
        max = 0
        for i in range(0, len(a)):
            if max < a[i]: max = a[i]
        return max


    #mittels stabilem counting sort
    def sortExponent(self, a, k, exp):
        b = [0] * (k)
        output = [0] * (len(a)+1)

        for i in range(0, len(a)):
            bIndex = (a[i] // exp) % k
            b[bIndex]+=1

        for i in range(1, k):
            b[i] += b[i - 1]

        i = len(a)-1
        while i >= 0:
            bIndex = (a[i] // exp) % k
            output[b[bIndex] - 1] = a[i]
            b[bIndex] -= 1
            i-=1

        for i in range(0, len(a)):
            a[i] = output[i]



    def radix_sort(self, a):

        m = self.findMax(a)
        exp = 1
        while m // exp > 0:
            self.sortExponent(a, 10, exp)
            exp *= 10
            #print(a)

if __name__ == "__main__":
    obj = Radixsort()
    arr = [88, 3, 9, 12, 3, 2, 6, 2, 15]
    #arr.insert(0,0)
    print(arr)
    #obj.radix_sort(arr)
    obj.radix_sort(arr)
    print(arr)