import sys, math

def knot_hash(string):
    knot = range(256)
    pointer = 0
    skip = 0
    def reverse_section_circular(start, length):
        end = start + length-1
        length = math.floor(length/2)
        if end >= len(knot):
            end -= len(knot)
        while length > 0:
            knot[start], knot[end] = knot[end], knot[start]
            start += 1
            if start == len(knot):
                start = 0
            end -= 1
            if end < 0:
                end = len(knot)-1
            length -= 1

    for val in map(int, string.split(",")):
        reverse_section_circular(pointer, val)
        pointer += val + skip
        if pointer >= len(knot):
            pointer -= len(knot)
        skip += 1

    print "Part 1 Solution: %s" % (knot[0] * knot[1])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    knot_hash(inp)
