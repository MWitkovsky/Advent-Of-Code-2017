import sys
from copy import deepcopy

STARTING_PROGRAMS = list("abcdefghijklmnop")

def spin(array, num):
    num = len(array)-(num)
    return array[num:] + array[0:num]

def exchange(array, a, b):
    array[a], array[b] = array[b], array[a]

def partner(array, a, b):
    a = array.index(a); b = array.index(b)
    array[a], array[b] = array[b], array[a]

def perform_dance(array, moves):
    for move in moves:
        move_type = move[0]
        if move_type == "s":
            array = spin(array, int(move[1:]))
        elif move_type == "x":
            move = move[1:].split("/")
            exchange(array, int(move[0]), int(move[1]))
        elif move_type == "p":
            move = move[1:].split("/")
            partner(array, move[0], move[1])
    return array

def permutation_promenade(string):
    # part 1
    moves = string.replace("\n","").split(",")
    programs = deepcopy(STARTING_PROGRAMS)
    programs = perform_dance(programs, moves)
    print "Part 1 Solution: %s" % "".join(programs)

    # part 2
    seen = {"".join(STARTING_PROGRAMS): "".join(programs)}
    i = 999999999
    while i > 0:
        result = seen.get("".join(programs))
        if result:
            i %= len(seen)
            programs = result
        else:
            key = "".join(programs)
            programs = perform_dance(programs, moves)
            seen[key] = "".join(programs)
        i -= 1
    print "Part 2 Solution: %s" % "".join(programs)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    permutation_promenade(inp)
