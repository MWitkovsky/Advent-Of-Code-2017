import sys

def spiral_memory(num):
    target = int(num)
    right = 0
    up = 0
    direction = ["right", "up", "left", "down"]
    curr_direction = direction[0]

    change_dir_counter = 0
    change_dir_limit = 1
    first_limit = True

    def change_direction(curr_dir, dirs):
        index = dirs.index(curr_dir)
        if index == 3:
            index = 0
        else:
            index += 1
        return dirs[index]


    for step in range(target):
        if step == 0:
            continue
        if curr_direction == "right":
            right += 1
        elif curr_direction == "up":
            up += 1
        elif curr_direction == "left":
            right -= 1
        else:
            up -= 1
        change_dir_counter += 1
        if change_dir_counter == change_dir_limit:
            if first_limit:
                first_limit = False
            else:
                change_dir_limit += 1
                first_limit = True
            curr_direction = change_direction(curr_direction, direction)
            change_dir_counter = 0

    print "right: %s\nup: %s\ntotal: %s" % (str(right), str(up), str(abs(right)+abs(up)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    spiral_memory(inp)
