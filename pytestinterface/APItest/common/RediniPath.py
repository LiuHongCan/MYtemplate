import configparser
import os
from APItest.common.GetPath import Getpath


class ReadIni:
    def __init__(self):
        pathini = os.path.join(os.path.dirname(os.getcwd()), "APItestConfig\APItest.ini")
        self.iniconfig = configparser.ConfigParser()
        self.iniconfig.read(pathini, encoding="utf8")

    def Readjsonpath(self):
        """
        获取json文档路径
        :return:
        """
        path = self.iniconfig.get("path", "jsonpath")
        return Getpath(path)

    def Readexcelpath(self):
        """
        获取Excel文档路径
        :return:
        """
        path = self.iniconfig.get("path", "excelpath")
        return Getpath(path)

    def ReadSheet(self):
        """
        获取sheet页名字
        :return:
        """
        path = self.iniconfig.get("path", "Sheet")
        return path

if __name__ == '__main__':
    print(ReadIni().ReadSheet())