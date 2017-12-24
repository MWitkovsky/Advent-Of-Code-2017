import sys

def a_series_of_tubes(string):
    string = string.splitlines()
    grid = []
    for line in string:
        grid.append(line)
    direction = {"x": 0, "y": 1}
    position = {"x": 0, "y": 0}
    message = []
    step_count = 0
    while True:
        char = grid[position["y"]][position["x"]]
        if char in ("|", "-"):
            position["x"] += direction["x"]
            position["y"] += direction["y"]
            step_count += 1
        elif char == "+":
            if abs(direction["y"]) == 1:
                direction["y"] = 0
                hi = position["x"]+1
                if hi < len(grid[position["y"]]):
                    char = grid[position["y"]][hi]
                    if char == "-":
                        direction["x"] = 1
                    else:
                        direction["x"] = -1
                else:
                    direction["x"] = -1
            else:
                direction["x"] = 0
                hi = position["y"] + 1
                if hi < len(grid) and len(grid[position["y"]+1]) > position["x"]:
                    if grid[position["y"]+1][position["x"]] == "|":
                        direction["y"] = 1
                    else:
                        direction["y"] = -1
                else:
                    direction["y"] = -1
            position["x"] += direction["x"]
            position["y"] += direction["y"]
            step_count += 1
        elif char == " ":
            break
        else:
            message.append(char)
            position["x"] += direction["x"]
            position["y"] += direction["y"]
            step_count += 1

    print "Part 1 Solution: %s" % "".join(message)
    print "Part 2 Solution: %s" % step_count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    a_series_of_tubes(inp)
