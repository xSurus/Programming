import hashlib
import random

file = "words_alpha.txt"
used_hashes = []


def make_a_hash(dictionary):
    f = open("list_of_hashes.txt", "a")
    with open(dictionary, "r") as file:
        lines = file.readlines()
        # creates a list with the words from the dictionary
        list_dict = [y.strip() for y in lines]
        while len(used_hashes) < 5040:
            hashed_wrd = str(hashlib.md5(''.join(list_dict[random.randint(1, 370098)]).encode()).hexdigest())
            if hashed_wrd not in used_hashes:
                used_hashes.append(hashed_wrd)
                f.write(hashed_wrd + "\n")
    f.close()
make_a_hash(file)