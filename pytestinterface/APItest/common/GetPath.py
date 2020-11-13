import os



def Getpath(path):
    beforpath = os.path.dirname(os.getcwd())
    return os.path.join(beforpath, path)


if __name__ == '__main__':
    pass