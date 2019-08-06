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
hashfile_name = "list_of_hashes_perm_more.txt"
output_name = "benchmarks_perm_more.txt"
time_tot = 0
round_nmbr = 0
alphabet = ["a", "e", "s", "m", "f", "l"]
max_length = 7


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


def cracker_perm_wrapper(hashes, pw):
        password =''.join(pw)
        cracker(hashes, password)


def HashCrackerPermutationsListHashes(workers, alphabet, max_length, hashfile, num_hashes):
    # hashes = ["534b44a19bf18d20b71ecc4eb77c572f"]
    pool = multiprocessing.Pool(workers)
    with open(hashfile, "r") as file:
        single = file.readlines()
        list_hashes = [y.strip() for y in single]
        checker = functools.partial(cracker_perm_wrapper, list_hashes[:num_hashes])
        for length in range(1, max_length+1):
            result = list(pool.imap(checker, itertools.product(list(alphabet), repeat=length), chunksize=100))
        pool.terminate()


if __name__ == "__main__":
    t1 = time.time()
    while num_workers > 0:
        f = open(output_name, "a")
        f.write("workers: " + str(num_workers) + "\n")
        while num_hashes <= 5000:
            while tries < 11:
                time_start()
                HashCrackerPermutationsListHashes(num_workers, alphabet, max_length, hashfile_name, num_hashes)
                end = time_end()
                time_tot += end
                tries += 1
            time_av = time_tot / 10
            time_tot, tries = 0, 1
            f.write(str(time_av) + "\n")
            round_nmbr += 1
            num_hashes += 20
        round_nmbr, num_hashes = 0, 20
        num_workers -= 1
        f.close()
    t2 = time.time()