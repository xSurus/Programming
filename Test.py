import itertools
import hashlib
toBeHashed = "aec"
y = str(hashlib.md5(toBeHashed.encode()).hexdigest())
print(y)
alphabet = ["a", "e", "c", "d"]
hashed_words = []
hashes = [y]
# if known how long the password is change it to its length + 1
for r in range(1, len(alphabet) + 1):
    for s in itertools.product(alphabet, repeat=r):
        hashed_perm = str(hashlib.md5(''.join(s).encode()).hexdigest())
        for hash in hashes:
            if hash == hashed_perm and s not in\
                    hashed_words:
                hashed_words.append(s)
                print(hash, "is the corresponding hash to", ''.join(s))
                hashes.remove(hash)
        if len(hashes) == 0:
            break
    else:
        continue
    break