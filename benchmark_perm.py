import itertools
import multiprocessing
import argparse
import hashlib
import time
import functools


hashfile_name = "list_of_hashes_perm_more.txt"
output_name = "benchmarks_perm_more.txt"
num_hashes_start = 20
num_workers_start = 0
max_length = 7
alphabet = ["a", "e", "s", "m", "f", "l"]


def time_start():
    time_starter = time.time()
    return time_starter


def time_end(time_starter):
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

def HashCrackerPermutations_SingleHashFile(alphabet, max_length, hashfile, num_hashes):
    # if known how long the password is change it to its length + 1
    with open(hashfile, "r") as file:
        single = file.readlines()
        list_hashes = [y.strip() for y in single]
        for length in range(1, max_length + 1):
            for s in itertools.product(list(alphabet), repeat=length):
                hashed_perm = str(hashlib.md5(''.join(s).encode()).hexdigest())
                if hashed_perm in list_hashes[:num_hashes]:
                    pass
                    

def HashCrackerPermutationsFileHashes(workers, alphabet, max_length, hashfile, num_hashes):
    # hashes = ["534b44a19bf18d20b71ecc4eb77c572f"]
    pool = multiprocessing.Pool(workers)
    with open(hashfile, "r") as file:
        single = file.readlines()
        list_hashes = [y.strip() for y in single]
        checker = functools.partial(cracker_perm_wrapper, list_hashes[:num_hashes])
        for length in range(1, max_length+1):
            result = list(pool.imap(checker, itertools.product(list(alphabet), repeat=length), chunksize=100))
        pool.terminate()


def becnhmark_single():
    round_nmbr = 0
    num_hashes = num_hashes_start
    f = open(output_name, "a")
    f.write("Singlethread\n")
    while num_hashes <= 5000:
        t1 = time_start()
        for i in range(10):
            HashCrackerPermutations_SingleHashFile(alphabet, max_length, hashfile_name, num_hashes)
        t2 = time_end(t1)
        time_av = t2 / 10
        f.write(str(time_av) + "\n")
        round_nmbr += 1
        print(round_nmbr)
        num_hashes += 20
    round_nmbr, num_hashes = 0, 20
    f.close()


def becnhmark_multi(num_hashes_start, num_workers_start):
    round_nmbr= 0
    num_hashes = num_hashes_start
    num_workers = num_workers_start
    while num_workers > 0:
        f = open(output_name, "a")
        f.write("Number of workers: " + str(num_workers) + "\n")
        while num_hashes <= 5000:
            t1 = time_start()
            for i in range(10):
                HashCrackerPermutationsFileHashes(num_workers, alphabet, max_length, hashfile_name, num_hashes)
            t2 = time_end(t1)
            time_av = t2 / 10
            f.write(str(time_av) + "\n")
            round_nmbr += 1
            print(round_nmbr)
            num_hashes += 20
        round_nmbr, num_hashes = 0, 20
        num_workers -= 1
        f.close()


if __name__ == "__main__":
    ts = time_start()
    becnhmark_multi(num_hashes_start, num_workers_start)
    te = time_end(ts)  
    print(f"Done:\nFinished all the permutations with {num_workers_start} workers until singleprocessing in {te} seconds")