import sys

def inverse_captcha(string):
    string += string[0]
    total = 0
    for i, char in enumerate(string):
        if i == len(string)-1:
            break
        if char == string[i+1]:
            total += int(char)
    print total

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    f = open(sys.argv[1], "r")
    inp = f.read()
    f.close()
    inverse_captcha(inp)
