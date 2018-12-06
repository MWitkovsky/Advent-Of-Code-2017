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

    bytelist = []
    for char in string.replace("\n", ""):
        bytelist.append(ord(char))
    bytelist.extend([17, 31, 73, 47, 23])

    for i in range(64):
        for val in bytelist:
            reverse_section_circular(pointer, val)
            pointer += val + skip
            while pointer >= len(knot):
                pointer -= len(knot)
            skip += 1

    pointer = 0
    dense_hash = []
    while pointer < len(knot):
        val = 0
        for i in range(16):
            val ^= knot[pointer+i]
        dense_hash.append(val)
        pointer += 16

    for i, val in enumerate(dense_hash):
        dense_hash[i] = hex(val)[2:]

    print "Part 2 Solution: %s" % "".join(dense_hash)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    knot_hash(inp)
