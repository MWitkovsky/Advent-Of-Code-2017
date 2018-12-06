import sys
sys.path.append("../../")

from lib import utils
from collections import Counter, defaultdict

c = Counter()

fabric_snippets = {}
class FabricSnippet:
    largest_x = 0
    largest_y = 0
    grid = None

    def __init__(self, def_line):
        def_line = def_line.split(" ")
        self.id = int(def_line[0][1:])

        xy = def_line[2].split(",")
        self.x = int(xy[0])
        self.y = int(xy[1][:-1])

        dimensions = def_line[3].split("x")
        self.width = int(dimensions[0])
        self.height = int(dimensions[1])

        if (self.x + self.width) > FabricSnippet.largest_x:
            FabricSnippet.largest_x = self.x + self.width

        if (self.y + self.height) > FabricSnippet.largest_y:
            FabricSnippet.largest_y = self.y + self.height

    @staticmethod
    def _init_grid():
        FabricSnippet.grid = []
        for y in range(FabricSnippet.largest_y):
            FabricSnippet.grid.append([None]*FabricSnippet.largest_x)
        print ("Grid Dimensions: {}{}{}".format(len(FabricSnippet.grid), "X",
                                                len(FabricSnippet.grid[0])))

    @staticmethod
    def build_fabric_grid():
        FabricSnippet._init_grid()
        overlapping_cuts = set()
        winner_candidates = set()
        for id, snippet in fabric_snippets.items():
            winner_candidates.add(id)
            for y in range(snippet.y, (snippet.y+snippet.height), 1):
                for x in range(snippet.x, (snippet.x+snippet.width), 1):
                    grid_val = FabricSnippet.grid[y][x]
                    if grid_val is not None:
                        overlapping_cuts.add("{0},{1}".format(y, x))
                        if grid_val in winner_candidates:
                            winner_candidates.remove(grid_val)
                        if id in winner_candidates:
                            winner_candidates.remove(id)
                    FabricSnippet.grid[y][x] = id
        return len(overlapping_cuts), winner_candidates



def no_matter_how_you_slice_it(inp):
    inp = utils.lines_to_array(inp)
    for i, line in enumerate(inp):
        fabric_snippets[i+1] = FabricSnippet(line)
    num_overlap, winner = FabricSnippet.build_fabric_grid()

    print ("part 1: {0}".format(num_overlap))
    print ("part 2: {0}".format(winner))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    no_matter_how_you_slice_it(inp)
