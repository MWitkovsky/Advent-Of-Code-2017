import sys

def recursive_circus(string):
    #build tower
    disc_desc = string.replace("(", "").replace(")", "").replace(",", "").replace("->", "").splitlines()
    nodes = {}
    for desc in disc_desc:
        desc = desc.split(" ")
        if not nodes.get(desc[0]):
            nodes[desc[0]] = {"weight": desc[1],
                              "child_nodes": [],
                              "parent_nodes": []}
        else:
            nodes[desc[0]]["weight"] = desc[1]
        if len(desc) > 2:
            for child_desc in desc[2:]:
                if not nodes.get(child_desc):
                    nodes[child_desc] = {"weight": 0,
                                         "child_nodes": [],
                                         "parent_nodes": [desc[0]]}
                else:
                    nodes[child_desc]["parent_nodes"].append(desc[0])
                nodes[desc[0]]["child_nodes"].append(child_desc)

    # part 1
    topmost = ""
    topnode = nodes[nodes.keys()[0]]
    while topnode["parent_nodes"] != []:
        topmost = topnode["parent_nodes"][0]
        topnode = nodes[topnode["parent_nodes"][0]]
    print "Part 1 Solution: %s" % topmost


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    recursive_circus(inp)
