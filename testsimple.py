import itertools
import multiprocessing
import argparse
import hashlib
import time
import functools

def HashCrackerPermutations_single(alphabet, max_length, hashes):
    # if known how long the password is change it to its length + 1
    for length in range(1, max_length + 1):
        for s in itertools.product(list(alphabet), repeat=length):
            hashed_perm = str(hashlib.md5(''.join(s).encode()).hexdigest())
            if hashed_perm in hashes:
                print(hashed_perm, "is the corresponding hash to", ''.join(s))
            print("hi")

HashCrackerPermutations_single(["a", "b", "c"], 4, ["ea01e5fd8e4d8832825acdd20eac5104"])