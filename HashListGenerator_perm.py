import hashlib
import random
import itertools

used_hashes = []
alphabet = ["a", "e", "s", "m", "f", "l"]
made_perm = []

def make_a_hash():
    f = open("list_of_hashes_perm_more.txt", "a")
    for length in range(1, 7 + 1):
        for s in itertools.product(alphabet, repeat=length):
            made_perm.append(s)
    print(len(made_perm))
    while len(used_hashes) < 5020:
        hashed_wrd = str(hashlib.md5(''.join(made_perm[random.randint(1, 19510)]).encode()).hexdigest())
        if hashed_wrd not in used_hashes:
            used_hashes.append(hashed_wrd)
            f.write(hashed_wrd + "\n")
    f.close()


make_a_hash()