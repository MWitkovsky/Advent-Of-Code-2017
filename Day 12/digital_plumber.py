import sys

def digital_plumber(string):
    programs = {}
    for line in string.splitlines():
        line = line.replace(" ", "").split("<->")
        programs[int(line[0])] = {}
        programs[int(line[0])]["links"] = map(int, line[1].split(","))

    all_programs = set(programs.keys())
    visited = set()
    def search_for_connected_programs(program):
        for p in programs[program]["links"]:
            if p not in visited:
                visited.add(p)
                search_for_connected_programs(p)

    search_for_connected_programs(0)

    print "Part 1 Solution: %s" % len(visited)

    groups = 1
    all_programs -= visited
    while all_programs != set([]):
        search_for_connected_programs(all_programs.pop())
        all_programs -= visited
        groups += 1

    print "Part 2 Solution: %s" % groups


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    digital_plumber(inp)
