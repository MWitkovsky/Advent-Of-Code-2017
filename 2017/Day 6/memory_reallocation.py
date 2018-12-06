import sys
from copy import deepcopy

def distribute_memory(memory):
    pointer = memory.index(max(memory))
    blocks = memory[pointer]
    memory[memory.index(max(memory))] = 0
    while blocks > 0:
        pointer += 1
        if pointer == len(memory):
            pointer = 0
        memory[pointer] += 1
        blocks -= 1
    return memory

def memory_reallocation(string):
    # part 1
    memory = map(int, string.split("\t"))
    seen = [deepcopy(memory)]
    while True:
        memory = distribute_memory(memory)
        if memory in seen:
            break
        seen.append(deepcopy(memory))

    print "Part 1 Solution: %s" % len(seen)

    print "Part 2 Solution: %s" % (len(seen) - seen.index(memory))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    memory_reallocation(inp)
