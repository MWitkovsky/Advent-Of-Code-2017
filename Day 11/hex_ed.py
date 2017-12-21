import sys
from copy import deepcopy
from collections import Counter

def hex_ed(string):
    oldAmounts = Counter(string.replace("\n", "").split(","))
    amounts = deepcopy(oldAmounts)
    while True:
        oldAmounts = deepcopy(amounts)
        if amounts["n"] and amounts["s"]:
            amounts["n"] -= 1
            amounts["s"] -= 1
        if amounts["ne"] and amounts["sw"]:
            amounts["ne"] -= 1
            amounts["sw"] -= 1
        if amounts["nw"] and amounts["se"]:
            amounts["nw"] -= 1
            amounts["se"] -= 1

        if amounts["ne"] and amounts["nw"]:
            amounts["ne"] -= 1
            amounts["nw"] -= 1
            amounts["n"] += 1
        if amounts["n"] and amounts["sw"]:
            amounts["n"] -= 1
            amounts["sw"] -= 1
            amounts["nw"] += 1
        if amounts["nw"] and amounts["s"]:
            amounts["nw"] -= 1
            amounts["s"] -= 1
            amounts["sw"] += 1
        if amounts["sw"] and amounts["se"]:
            amounts["sw"] -= 1
            amounts["se"] -= 1
            amounts["s"] += 1
        if amounts["s"] and amounts["ne"]:
            amounts["s"] -= 1
            amounts["ne"] -= 1
            amounts["se"] += 1
        if amounts["se"] and amounts["n"]:
            amounts["se"] -= 1
            amounts["n"] -= 1
            amounts["ne"] += 1
        if oldAmounts == amounts:
            break
    print "Part 1 Solution: %s" % (sum(amounts.values()))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    hex_ed(inp)
