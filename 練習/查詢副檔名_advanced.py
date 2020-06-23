from os.path import splitext

def get_file(filename):
    return splitext(filename[1][1:])

