import sys
from collections import Counter

def high_entropy_passphrases(string):
    # part 1
    num_valid = 0
    for line in string.split("\n"):
        line = line.split(" ")
        if len(line) == len(set(line)):
            num_valid += 1

    print "Part 1 Solution: %s" % num_valid

    # part 2
    num_valid = 0
    for line in string.split("\n"):
        line = line.split(" ")
        if len(line) == len(set(line)):
            line = map(Counter, line)
            bad = False
            for i, word1 in enumerate(line):
                for j, word2 in enumerate(line):
                    if i == j:
                        continue
                    if sum(word1.values()) == sum(word2.values()) and word1 - word2 == Counter():
                        bad = True
                if bad:
                    break
            if not bad:
                num_valid += 1

    print "Part 2 Solution: %s" % num_valid


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    high_entropy_passphrases(inp)
