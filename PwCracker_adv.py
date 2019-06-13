import hashlib
filename = "words_alpha.txt"
hashed_pw = input("Please input the hashed word.")
hashed_words = []
x = 0
def pwCracker():
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = [x.strip() for x in lines]
        for line in lines:
            line = line.encode()
            hashed_dict = hashlib.md5(line).hexdigest() 
            if hashed_dict not in hashed_words:
                hashed_words.append(hashed_dict)
                x += 1
                """  """
    """        if hashed_dict == hashed_pw:
                print(line)
                break"""
if __name__ == "__main__":
    pwCracker()
# here lines still exists
# the file is closed