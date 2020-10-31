import json
from common.readini import Get_ini_data


def readjsondata():
    jsonfile = Get_ini_data().get_documentop_path()
    with open(jsonfile, 'r', encoding='utf8') as fp:
        return json.load(fp)


if __name__ == '__main__':
    print(readjsondata())
