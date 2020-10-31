import configparser
import datetime
import os
import time

from common.getfilepath import get_file_path



class Get_ini_data:
    def __init__(self):
        """
        初始化,获取ini路径，并进行配置文件读取
        """
        ini_file = get_file_path('PYTestRanzhiadduser\\testdata\\filepath.ini')
        # 实例化配置读取的一个类
        self.iniconfig = configparser.ConfigParser()
        # 读取配置文件
        self.iniconfig.read(ini_file)

    def get_los_path(self):
        """
        获取配置文件中的相对路径，返回电脑中的绝对路径
        :return:
        """
        return get_file_path(self.iniconfig.get('path', 'logspath'))

    def get_adduser_yaml_path(self):
        """
        获取添加用户数据文件的完整路径
        :return:
        """
        return get_file_path(self.iniconfig.get('path', 'adduserpath'))
    def get_screenshot_path(self):
        """
        获取截图文件完整路径
        :return:
        """
        tim = '{}.png'.format(time.strftime("%Y_%m_%d_%H_%M_%S"))
        scr_beforpath = get_file_path(self.iniconfig.get('path', 'Screenshotpath'))
        scr_allpath = os.path.join(scr_beforpath, tim)
        return scr_allpath

    def get_case_path(self):
        """
        获取用例路径
        :return:
        """
        return get_file_path(self.iniconfig.get('path', 'Casepath'))

    def get_htmlreport_path(self):
        """
        获取HTML报告的完整路径
        :return:
        """
        return  get_file_path(self.iniconfig.get('path', 'Htmlreport'))
    def get_documentop_path(self):
        """
        返回文档库测试的数据信息
        :return:
        """
        return get_file_path(self.iniconfig.get('path', 'docoppath'))




if __name__ == '__main__':
    aa = Get_ini_data().get_htmlreport_path()
    print(aa)