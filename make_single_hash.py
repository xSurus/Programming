import hashlib


def make_a_hash():
    # the word that the user wants to hash
    words_to_hash = input("Give me a word to hash: ").split()
    # can hash many words, not just one
    for i in words_to_hash:
        hashed_wrd = str(hashlib.md5(''.join(i).encode()).hexdigest())
        print(hashed_wrd)


make_a_hash()
