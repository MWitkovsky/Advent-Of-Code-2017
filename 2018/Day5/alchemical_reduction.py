import sys
sys.path.append("../../")

from lib import utils
from collections import defaultdict, Counter


def reduce_polymer(polymer):
    stack = []
    for char in polymer:
        if not stack:
            stack.append(char)
        elif stack[len(stack)-1].lower() == char.lower() and\
                stack[len(stack)-1] != char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)


def alchemical_reduction(inp):
    polymer = inp.splitlines()[0]
    reduced = reduce_polymer(polymer)

    print ("part 1: {0}".format(len(reduced)))

    char_2_purified_reduced_polymer_length = {}
    for i in range(65, 91, 1):
        char = chr(i)
        purified_polymer = polymer.replace(char, "").replace(char.lower(), "")
        char_2_purified_reduced_polymer_length[char] = len(reduce_polymer(purified_polymer))

    print ("part 2: {0}".format(sorted(char_2_purified_reduced_polymer_length.values())[0]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    alchemical_reduction(inp)
