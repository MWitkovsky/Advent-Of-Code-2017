import sys
from copy import deepcopy

def packet_scanners(string):
    scanners = {}
    for line in string.splitlines():
        line = line.split(": ")
        scanners[int(line[0])] = {}
        scanners[int(line[0])]["direction"] = 1
        scanners[int(line[0])]["len"] = int(line[1])-1

    severity = 0
    picosecond = 0
    for i in range(max(scanners)):
        if i == 0:
            continue
        picosecond += 1
        scanner = scanners.get(i)
        if scanner and picosecond % ((scanner["len"])*2) == 0:
            severity += i*(scanner["len"]+1)

    print "Part 1 Solution: %s" % severity

    start_picosecond = -1
    severity = 1
    while severity != 0:
        if not start_picosecond % 1000:
            print start_picosecond
        start_picosecond += 1
        picosecond = start_picosecond
        severity = 0
        for i in range(max(scanners)):
            picosecond += 1
            scanner = scanners.get(i)
            if scanner and picosecond % ((scanner["len"])*2) == 0:
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
