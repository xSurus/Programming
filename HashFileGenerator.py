import hashlib
import random
import itertools


made_perm = []
used_hashes = []

"""
following lines can be adjusted to the users liking
"""
dictionary = "words_alpha.txt"
output_dict = "list_of_hashes_dict.txt"
output_perm = "list_of_hashes_perm_more.txt"
alphabet = ["a", "e", "s", "m", "f", "l"]
max_length = 7

# generates 5019 hashes from a dictionary
def HashFileGeneratorDict(dictionary, output):
    with open(output, "a") as ouputfile:
        with open(dictionary, "r") as dictionaryfile:
            lines = dictionaryfile.readlines()
            # creates a list with the words from the dictionary
            list_dict = [y.strip() for y in lines]
            while len(used_hashes) < 5020:
                # hash a random word from the dictionary
                hashed_wrd = str(hashlib.md5(''.join(list_dict[random.randint(
                                            1, 370098)]).encode()).hexdigest())
                # check if this word has not been hashed before, if not then
                # write it on the output file and append it to a list
                if hashed_wrd not in used_hashes:
                    used_hashes.append(hashed_wrd)
                    ouputfile.write(hashed_wrd + "\n")

# generate 5019 hashes from a list of permutations made from an input
def HashFileGeneratorPerm(output):
    with open(output, "a") as ouputfile:
        for length in range(1, max_length + 1):
            # create all the permutations and append them to a list
            for s in itertools.product(alphabet, repeat=length):
                made_perm.append(s)
        # goal is 5019 hashes so while it's less than 5020 
        while len(used_hashes) < 5020:
            # choose a random permutation from the list and hash it
            hashed_wrd = str(hashlib.md5(''.join(made_perm[random.randint(
                                        1, 19510)]).encode()).hexdigest())
            # check if this word has already been used
            if hashed_wrd not in used_hashes:
                # write that word on output file and append to list
                used_hashes.append(hashed_wrd)
                ouputfile.write(hashed_wrd + "\n")

# very simple version to choose which function to use
if __name__ == "__main__":
    user_input = input("Do you want make a file with hashes out of\n\
                    a) a dictionary and hash it's words, then type in a or \n\
                    b) randomly generate them from an input of letters, then\
                    type in b\n")
    while user_input != "a" and user_input != "b" and user_input != "exit":
        print("You didn't choose either of the options, try again.\nIf you \
              wish to exit type: exit")
        user_input = input()
    if user_input == "a":
        HashFileGeneratorDict(dictionary, output_dict)
    elif user_input == "b":
        HashFileGeneratorPerm(output_perm)
    elif user_input == "exit":
        pass
