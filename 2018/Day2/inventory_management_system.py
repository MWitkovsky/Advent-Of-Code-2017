import sys
sys.path.append("../../")

from lib import utils
from collections import Counter
from difflib import SequenceMatcher


def find_similar(items_to_check, sim_ratio):
    for i, id1 in enumerate(items_to_check):
        s = SequenceMatcher(a=id1, b=items_to_check[i])

        for id2 in items_to_check[i+1:]:
            s.set_seq2(id2)
            if s.ratio() == sim_ratio:
                return True, (id1, id2)
    return False, "No similar found"


def inventory_management(inp):
    inp = utils.lines_to_array(inp)

    two_rec_count = 0
    three_rec_count = 0
    for line in inp:
        line_counter = Counter(line)
        vals = line_counter.values()
        if 2 in vals:
            two_rec_count += 1
        if 3 in vals:
            three_rec_count += 1

    print ("part 1: {0}".format(two_rec_count * three_rec_count))

    ratio = (len(inp[0])-1) / len(inp[0])
    ok, info = find_similar(inp, ratio)
    if not ok:
        print(info)
        return

    id1, id2 = info
    print ("part 2: {0}".format("".join([c for i, c in enumerate(id1)
                                                              if c == id2[i]])))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    inventory_management(inp)
