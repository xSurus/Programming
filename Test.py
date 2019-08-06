import multiprocessing
import hashlib
import time
import functools
import itertools


def time_start():
    global time_start
    time_start = time.time()


def time_end():
    time_end = time.time()
    time_total = time_end - time_start
    print(time_total)

def cracker(hashes, word):
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    print("hi")
    if hashed_word in hashes:
        print(hashed_word, "is the corresponding hash to ", word)

def cracker_perm_wrapper(hashes, pw):
        password =''.join(pw)
        cracker(hashes, password)


def HashCrackerDictionary(dictionary):
    # importing the dictionary
    hashes = ["d2cbe65f53da8607e64173c1a83394fe"]
    pool = multiprocessing.Pool(4)
    with open(dictionary, "r") as file:
        lines = file.readlines()
        # creates a list with the words from the dictionary
        list_dict = [x.strip() for x in lines]
        checker = functools.partial(cracker, hashes)
        result = list(pool.map(checker, list_dict))

def HashCrackerPermutations(alphabet, max_length):
    hashes = ["6c7be0759b9fe15878dbd4cd7c5d0d84"]
    pool = multiprocessing.Pool(4)
    checker = functools.partial(cracker_perm_wrapper, hashes)
    for length in range(1, max_length+1):
        result = list(pool.imap(checker, itertools.product(alphabet, repeat=length)))
     

if __name__ == "__main__":
    time_start()
    #HashCrackerDictionary("./words_alpha.txt")
    HashCrackerPermutations(['a', 'n', 'e'], 5)
    time_end()