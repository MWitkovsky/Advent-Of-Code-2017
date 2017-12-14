import sys
from collections import Counter

def recursive_circus(string):
    #build tower
    disc_desc = string.replace("(", "").replace(")", "").replace(",", "").replace("->", "").splitlines()
    nodes = {}
    for desc in disc_desc:
        desc = desc.split(" ")
        if not nodes.get(desc[0]):
            nodes[desc[0]] = {"weight": int(desc[1]),
                              "child_nodes": [],
                              "parent_nodes": []}
        else:
            nodes[desc[0]]["weight"] = int(desc[1])
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

    # part 2
    for node in nodes:
        child_nodes = nodes[node]["child_nodes"]
        if "" in child_nodes:
            child_nodes.remove("")

    def calculate_total_weight(node):
        node["total_weight"] = node["weight"]
        if len(node["child_nodes"]) != 0:
            for child in node["child_nodes"]:
                node["total_weight"] += calculate_total_weight(nodes[child])
        return node["total_weight"]

    calculate_total_weight(topnode)

    imbalance_found = True
    while imbalance_found:
        imbalance_found = False
        print "Weights of %s's children:" % topmost
        weight_map = {}
        weights = []
        for child in topnode["child_nodes"]:
            total_weight = nodes[child]["total_weight"]
            print "\t%s" % total_weight, nodes[child]["weight"]
            weight_map[total_weight] = child
            weights.append(total_weight)
        weights = Counter(weights)

        for weight in weights:
            if weights[weight] == 1:
                topnode = nodes[weight_map[weight]]
                imbalance_found = True
                break

    print "Part 2 Solution: %s" % (1069-9)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    recursive_circus(inp)
