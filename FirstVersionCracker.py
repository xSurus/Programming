import hashlib
filename = "words_alpha.txt"
hashed_pw = input("Please input the hashed word.")
with open(filename, "r") as file:
    lines = file.readlines()
    lines = [x.strip() for x in lines]
    for line in lines:
        line = line.encode()
        hashed_dict = hashlib.md5(line).hexdigest() 
        if hashed_dict == hashed_pw:
            print(line)
            break
# here lines still exists
# the file is closed
