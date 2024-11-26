import os

# Function to read player's chips from file

# Program will start with 100 if file is not found

def read_chips():
    if os.path.exists("chips.txt"):
        with open("chips.txt", "r") as file:
            return float(file.read())
    else:   
        return 100

# Function to write player's chips to file

def write_chips(chips):
    with open("chips.txt", "w") as file:
        file.write(str(chips))
