import configparser
from common.getfullpath import getfullpathmethod


class ReadIni:
    """
    读取ini配置文件
    包含 相对路径，Sheet页名字等类容
    """

    def __init__(self):
        # 获取ini文件的完整路径
        inifile = getfullpathmethod(r'requesttesttools\config\filepath.ini')
        # 实例化读取ini文件的类
        self.iniconfig = configparser.ConfigParser()
        # 进行文件读取
        self.iniconfig.read(inifile, encoding='utf8')

    def readexcel(self):
        """
        读取excel完整路径
        :return:
        """
        path = self.iniconfig.get("EXCELPATH", "testtoolexcelpath")
        return getfullpathmethod(path)

    def redexcelsheet(self):
        """
        读取excel的Sheet页名字，如果要更换Sheet页，只需要在配置文件（.ini）中修改名字即可
        :return:
        """
        return self.iniconfig.get("EXCELSHEET", "SHEET")

    def readjson(self):
        """
        返回json文件的完整路径
        :return:
        """
        path = self.iniconfig.get("JSONPATH", "paramspath")
        print(path)
        return getfullpathmethod(path)

    def readtestcasepath(self):
        """
        获取用例保存的文件夹路径
        :return:
        """
        path = self.iniconfig.get("TESTCASEPATH", "testcasepath")
        return getfullpathmethod(path)

    def readtestcasefilename(self):
        """
        获取用例保存的文件名字
        :return:
        """
        filename = self.iniconfig.get("TESTCASEPATH", "testcasefile")
        return filename

    def readresultpath(self):
        """
        获取html报告保存的文件夹路径
        :return:
        """
        path = self.iniconfig.get("RESULTPATH", "resultpath")
        return getfullpathmethod(path)

    def readlogspath(self):
        path = self.iniconfig.get("LOGSPATH", "logspath")
        return getfullpathmethod(path)


if __name__ == '__main__':
    print(ReadIni().readjson())
    # a = ReadIni()
    pass
