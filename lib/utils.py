def read_file_to_string_by_path(path):
    f = open(path, "r")
    contents = f.read()
    f.close()
    return contents[:-1] if contents.endswith("\n") else contents


def lines_to_array(string):
    return string.splitlines()
