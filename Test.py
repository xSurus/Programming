import itertools
import multiprocessing
import argparse
import hashlib
import time


def HashCrackerPermutations(hashes):
    global alphabet
    alphabet = ['h', 't', 'i', 'w', 'r', 'm', 'z']
    possible_strings = []
    hashed_words = []
    # if known how long the password is change it to its length + 1
    for r in range(1, len(alphabet)+1):
        for s in itertools.product(alphabet, repeat=r):
            possible_strings.append(''.join(s))
            for permutations in possible_strings:
                hashed_permutation = str(hashlib.md5(
                    permutations.encode()).hexdigest())
                for i in hashes:
                    if hashes == hashed_permutation and permutations not in\
                            hashed_words:
                        hashed_words.append(permutations)
                        print(hashes, "is the corresponding hash to", permutations)
            print(hashed_words)


if __name__ == "__main__":
    pool = multiprocessing.Pool(4)
    hashes = input("Please input the hashed words: ").split()
    parser = argparse.ArgumentParser(description='Crack a Hash')
    parser.add_argument("type", help="Choose with which method you'd like to \
        crack a hash")
    args = parser.parse_args()
    if args.type == "p,m":
        """alphabet = input("Please input the amount of letter you'll use")\
            .split()"""
        time_start_permutations = time.time()
        pool.map(HashCrackerPermutations, hashes)
        time_end_permutations = time.time()
        total_time_permutations = time_end_permutations - \
            time_start_permutations
        print(total_time_permutations)
