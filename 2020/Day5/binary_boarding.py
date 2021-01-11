import sys
sys.path.append("../../")

import math
from lib import utils


class BoardingPass:
    num_rows = 128
    num_cols = 8

    def __init__(self, bsp_str):
        row_lo, row_hi = 0, self.num_rows-1
        row_bsp = bsp_str[:-3]
        for bsp in row_bsp:
            diff_step = math.ceil((row_hi - row_lo)/2)
            if bsp == "F":
                row_hi -= diff_step
            else:
                row_lo += diff_step

        self.row = row_lo

        col_lo, col_hi = 0, self.num_cols-1
        col_bsp = bsp_str[-3:]
        for bsp in col_bsp:
            diff_step = math.ceil((col_hi - col_lo)/2)
            if bsp == "L":
                col_hi -= diff_step
            else:
                col_lo += diff_step

        self.col = col_lo

    @property
    def seat_id(self):
        return self.row * 8 + self.col


def binary_boarding(boarding_pass_strings):
    boarding_pass_strings = boarding_pass_strings.split("\n")
    boarding_passes = \
        [BoardingPass(bp_string) for bp_string in boarding_pass_strings]
    used_seats = {bp.seat_id for bp in boarding_passes}
    print(f"part 1: {max(used_seats)}")
    print([num for num in range(128*8) if num not in used_seats])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    binary_boarding(inp)
