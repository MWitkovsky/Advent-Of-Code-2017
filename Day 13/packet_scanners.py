import sys
from copy import deepcopy

def packet_scanners(string):
    scanners = {}
    for line in string.splitlines():
        line = line.split(": ")
        scanners[int(line[0])] = int(line[1])-1

    severity = 0
    for i in scanners:
        length = scanners[i]
        if i % (length*2) == 0:
            severity += i*(length+1)

    print "Part 1 Solution: %s" % severity

    start_picosecond = -1
    severity = 1
    while severity != 0:
        start_picosecond += 1
        severity = 0
        for i in scanners:
            length = scanners[i]
            if (start_picosecond+i) % (length*2) == 0:
                severity = 1
                break

    print "Part 2 Solution: %s" % start_picosecond


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    packet_scanners(inp)
