import json

from APItest.common.RediniPath import ReadIni


def ReadJsonData():
    file = ReadIni().Readjsonpath()
    with open(file, encoding="utf8") as fp:
        return json.loads(fp.read())

if __name__ == '__main__':
    print(ReadJsonData())