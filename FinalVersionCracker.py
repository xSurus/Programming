import itertools
import multiprocessing
import argparse
import hashlib
import time
import functools

def time_start():
    global time_start
    time_start = time.time()


def time_end():
    time_end = time.time()
    time_total = time_end - time_start
    print(time_total)


def cracker(hashes, word):
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    if hashed_word in hashes:
        print(hashed_word, "is the corresponding hash to", word)

def cracker_perm_wrapper(hashes, pw):
        password =''.join(pw)
        cracker(hashes, password)


def HashCrackerDictionaryHashFile(workers, dictionary, hashfile):
    # importing the dictionary
    # hashes = ["d2cbe65f53da8607e64173c1a83394fe"]
    pool = multiprocessing.Pool(workers)
    with open(dictionary, "r") as file:
        lines = file.readlines()
        # creates a list with the words from the dictionary
        list_dict = [y.strip() for y in lines]
        with open(hashfile, "r") as file:
            single = file.readlines()
            list_hashes = [x.strip() for x in single]
            checker = functools.partial(cracker, list_hashes)
            result = pool.map(checker, list_dict)


def HashCrackerDictionary(workers, dictionary, hashes):
    # importing the dictionary
    # hashes = ["d2cbe65f53da8607e64173c1a83394fe"]
    pool = multiprocessing.Pool(workers)
    with open(dictionary, "r") as file:
        lines = file.readlines()
        # creates a list with the words from the dictionary
        list_dict = [x.strip() for x in lines]
        checker = functools.partial(cracker, hashes)
        result = pool.map(checker, list_dict)


def HashCrackerDictionary_single(dictionary, hashes):
    with open(dictionary, "r") as file:
        lines = file.readlines()
        # creates a list with the words from the dictionary
        lines = [x.strip() for x in lines]
        for line in lines:
            # encode each line into bit so it can be hashed
            hashed_dict = str(hashlib.md5(line.encode()).hexdigest())
            # statement to check for correct password
            if hashed_dict in hashes:
                print(hashed_dict, "is the corresponding hash to", line)
                


def HashCrackerDictionary_SingleHashFile(dictionary, hashfile):
    with open(dictionary, "r") as file:
        lines = file.readlines()
        # creates a list with the words from the dictionary
        list_dict = [x.strip() for x in lines]
        with open(hashfile, "r") as file:
            single = file.readlines()
            list_hashes = [y.strip() for y in single]
            for line in list_dict:
                # encode each line into bit so it can be hashed
                hashed_dict = str(hashlib.md5(line.encode()).hexdigest())
                # statement to check for correct password
                if hashed_dict in list_hashes:
                    print(hashed_dict, "is the corresponding hash to", line)
                    

def HashCrackerPermutations(workers, alphabet, max_length, hashes):
    # hashes = ["534b44a19bf18d20b71ecc4eb77c572f"]
    pool = multiprocessing.Pool(workers)
    checker = functools.partial(cracker_perm_wrapper, hashes)
    for length in range(1, max_length+1):
        result = list(pool.imap(checker, itertools.product(list(alphabet), repeat=length), chunksize=100))
     


def HashCrackerPermutations_single(alphabet, max_length, hashes):
    # if known how long the password is change it to its length + 1
    for length in range(1, max_length + 1):
        for s in itertools.product(list(alphabet), repeat=length):
            hashed_perm = str(hashlib.md5(''.join(s).encode()).hexdigest())
            if hashed_perm in hashes:
                print(hashed_perm, "is the corresponding hash to", ''.join(s))
                


def HashCrackerPermutationsListHashes(workers, alphabet, max_length, hashfile):
    # hashes = ["534b44a19bf18d20b71ecc4eb77c572f"]
    pool = multiprocessing.Pool(workers)
    with open(hashfile, "r") as file:
        single = file.readlines()
        list_hashes = [y.strip() for y in single]
        checker = functools.partial(cracker_perm_wrapper, list_hashes)
        for length in range(1, max_length+1):
            result = list(pool.imap(checker, itertools.product(list(alphabet), repeat=length), chunksize=100))



def HashCrackerPermutations_SingleHashFile(alphabet, max_length, hashfile):
    # if known how long the password is change it to its length + 1
    with open(hashfile, "r") as file:
        single = file.readlines()
        list_hashes = [y.strip() for y in single]
        for length in range(1, max_length + 1):
            for s in itertools.product(list(alphabet), repeat=length):
                hashed_perm = str(hashlib.md5(''.join(s).encode()).hexdigest())
                if hashed_perm in list_hashes:
                    print(hashed_perm, "is the corresponding hash to", ''.join(s))
                    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Crack a Hash')

    parser.add_argument("type", help="Choose with which method you'd like to \
        crack a hash", choices=["Dictionary", "dictionary", "Permutations", "permutations"])

    parser.add_argument("type2", help="Do you want to hash from a file or input hashes?",\
        choices=["List", "File"])

    parser.add_argument("--multiprocessing", type=int, default=1, help="Leave it \
        empty for singleprocessing, put in the numbers of workers for multiprocessing")

    parser.add_argument("--hashes", type=str, default="47bce5c74f589f4867dbd57e9ca9f808",\
        help="The hash that you want to know")

    parser.add_argument("--alphabet", type=str, default="a", help="The characters that are\
         used for the permutation")

    parser.add_argument("--max_length", type=int, default=8, help="Choose the maximal length \
        permutations should have")

    parser.add_argument("--filename", type=str, default="words_alpha.txt", help="Choose with \
        which file you want to hash, default is words_alpha.txt")

    args = parser.parse_args()

    if args.type == "dictionary":
        if args.multiprocessing == 1:
            if args.type2 == "List":
                time_start()
                HashCrackerDictionary_single(args.filename, args.hashes)
                time_end()
            else:
                time_start()
                HashCrackerDictionary_SingleHashFile(args.filename, "list_of_hashes.txt")
                time_end()
        else:
            if args.type2 =="List":
                time_start()
                HashCrackerDictionary(args.multiprocessing, args.filename, [args.hashes])
                time_end()
            else:
                time_start()
                HashCrackerDictionaryHashFile(args.multiprocessing, args.filename, "list_of_hashes.txt")
                time_end()
    else:
        if args.multiprocessing == 1:
            if args.type2 == "List":
                time_start()
                HashCrackerPermutations_single(args.alphabet, args.max_length, args.hashes)
                time_end()
            else:
                time_start()
                HashCrackerPermutations_SingleHashFile(args.alphabet, args.max_length, "list_of_hashes.txt")
                time_end()
        else:
            if args.type2 == "File":
                time_start()
                HashCrackerPermutations(args.multiprocessing, args.alphabet, args.max_length, [args.hashes])
                time_end()
            else:
                time_start()
                HashCrackerPermutations(args.multiprocessing, args.alphabet, args.max_length, "list_of_hashes.txt")
                time_end()