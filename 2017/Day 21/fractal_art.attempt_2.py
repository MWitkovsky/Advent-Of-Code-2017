import sys
sys.path.append("../../")

from lib import utils

init_pattern = ".#./..#/###"

def rotate_matrix(matrix):
    return list(zip(*reversed(matrix)))

class RuleBook(object):
    def __init__(self, rulebook_string):
        rules = rulebook_string.splitlines()
        rules = [rule.split(" => ") for rule in rules]
        self.rules = {rule[0]:rule[1] for rule in rules}

    def lookup_rule(self, pattern):
        def flip(pattern):
            return [line[::-1] for line in pattern]

        def rotate(pattern):
            return ["".join(line) for line in rotate_matrix(pattern)]

        def check_rulebook(pattern):
            return self.rules.get("/".join(pattern))

        pattern_string = "/".join(pattern)
        if pattern_string in self.rules:
            return self.rules[pattern_string].split("/")

        while True:
            for i in range(4):
                pattern = rotate(pattern)
                result = check_rulebook(pattern)
                if result:
                    return result.split("/")
            pattern = flip(pattern)
            result = check_rulebook(pattern)
            if result:
                return result.split("/")

class PixelGrid(object):
    def __init__(self, grid_string):
        self.pattern = grid_string.split("/")

    def update_pattern(self, rulebook):
        if len(self.pattern) == 3:
            self.pattern = rulebook.lookup_rule(self.pattern)
            return

        new_patterns = []
        new_grid = []
        if len(self.pattern[0]) & 1 == 0:
            grid_row = 0
            for row in range(0, len(self.pattern), 2):
                new_grid.append("")
                new_grid.append("")
                new_grid.append("")
                for col in range(0, len(self.pattern), 2):
                    new_pattern = ""
                    new_pattern += "{0}{1}\n".format(self.pattern[row][col], self.pattern[row][col+1])
                    new_pattern += "{0}{1}\n".format(self.pattern[row+1][col], self.pattern[row+1][col+1])
                    new_pattern = rulebook.lookup_rule(new_pattern.splitlines())
                    new_patterns.append(new_pattern)
                    new_grid[grid_row] += new_pattern[0]
                    new_grid[grid_row+1] += new_pattern[1]
                    new_grid[grid_row+2] += new_pattern[2]
                grid_row += 3
        else:
            grid_row = 0
            for row in range(0, len(self.pattern), 3):
                new_grid.append("")
                new_grid.append("")
                new_grid.append("")
                new_grid.append("")
                for col in range(0, len(self.pattern), 3):
                    new_pattern = ""
                    new_pattern += "{0}{1}{2}\n".format(self.pattern[row][col], self.pattern[row][col+1], self.pattern[row][col+2])
                    new_pattern += "{0}{1}{2}\n".format(self.pattern[row+1][col], self.pattern[row+1][col+1], self.pattern[row+1][col+2])
                    new_pattern += "{0}{1}{2}\n".format(self.pattern[row+2][col], self.pattern[row+2][col+1], self.pattern[row+2][col+2])
                    new_pattern = rulebook.lookup_rule(new_pattern.splitlines())
                    new_patterns.append(new_pattern)
                    new_grid[grid_row] += new_pattern[0]
                    new_grid[grid_row+1] += new_pattern[1]
                    new_grid[grid_row+2] += new_pattern[2]
                    new_grid[grid_row+3] += new_pattern[3]
                grid_row += 4

        self.pattern = new_grid


    def __str__(self):
        str = ""
        for line in self.pattern:
            str += "{0}\n".format(line)
        return str

def part1(rulebook, pixel_grid):
    print("0:\n{0}\n".format(pixel_grid))
    for i in range(1,19):
        pixel_grid.update_pattern(rulebook)
        print("{0}:\n{1}".format(i, pixel_grid))
    print("Part 1: {0}".format(pixel_grid.__str__().count("#")))

def part2(data):
    pass


def fractal_art(string):
    rulebook = RuleBook(string)
    pixel_grid = PixelGrid(init_pattern)
    part1(rulebook, pixel_grid)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    fractal_art(inp)
