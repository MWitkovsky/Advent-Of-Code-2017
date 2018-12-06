import sys

def high_entropy_passphrases(string):
    # part 1
    string2 = ""

    pointer = 0
    in_garbage = False
    score = 0
    score_val = 1
    garbage_count = 0
    while pointer < len(string):
        char = string[pointer]
        if in_garbage:
            garbage_count += 1
            if char == "!":
                garbage_count -= 1
                pointer += 2
                continue
            if char == ">":
                garbage_count -= 1
                in_garbage = False
        else:
            if char == "<":
                in_garbage = True
            if char == "{":
                score += score_val
                score_val += 1
            if char == "}":
                score_val -= 1
        pointer += 1

    print "Part 1 Solution: %s" % score
    print "Part 2 Solution: %s" % garbage_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    high_entropy_passphrases(inp)
