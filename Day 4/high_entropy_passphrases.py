import sys

def high_entropy_passphrases(string):
    num_valid = 0
    for line in string.split("\n"):
        line = line.split(" ")
        if len(line) == len(set(line)):
            num_valid += 1

    print num_valid

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    high_entropy_passphrases(inp)
