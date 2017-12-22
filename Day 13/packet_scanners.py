import sys
from copy import deepcopy

def packet_scanners(string):
    scanners = {}
    for line in string.splitlines():
        line = line.split(": ")
        scanners[int(line[0])] = {}
        scanners[int(line[0])]["direction"] = 1
        scanners[int(line[0])]["len"] = int(line[1])-1
        scanners[int(line[0])]["pos"] = 0

    severity = 0
    def timestep():
        for scanner in scanners.values():
            length = scanner["len"]
            dr = scanner["direction"]
            scanner["pos"] += dr
            if scanner["pos"] in (0, length):
                scanner["direction"] *= -1

    for i in range(max(scanners)):
        scanner = scanners.get(i)
        if scanner and scanner["pos"] == 0:
            severity += i*(scanner["len"]+1)
        timestep()

    print "Part 1 Solution: %s" % severity

    def reset_scanners():
        for scanner in scanners.values():
            scanner["direction"] = 1
            scanner["pos"] = 0

    start_picosecond = -1
    severity = 1
    reset_scanners()
    snapshot = deepcopy(scanners)
    while severity != 0:
        if not start_picosecond % 1000:
            print start_picosecond
        start_picosecond += 1
        scanners = deepcopy(snapshot)
        timestep()
        snapshot = deepcopy(scanners)
        severity = 0
        for i in range(max(scanners)):
            scanner = scanners.get(i)
            if scanner and scanner["pos"] == 0:
                severity = 1
                break
            timestep()

    print "Part 2 Solution: %s" % start_picosecond


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    packet_scanners(inp)
