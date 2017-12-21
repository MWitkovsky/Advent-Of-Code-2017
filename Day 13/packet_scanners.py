import sys
from copy import deepcopy

def packet_scanners(string):
    scanners = {}
    for line in string.splitlines():
        line = line.split(": ")
        scanners[int(line[0])] = {}
        scanners[int(line[0])]["direction"] = 1
        scanners[int(line[0])]["scanner"] = [None] * int(line[1])
        scanners[int(line[0])]["scanner"][0] = "s"

    severity = 0
    def timestep():
        for scanner in scanners.values():
            scn = scanner["scanner"]
            dr = scanner["direction"]
            i = scn.index("s")
            scn[i] = None
            scn[i+dr] = "s"
            if i+dr in (0, len(scn)-1):
                scanner["direction"] *= -1

    for i in range(max(scanners)):
        scanner = scanners.get(i)
        if scanner and scanner["scanner"][0] == "s":
            severity += i*len(scanner["scanner"])
        timestep()

    print "Part 1 Solution: %s" % severity

    def reset_scanners():
        for scanner in scanners.values():
            scn = scanner["scanner"]
            scn[scn.index("s")] = None
            scn[0] = "s"
            scanner["direction"] = 1

    start_picosecond = -1
    severity = 1
    reset_scanners()
    snapshot = deepcopy(scanners)
    while severity != 0:
        start_picosecond += 1
        scanners = deepcopy(snapshot)
        timestep()
        snapshot = deepcopy(scanners)
        severity = 0
        for i in range(max(scanners)):
            scanner = scanners.get(i)
            if scanner and scanner["scanner"][0] == "s":
                severity = 1
                continue
            timestep()

    print "Part 2 Solution: %s" % start_picosecond


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    packet_scanners(inp)
