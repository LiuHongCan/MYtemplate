import os



def get_file_path(relative_path):
    """
    路径封装
    relative_path = 项目名开始的相对路径
    例如：'PYTestRanzhiadduser\result\logs\'
    :param relative_path:
    :return:
    """
    # 切割出项目名字
    proname = relative_path.split('\\')[0]
    # 获得电脑上的项目路径
    beforpath = os.path.dirname(__file__).split(proname)[0]
    # 返回该文件在电脑上的绝对路径
    return os.path.join(beforpath, relative_path)

if __name__ == '__main__':
    print(get_file_path('PYTestRanzhiadduser\\result\\logs\\'))