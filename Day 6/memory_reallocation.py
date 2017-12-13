import sys
from copy import deepcopy

def memory_reallocation(string):
    memory = map(int, string.split("\t"))
    seen = [deepcopy(memory)]
    while True:
        pointer = memory.index(max(memory))
        blocks = memory[pointer]
        memory[memory.index(max(memory))] = 0
        while blocks > 0:
            pointer += 1
            if pointer == len(memory):
                pointer = 0
            memory[pointer] += 1
            blocks -= 1
        if memory in seen:
            break
        seen.append(deepcopy(memory))

    print len(seen)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    memory_reallocation(inp)
