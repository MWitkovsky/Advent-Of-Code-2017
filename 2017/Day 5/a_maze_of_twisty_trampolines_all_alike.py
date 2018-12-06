import sys

def a_maze_of_twisty_trampolines_all_alike(string):
    # part 1
    pointer = 0
    num_steps = 0
    instructions = [int(jump) for jump in string.split("\n")]
    while pointer >= 0 and pointer < len(instructions):
        instructions[pointer] += 1
        pointer += instructions[pointer]-1
        num_steps += 1

    print "Part 1 Solution: %s" % num_steps

    # part 2
    pointer = 0
    num_steps = 0
    instructions = [int(jump) for jump in string.split("\n")]
    while pointer >= 0 and pointer < len(instructions):
        if instructions[pointer] >= 3:
            instructions[pointer] -= 1
            offset = 1
        else:
            instructions[pointer] += 1
            offset = -1
        pointer += instructions[pointer] + offset
        num_steps += 1

    print "Part 2 Solution: %s" % num_steps

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    a_maze_of_twisty_trampolines_all_alike(inp)
