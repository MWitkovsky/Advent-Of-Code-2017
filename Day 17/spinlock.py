import sys

def spinlock(string):
    # part 1
    spin_val = int(string)
    spin_list = [0]
    spin_pointer = 0
    for i in xrange(1, 2018):
        spin_pointer = (spin_pointer + spin_val) % len(spin_list)
        spin_list.insert(spin_pointer+1, i)
        spin_pointer += 1

    print "Part 1 Solution: %s" % spin_list[spin_list.index(2017)+1]

    # part 2
    spin_list = [0]
    spin_pointer = 0
    short_val = -1
    for i in xrange(1, 50000001):
        spin_pointer = (spin_pointer + spin_val) % i + 1
        if spin_pointer == 1:
            short_val = i
    print "Part 2 Solution: %s" % short_val


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    spinlock(inp)
