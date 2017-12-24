import sys

def problem(string):

    # print "Part 1 Solution: %s" % num_matches
    # print "Part 2 Solution: %s" % num_matches


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    problem(inp)
