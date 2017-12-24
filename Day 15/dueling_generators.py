import sys

A_FACTOR = 16807
B_FACTOR = 48271
MOD = 2147483647

def bin(a):
    s=''
    t={'0':'000','1':'001','2':'010','3':'011',
       '4':'100','5':'101','6':'110','7':'111'}
    for c in oct(a)[1:].replace("L", ""):
            s+=t[c]
    return s[::-1]

def dueling_generators(string):
    generator_inputs = string.splitlines()
    a = int(generator_inputs[0][generator_inputs[0].index("with ")+5:])
    b = int(generator_inputs[1][generator_inputs[1].index("with ")+5:])

    num_matches = 0
    target = 40000000
    i = 0
    while i < target:
        i += 1
        a = (a*A_FACTOR)%MOD
        b = (b*B_FACTOR)%MOD
        if bin(a)[0:16] == bin(b)[0:16]:
            num_matches += 1

    print "Part 1 Solution: %s" % num_matches

    num_matches = 0
    target = 5000000
    i = 0
    while i < target:
        i += 1
        a = (a*A_FACTOR)%MOD
        while a&3 != 0:
            a = (a*A_FACTOR)%MOD
        b = (b*B_FACTOR)%MOD
        while b&7 != 0:
            b = (b*B_FACTOR)%MOD
        if bin(a)[0:16] == bin(b)[0:16]:
            num_matches += 1
    print "Part 2 Solution: %s" % num_matches


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    dueling_generators(inp)
