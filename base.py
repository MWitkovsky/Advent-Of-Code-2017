import sys
sys.path.append("../")

from lib import utils

def process_input(string):
    pass

def part1(data):
    pass

def part2(data):
    pass


def problem(string):
    data = process_input(string)
    part1(data)
    part2(data)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    problem(inp)
