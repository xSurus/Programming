import itertools
import multiprocessing
import argparse
import hashlib
import time


def time_start():
    global time_start
    time_start = time.time()


def time_end():
    time_end = time.time()
    time_total = time_end - time_start
    print(time_total)


def HashCrackerDictionary(hashes):
    # importing the dictionary
    time_start()
    filename_cleartext = "words_alpha.txt"
    hashed_words = []
    with open(filename_cleartext, "r") as file:
        lines = file.readlines()
        # creates a list with the words from the dictionary
        lines = [x.strip() for x in lines]
        for line in lines:
            # encode each line into bit so it can be hashed
            hashed_dict = str(hashlib.md5(line.encode()).hexdigest())
            # statement to check for correct password
            for hash in hashes:
                if hash == hashed_dict and line not in hashed_words:
                    hashed_words.append(line)
                    print(hash, "is the corresponding hash to", line)
                    hashes.remove(hash)    
            if len(hashes) == 0:
                break
    print(hashed_words)
    time_end()


def generate_permutations(alphabet, length):
    for s in itertools.product(alphabet, repeat=length):
        yield s


def HashCrackerPermutations(hashes):
    time_start()
    global alphabet
    alphabet = ["a", "e", "c", "d"]
    hashed_words = []
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
    print(hashed_words)
    time_end()


if __name__ == "__main__":
    pool = multiprocessing.Pool(4)
    parser = argparse.ArgumentParser(description='Crack a Hash')

    parser.add_argument("type", help="Choose with which method you'd like to \
        crack a hash", choices=["dictionary", "permutations"])

    parser.add_argument("--multiprocessing", type=int, default=1)

    args = parser.parse_args()
    if args.type == "dictionary":
        if args.multiprocessing == 1:
            HashCrackerDictionary()
        else:
            HashCrackerDictionaryParallel(args.multiprocessing)
    else:
        if args.multiprocessing == 1:
            HashCrackerPermutations()
        else:
            HashCrackerPermutations(args.multiprocessing)


