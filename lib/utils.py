def read_file_to_string_by_path(path):
    f = open(path, "r")
    contents = f.read()
    f.close()
    return contents