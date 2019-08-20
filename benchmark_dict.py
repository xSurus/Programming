import itertools
import multiprocessing
import argparse
import hashlib
import time
import functools


dict_name = "words_alpha.txt"
hashfile_name = "list_of_hashes.txt"
output_name = "test.txt"
num_hashes_start = 5
#the amount of workers will go down from this number
num_workers_start = 4


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

def HashCrackerDictionary_SingleHashFile(dictionary, hashfile, num_hashes):
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
                if hashed_dict in list_hashes[:num_hashes]:
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


def benchmark_single():
    round_nmbr = 0
    num_hashes = num_hashes_start
    f = open("benchmarks_dict.txt", "a")        
    f.write("Singlethread\n")
    while num_hashes <= 5000:
        t1 = time_start()
        for i in range(10):
            HashCrackerDictionary_SingleHashFile(dict_name, hashfile_name, num_hashes)
        t2 = time_end(t1)
        time_av = t2 / 10
        f.write(str(time_av) + "\n")
        round_nmbr += 1
        print(round_nmbr)
        num_hashes += 20
        f.close()        

def bechmark_multi(num_hashes_start, num_workers_start):
    round_nmbr = 0
    num_hashes = num_hashes_start
    num_workers = num_workers_start
    while num_workers > 0:
        f = open(output_name, "a")
        f.write("Number of workers: " + str(num_workers) + "\n")
        while num_hashes <= 5000:
            t1 = time_start()
            for i in range(10):
                HashCrackerDictionaryHashFile(num_workers, dict_name, hashfile_name, num_hashes)
            t2 = time_end(t1)
            time_av = t2 / 10
            f.write(str(time_av) + "\n")
            round_nmbr += 1
            print(round_nmbr)
            num_hashes += 20
        round_nmbr, num_hashes = 0, 20
        num_workers -= 1
        f.close()
    benchmark_single()

if __name__ == "__main__":
    ts = time_start()
    bechmark_multi(num_hashes_start, num_workers_start)
    te = time_end(ts)
    print(f"Done:\nFinished all the permutations with {num_workers_start} workers until singleprocessing in {te} seconds")