import sys

def inverse_captcha(string):
    # part 1
    string += string[0]
    total = 0
    for i, char in enumerate(string):
        if i == len(string)-1:
            break
        if char == string[i+1]:
            total += int(char)
    print "Part 1 Solution: %s" % total

    # part 2
    string = string[:-1]
    halflen = len(string)/2
    total = 0
    for i, char in enumerate(string):
        test_index = i + halflen
        if test_index >= len(string):
            test_index -= len(string)
        if char == string[test_index]:
            total += int(char)
    print "Part 2 Solution: %s" % total


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    inverse_captcha(inp)
