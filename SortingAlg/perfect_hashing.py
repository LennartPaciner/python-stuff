import random

from collections import Counter, namedtuple


class HashFunction(namedtuple("HashFunction", 'a b p m')):
    def __call__(self, k):
        return (self.a * k + self.b) % self.p % self.m

    def __str__(self):
        return f"{self.a} * k + {self.b} mod {self.p} mod {self.m}"


def random_hash_function(p, m):
    a = random.randrange(1, p)
    b = random.randrange(0, p)
    return HashFunction(a, b, p, m)


# Bucketgröße muss quadratisch in Anzahl der Elemente gewählt werden    
def bucket_size(count):
    return count ** 2


def perfect_hash_functions(table_size, keys, p):

    primary_redraws = 0
    secondary_redraws = 0

    # optimale primäre Hashfunktion finden
    while ...:
        primary_hash = random_hash_function(p, table_size)
        # elements_in_bucket[k] = Anzahl Elemente un Bucket k
        elements_in_bucket = Counter(primary_hash(k) for k in keys)
        # bucket_sizes[k] = Zielgröße des Buckets k (muss nicht mit Anzahl der Elemente übereinstimmen)
        bucket_sizes = [bucket_size(elements_in_bucket[i]) for i in range(table_size)]
        # Neu ziehen, bis die Summe der Bucketgrößen <= 2n
        if sum(bucket_sizes) <= 2 * len(keys):
            break
        primary_redraws += 1

    # Elemente nach primärem Hashwert gruppieren
    buckets = [[] for _ in range(table_size)]
    for k in keys:
        buckets[primary_hash(k)].append(k)

    # optimale sekundäre Hashfunktionen bestimmen
    bucket_hash_functions = []
    for current_bucket, current_bucket_size in zip(buckets, bucket_sizes):
        while ...:
            secondary_hash = random_hash_function(p, current_bucket_size)
            # elements_at_index[i] = Anzahl Elemente am Index i
            elements_at_index = Counter(secondary_hash(k) for k in current_bucket)
            # ist elements_at_index[i] > 1 für ein i, gibt es eine Kollision
            collision = any(c > 1 for c in elements_at_index.values())
            if not collision:
                bucket_hash_functions.append(secondary_hash)
                break
            secondary_redraws += 1

    return primary_hash, bucket_sizes, bucket_hash_functions, (primary_redraws, secondary_redraws)


def main():
    # Vorgaben auf Blatt
    key_count = 1 << 20
    # zum Debuggen
    key_count = 1 << 3
    p = 2147483659
    table_size = key_count

    # keine Duplikate ziehen
    keys = random.sample(range((1 << 31) - 1), key_count)

    primary_hash, bucket_sizes, secondary_hashes, r = perfect_hash_functions(table_size, keys, p)

    print("Neuziehungen")
    print(*r)
    print("Primäre Hashfunktion")
    print(primary_hash)
    print("Sekundäre Hashfunktionen")
    print(*secondary_hashes, sep='\n')

    test(keys, bucket_sizes, primary_hash, secondary_hashes)


def test(keys, bucket_sizes, primary_hash, secondary_hashes):
    table = [[None] * bs for bs in bucket_sizes]
    for k in keys:
        bucket = primary_hash(k)
        pos = secondary_hashes[bucket](k)
        assert table[bucket][pos] is None
        table[bucket][pos] = k
    print(*table, sep='\n')


if __name__ == '__main__':
    main()
