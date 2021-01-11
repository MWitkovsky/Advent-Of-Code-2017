import sys
sys.path.append("../../")

from lib import utils


class TobagganMap:
    def __init__(self, map_str):
        self.map = map_str.split("\n")[:-1]
        self.map_height = len(self.map)
        self.map_width = len(self.map[0])

    def count_trees_on_slope(self, dx, dy):
        num_trees = 0
        curr_x, curr_y = -dx, -dy
        while curr_y < self.map_height - dy:
            curr_x = (curr_x + dx) % self.map_width
            curr_y += dy
            if self.map[curr_y][curr_x] == "#":
                num_trees += 1
        return num_trees


def password_philosophy(map_str):
    tobaggan_map = TobagganMap(map_str)
    print(f"part 1: {tobaggan_map.count_trees_on_slope(3, 1)} trees")
    totals = [
        tobaggan_map.count_trees_on_slope(1, 1),
        tobaggan_map.count_trees_on_slope(3, 1),
        tobaggan_map.count_trees_on_slope(5, 1),
        tobaggan_map.count_trees_on_slope(7, 1),
        tobaggan_map.count_trees_on_slope(1, 2)
    ]
    part_2_ans = 1
    for total in totals:
        part_2_ans *= total
    print(f"part 2: {part_2_ans}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    password_philosophy(inp)
