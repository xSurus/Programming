import hashlib
import random
import itertools

alphabet = ["a", "e", "s", "m", "f", "l"]
made_perm = []
used_hashes = []
max_length = 7

def make_a_hash():
    f = open("list_of_hashes_perm_more.txt", "a")
    for length in range(1, max_length + 1):
        for s in itertools.product(alphabet, repeat=length):
            made_perm.append(s)
    while len(used_hashes) < 5020:
        hashed_wrd = str(hashlib.md5(''.join(made_perm[random.randint(1, 19510)]).encode()).hexdigest())
        if hashed_wrd not in used_hashes:
            used_hashes.append(hashed_wrd)
            f.write(hashed_wrd + "\n")
    f.close()

if __name__ == "__main__":
    make_a_hash()