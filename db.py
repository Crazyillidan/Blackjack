import os

def read_chips():
    if os.path.exists("chips.txt"):
        with open("chips.txt", "r") as file:
            return float(file.read())
    else:   
        return 100

def write_chips(chips):
    with open("chips.txt", "w") as file:
        file.write(str(chips))
