import sys

def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None

def perform_op(registers, instructions, pointer):
    instruction = instructions[pointer].split(" ")
    if not registers.get(instruction[1]):
        registers[instruction[1]] = 0
    if instruction[0] == "snd":
        return "snd", registers.get(instruction[1], 0)
    elif instruction[0] == "set":
        val = safe_int(instruction[2])
        if val is not None:
            registers[instruction[1]] = val
        else:
            registers[instruction[1]] = registers[instruction[2]]
    elif instruction[0] == "add":
        val = safe_int(instruction[2])
        if val is not None:
            registers[instruction[1]] += val
        else:
            registers[instruction[1]] += registers[instruction[2]]
    elif instruction[0] == "mul":
        val = safe_int(instruction[2])
        if val is not None:
            registers[instruction[1]] *= val
        else:
            registers[instruction[1]] *= registers[instruction[2]]
    elif instruction[0] == "mod":
        val = safe_int(instruction[2])
        if val is not None:
            registers[instruction[1]] %= val
        else:
            registers[instruction[1]] %= registers[instruction[2]]
    elif instruction[0] == "rcv":
        return "rcv", instruction[1]
    elif instruction[0] == "jgz":
        if registers[instruction[1]] > 0:
            val = safe_int(instruction[2])
            if val is not None:
                return "jump", pointer + val
            else:
                return "jump", pointer + registers[instruction[2]]
    return None, None


def duet(string):
    instructions = string.splitlines()
    registers = {}
    pointer = 0
    last_sound = -1
    while pointer >= 0 and pointer < len(instructions):
        result, val = perform_op(registers, instructions, pointer)
        if result == "snd":
            last_sound = val
        if result == "rcv":
            break
        if result == "jump":
            pointer = val
        else:
            pointer += 1

    print "Part 1 Solution: %s" % last_sound

    program0 = {"p": 0, "rcv_queue": [], "pointer": 0, "deadlocked": False}
    program1 = {"p": 1, "rcv_queue": [], "pointer": 0, "deadlocked": False}
    program1_send_count = 0
    deadlock_counter = 0
    while True:
        deadlock_counter += 1
        while not program0["deadlocked"]:
            result, val = perform_op(program0, instructions, program0["pointer"])
            if result == "snd":
                program1["rcv_queue"].append(val)
                program1["deadlocked"] = False
            if result == "rcv":
                if len(program0["rcv_queue"]) > 0:
                    program0[val] = program0["rcv_queue"].pop(0)
                else:
                    program0["deadlocked"] = True
                    deadlock_counter = 0
                    break
            if result == "jump":
                program0["pointer"] = val
            else:
                program0["pointer"] += 1

        while not program1["deadlocked"]:
            result, val = perform_op(program1, instructions, program1["pointer"])
            if result == "snd":
                program1_send_count += 1
                program0["rcv_queue"].append(val)
                program0["deadlocked"] = False
            if result == "rcv":
                if len(program1["rcv_queue"]) > 0:
                    program1[val] = program1["rcv_queue"].pop(0)
                else:
                    program1["deadlocked"] = True
                    deadlock_counter = 0
                    break
            if result == "jump":
                program1["pointer"] = val
            else:
                program1["pointer"] += 1

        if program0["deadlocked"] and program1["deadlocked"] and deadlock_counter > 0:
            break
        print program1_send_count


    print "Part 2 Solution: %s" % program1_send_count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    duet(inp)
