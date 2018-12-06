import sys

def corruption_checksum(string):
    string = string.split("\n")

    # part 1
    checksum = 0
    for i, line in enumerate(string):
        string[i] = [int(num) for num in line.split("\t")]
        checksum += max(string[i]) - min(string[i])
    print "Part 1 Solution: %s" % checksum

    # part 2
    checksum = 0
    for line in string:
        found = False
        for i, val1 in enumerate(line):
            for j, val2 in enumerate(line):
                if i == j:
                    continue
                if val1 % val2 == 0:
                    checksum += val1 / val2
            if found:
                break
    print "Part 2 Solution: %s" % checksum


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    corruption_checksum(inp)
