import sys
sys.path.append("../../")

from lib import utils
from collections import defaultdict, Counter


def problem(inp):
    duty_log = inp.splitlines()

    print ("part 1: {0}".format())
    print ("part 2: {0}".format())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    problem(inp)
