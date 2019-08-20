import os

x = 0
with open("C:/Users/alexa/Documents/Matura/PaperOwn/benchmarks/benchmarks_dict.txt", "r+") as f:
    for line in f:
            for word in line:
                x += 1
                if x == 3:
                    y = line.split()
                    print(y)