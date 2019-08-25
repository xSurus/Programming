import itertools
import multiprocessing
import argparse
import hashlib
import time

# Defining the start and end of the time function so that
# it is easier to call it to print out the time that passed
def time_start():
    global time_start
    time_start = time.time()


def time_end():
    time_end = time.time()
    time_total = time_end - time_start
    print(time_total)

# First funciton that takes a set of hashes as an input and
# searches for the clearword in a dictionary that is pre-defined
def HashCrackerDictionary(hashes):
    # importing the dictionary
    time_start()
    filename_cleartext = "words_alpha.txt"
    hashed_words = []
    with open(filename_cleartext, "r") as file:
        lines = file.readlines()
        # creates a list with the words from the dictionary where each
        # word is a single item in the list
        lines = [x.strip() for x in lines]
        for line in lines:
            # encodes each line into bit and hashse it through 
            hashed_dict = str(hashlib.md5(line.encode()).hexdigest())
            # statement to check for correct password
            for hash in hashes:
                if hash == hashed_dict and line not in hashed_words:
                    hashed_words.append(line)
                    # if the hash that was given as an input corresponds to the
                    # hashed word in the list then print it
                    print(hash, "is the corresponding hash to", line)
                    hashes.remove(hash)
            # ends the loop for efficiency sake when all hashes have been found
            if len(hashes) == 0:
                break
    print(hashed_words)
    time_end()


def HashCrackerPermutations(hashes):
    time_start()
    global alphabet
    # defines the input for the permutations
    alphabet = ["a", "e", "c", "d"]
    hashed_words = []
    # if known how long the password is change it to its length + 1
    for r in range(1, len(alphabet) + 1):
        for s in itertools.product(alphabet, repeat=r):
            # hashes each created permutations using the md5 hash
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
    time_end()

# to choose which function the user wants to use
# Options: permutations - multiprocessing/single thread; dictionary - multir
if __name__ == "__main__":
    pool = multiprocessing.Pool(4)
    parser = argparse.ArgumentParser(description='Crack a Hash')
    parser.add_argument("type", help="Choose with which method you'd like to \
        crack a hash")
    args = parser.parse_args()
    if args.type == "d,m":
        hashes = [input("Please input the hashed words: ").split()]
        pool.map(HashCrackerDictionary, hashes)
    elif args.type == "d,s":
        hashes = input("Please input the hashed words: ").split()
        HashCrackerDictionary(hashes)
    elif args.type == "p,m":
        hashes = [input("Please input the hashed words: ").split()]
        pool.map(HashCrackerPermutations, hashes)
    elif args.type == "p,s":
        alphabet = input("Please input the amount of letter you'll use (The \
letters should have a space between each one): ").split()
        hashes = input("Please input the hashed words: ").split()
        HashCrackerPermutations(hashes)
