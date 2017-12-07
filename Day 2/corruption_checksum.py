import sys

def corruption_checksum(string):
    string = string.split("\n")
    checksum = 0
    for i, line in enumerate(string):
        string[i] = [int(num) for num in line.split("\t")]
        checksum += max(string[i]) - min(string[i])
    print checksum

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    corruption_checksum(inp)
