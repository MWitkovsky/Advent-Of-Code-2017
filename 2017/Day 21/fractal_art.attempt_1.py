import sys
sys.path.append("../../")

from lib import utils

init_pattern = ".#./..#/###"

class RuleBook(object):
    def __init__(self, rulebook_string):
        rules = rulebook_string.splitlines()
        rules = [rule.split(" => ") for rule in rules]
        self.rules = {rule[0]:rule[1] for rule in rules}

    def lookup_rule(self, pattern):
        def flip(pattern):
            return [line[::-1] for line in pattern]

        num_rotates = 0
        def rotate(pattern):
            if len(pattern[0]) == 3:
                new_pattern = [[0,0,0],[0,pattern[1][1],0],[0,0,0]]
                new_pattern[0][0] = pattern[2][0]
                new_pattern[1][0] = pattern[2][1]
                new_pattern[2][0] = pattern[2][2]
                new_pattern[0][2] = pattern[0][0]
                new_pattern[1][2] = pattern[0][1]
                new_pattern[2][2] = pattern[0][2]
                new_pattern[0][1] = pattern[1][0]
                new_pattern[2][1] = pattern[1][2]
            else:
                new_pattern = [[0,0],[0,0]]
                new_pattern[0][0] = pattern[1][0]
                new_pattern[0][1] = pattern[0][0]
                new_pattern[1][0] = pattern[1][1]
                new_pattern[1][1] = pattern[0][1]
            return ["".join(line) for line in new_pattern]

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

class SubPixelGrid(object):
    split_format = "{0}{1}/{2}{3}"

    def __init__(self, grid_string):
        self.pattern = grid_string.split("/")
        self.split = False

    def _split_grid(self):
        self.split = True
        self.tl = SubPixelGrid(SubPixelGrid.split_format.format(self.pattern[0][0],self.pattern[0][1],
                                                                self.pattern[1][0],self.pattern[1][1]))
        self.tr = SubPixelGrid(SubPixelGrid.split_format.format(self.pattern[0][2],self.pattern[0][3],
                                                                self.pattern[1][2],self.pattern[1][3]))
        self.bl = SubPixelGrid(SubPixelGrid.split_format.format(self.pattern[2][0],self.pattern[2][1],
                                                                self.pattern[3][0],self.pattern[3][1]))
        self.br = SubPixelGrid(SubPixelGrid.split_format.format(self.pattern[2][2],self.pattern[2][3],
                                                                self.pattern[3][2],self.pattern[3][3]))

    def update_pattern(self, rulebook):
        if not self.split:
            self.pattern = rulebook.lookup_rule(self.pattern)
            if len(self.pattern[0]) % 2 == 0:
                self._split_grid()
        else:
            self.tl.update_pattern(rulebook)
            self.tr.update_pattern(rulebook)
            self.bl.update_pattern(rulebook)
            self.br.update_pattern(rulebook)

    def __str__(self):
        if not self.split:
            return "\n".join(self.pattern)
        else:
            ret = ""
            lstr = self.tl.__str__().splitlines()
            lstr.extend(self.bl.__str__().splitlines())
            rstr = self.tr.__str__().splitlines()
            rstr.extend(self.br.__str__().splitlines())
            for i, line in enumerate(lstr):
                ret += "{0}|{1}\n".format(line, rstr[i])
                if len(lstr)/2-1 == i:
                    ret += ("-"*(len(line)*2+1)) + "\n"
            return ret

def part1(rulebook, pixel_grid):
    print("0:\n{0}\n".format(pixel_grid))
    for i in range(1,11):
        pixel_grid.update_pattern(rulebook)
        print("{0}:\n{1}".format(i, pixel_grid))
    print("Part 1: {0}".format(pixel_grid.__str__().count("#")))

def part2(data):
    pass


def fractal_art(string):
    rulebook = RuleBook(string)
    pixel_grid = SubPixelGrid(init_pattern)
    part1(rulebook, pixel_grid)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    fractal_art(inp)
