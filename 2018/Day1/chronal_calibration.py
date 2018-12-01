import sys
sys.path.append("../../")

from lib import utils


def get_frequencies(string):
    lines = string.splitlines()
    for line in lines:
        yield int(line)


def analyize_frequencies(frequencies):
    freq_history = set()
    total_freq = 0
    for frequency in get_frequencies(frequencies):
        total_freq += frequency
    print ("part 1: {0}".format(total_freq))

    freq_history = set()
    total_freq = 0
    first_duplicate_freq = None
    while first_duplicate_freq is None:
        for frequency in get_frequencies(frequencies):
            total_freq += frequency
            if total_freq in freq_history:
                first_duplicate_freq = total_freq
                break
            freq_history.add(total_freq)
    print ("part 2: {0}".format(first_duplicate_freq))


def problem(frequencies):
    analyize_frequencies(frequencies)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    inp = utils.read_file_to_string_by_path(sys.argv[1])
    problem(inp)
