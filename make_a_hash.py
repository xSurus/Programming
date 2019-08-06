import hashlib

def make_a_hash():
    x = input("Give me a word to hash: ").split()
    print(x)
    for i in x:
        hashed_wrd = str(hashlib.md5(''.join(i).encode()).hexdigest())
        print(hashed_wrd)

make_a_hash()