import itertools
import multiprocessing
import argparse
import hashlib
import time
import functools


tries = 1
num_hashes = 20
num_workers = 4
dict_name = "words_alpha.txt"
hashfile_name = "list_of_hashes.txt"
output_name = "benchmarks_dict.txt"
time_tot = 0
round_nmbr = 0
def time_start():
    global time_starter
    time_starter = time.time()


def time_end():
    time_ended = time.time()
    time_total = time_ended - time_starter
    return time_total


def cracker(hashes, word):
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    if hashed_word in hashes:
        pass


def HashCrackerDictionaryHashFile(workers, dictionary, hashfile, num_hashes):
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
            checker = functools.partial(cracker, list_hashes[:num_hashes])
            result = pool.map(checker, list_dict)
            pool.terminate()


if __name__ == "__main__":
    t1 = time.time()
    while num_workers > 0:
        f = open("benchmarks_dict.txt", "a")
        while num_hashes <= 5000:
            while tries < 11:
                time_start()
                HashCrackerDictionaryHashFile(num_workers, dict_name, hashfile_name, num_hashes)
                timed = time_end()
                time_tot += timed
                tries += 1
            time_av = time_tot / 10
            time_tot = 0
            tries = 1
            f.write(str(time_av) + ", ")
            round_nmbr += 1
            print(round_nmbr)
            num_hashes += 20
        round_nmbr = 0
        num_workers -= 1
        num_hashes = 20
        f.write("workers: " + str(num_workers) + "\n")
        f.close()
    t2 = time.time()