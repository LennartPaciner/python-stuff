"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Implement car and cdr.
"""


class TupelExercise:

    #Erstelle Tupel aus übergenen Argumenten
    def cons(self, a, b):
        return (a,b)

    #Gib erstes Element eines Tupels zurück
    def car(self, a):
        return a[0]

    #Gib zweites Element eines Tupels zurück
    def cdr(self, a):
        return a[1]




if __name__ == "__main__":
    t = TupelExercise()

    #Aufruf...
    paar = t.cons('x', 5.5)
    print(t.car(paar))
    print(t.cdr(paar))



