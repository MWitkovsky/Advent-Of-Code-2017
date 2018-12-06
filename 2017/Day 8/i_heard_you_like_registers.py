import sys

def check_cond(lhs, cond, rhs):
    if cond == "==":
        return lhs == rhs
    if cond == "!=":
        return lhs != rhs
    if cond == ">":
        return lhs > rhs
    if cond == "<":
        return lhs < rhs
    if cond == ">=":
        return lhs >= rhs
    if cond == "<=":
        return lhs <= rhs


def perform_op(lhs, op, rhs):
    if op == "inc":
        return lhs + rhs
    if op == "dec":
        return lhs - rhs


def i_heard_you_like_registers(string):
    instructions = [line.split(" if ") for line in string.splitlines()]
    registers = {}
    max_value = 0
    for instruction in instructions:
        condition = instruction[1].split(" ")
        instruction = instruction[0].split(" ")
        reg = instruction[0]
        op = instruction[1]
        val = int(instruction[2])
        lhs = condition[0]
        cond = condition[1]
        rhs = int(condition[2])
        if not registers.get(reg):
            registers[reg] = 0
        if not registers.get(lhs):
            registers[lhs] = 0
        if check_cond(registers[lhs], cond, rhs):
            registers[reg] = perform_op(registers[reg], op, val)
            if registers[reg] > max_value:
                max_value = registers[reg]

    print "Part 1 Solution: %s" % max(registers.values())
    print "Part 2 Solution: %s" % max_value


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    i_heard_you_like_registers(inp)
