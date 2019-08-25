import hashlib
filename = "words_alpha.txt"
hashed_pw = input("Please input the hashed word.")
with open(filename, "r") as file:
    # read all lines and create a list with all the words
    lines = file.readlines()
    lines = [x.strip() for x in lines]
    for line in lines:
        # encode (put it into bits) each line
        line = line.encode()
        # hash the encoded word
        hashed_dict = hashlib.md5(line).hexdigest()
        # if the hashed word corresponds to the created hash
        # print the word, before it was hashed
        if hashed_dict == hashed_pw:
            print(line)
            break
